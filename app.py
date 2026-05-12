from flask import Flask, render_template, request, redirect
from audit.engine import audit_tool
from utils.summary import generate_summary
from database import init_db, save_audit

init_db()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/audit", methods=["POST"])
def audit():
    global latest_results
    latest_results = results
    tool = request.form.get("tool")
    plan = request.form.get("plan")
    spend = float(request.form.get("spend"))
    users = int(request.form.get("users"))
    use_case = request.form.get("use_case")

    result = audit_tool(tool, plan, users, spend, use_case)

    return render_template("result.html", result=result)


@app.route("/save-lead", methods=["POST"])
def save_lead_route():

    email = request.form.get("email")
    company = request.form.get("company")
    role = request.form.get("role")

    recommendations = str(latest_results["results"])

    audit_id = save_audit(
        email,
        company,
        role,
        latest_results["total_savings"],
        recommendations
    )

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
        recommendations=audit[1]
    )


if __name__ == "__main__":
    app.run(debug=True)