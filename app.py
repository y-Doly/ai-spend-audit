from flask import Flask, render_template, request, redirect
from audit.engine import audit_all_tools
from utils.summary import generate_summary
from database import init_db, save_audit

from flask_mail import Mail, Message
from dotenv import load_dotenv

import sqlite3
import os
import json

load_dotenv()

app = Flask(__name__)

# Mail config
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASSWORD")

mail = Mail(app)

# Initialize database
init_db()

# Temporary storage
latest_results = {}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/audit", methods=["POST"])
def audit():

    global latest_results

    tools = {

        "chatgpt": {
            "plan": request.form.get("chatgpt_plan"),
            "spend": float(request.form.get("chatgpt_spend") or 0),
            "users": int(request.form.get("chatgpt_users") or 0)
        },

        "copilot": {
            "plan": request.form.get("copilot_plan"),
            "spend": float(request.form.get("copilot_spend") or 0),
            "users": int(request.form.get("copilot_users") or 0)
        },

        "cursor": {
            "plan": request.form.get("cursor_plan"),
            "spend": float(request.form.get("cursor_spend") or 0),
            "users": int(request.form.get("cursor_users") or 0)
        },

        "claude": {
            "plan": request.form.get("claude_plan"),
            "spend": float(request.form.get("claude_spend") or 0),
            "users": int(request.form.get("claude_users") or 0)
        },

        "gemini": {
            "plan": request.form.get("gemini_plan"),
            "spend": float(request.form.get("gemini_spend") or 0),
            "users": int(request.form.get("gemini_users") or 0)
        }
    }

    use_case = request.form.get("use_case")

    results = audit_all_tools(tools, use_case)

    latest_results = results

    summary = generate_summary(
        results["total_savings"],
        results["results"]
    )

    return render_template(
        "result.html",
        results=results,
        summary=summary
    )


@app.route("/save-lead", methods=["POST"])
def save_lead_route():

    email = request.form.get("email")
    company = request.form.get("company")
    role = request.form.get("role")

    recommendations = json.dumps(latest_results["results"])

    audit_id = save_audit(
        email,
        company,
        role,
        latest_results["total_savings"],
        recommendations
    )

    # Send confirmation email
    msg = Message(
        subject="Your AI Spend Audit Report",
        sender=app.config["MAIL_USERNAME"],
        recipients=[email]
    )

    msg.body = f"""
Thanks for using AI Spend Audit.

Estimated monthly savings:
${latest_results["total_savings"]}

Your public report:
http://127.0.0.1:5000/result/{audit_id}
"""

    # Prevent app crash if email fails
    try:
        mail.send(msg)

    except Exception as e:
        print("Email failed:", e)

    return redirect(f"/result/{audit_id}")


@app.route("/result/<int:audit_id>")
def public_result(audit_id):

    conn = sqlite3.connect("leads.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT total_savings, recommendations
    FROM audits
    WHERE id = ?
    """, (audit_id,))

    audit = cursor.fetchone()

    conn.close()

    if not audit:
        return "Audit not found"

    return render_template(
        "share.html",
        total_savings=audit[0],
        recommendations=json.loads(audit[1])
    )


if __name__ == "__main__":
    app.run(debug=True)