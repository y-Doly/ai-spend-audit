def audit_tool(tool, plan, users, spend, use_case):
    result = {
        "tool": tool,
        "current_spend": spend,
        "recommendation": "No change",
        "savings": 0,
        "reason": "Looks fine"
    }

    if tool == "chatgpt":
        if plan.lower() == "team" and users < 3:
            savings = (30 - 20) * users
            result["recommendation"] = "Switch to ChatGPT Plus"
            result["savings"] = savings
            result["reason"] = "Team plan is expensive for small teams"

    return result