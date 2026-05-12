from flask import Flask, render_template, request
from audit.engine import audit_tool
from utils.summary import generate_summary
from database import init_db, save_lead

init_db()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/audit", methods=["POST"])
def audit():
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

    save_lead(email, company, role)

    return "Lead saved successfully!"

if __name__ == "__main__":
    app.run(debug=True)