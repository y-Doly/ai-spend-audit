import json

with open("data/pricing.json") as f:
    pricing = json.load(f)


def audit_all_tools(tools, use_case):

    results = []
    total_savings = 0

    # ChatGPT logic
    chatgpt = tools["chatgpt"]

    if chatgpt["plan"] == "team" and chatgpt["users"] < 3:

        team_price = pricing["chatgpt"]["team"]
        plus_price = pricing["chatgpt"]["plus"]

        savings = (team_price - plus_price) * chatgpt["users"]

        results.append({
            "tool": "ChatGPT",
            "recommendation": "Switch to Plus",
            "savings": savings,
            "reason": "Small teams usually do not need Team plan"
        })

        total_savings += savings

    # Copilot logic
    copilot = tools["copilot"]

    if (
        use_case == "coding"
        and copilot["plan"] == "business"
        and copilot["users"] < 3
    ):

        business_price = pricing["copilot"]["business"]
        individual_price = pricing["copilot"]["individual"]

        savings = (
            business_price - individual_price
        ) * copilot["users"]

        results.append({
            "tool": "GitHub Copilot",
            "recommendation": "Switch to Individual",
            "savings": savings,
            "reason": "Business plan is expensive for very small developer teams"
        })

        total_savings += savings

    return {
        "results": results,
        "total_savings": total_savings
    }