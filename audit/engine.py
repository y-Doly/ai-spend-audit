import json

with open("data/pricing.json") as f:
    pricing = json.load(f)


def audit_all_tools(tools, use_case):

    results = []

    total_savings = 0

    # ---------------------------
    # ChatGPT Logic
    # ---------------------------

    chatgpt = tools.get("chatgpt")

    if (
        chatgpt
        and chatgpt["plan"] == "team"
        and chatgpt["users"] < 3
    ):

        team_price = pricing["chatgpt"]["team"]

        plus_price = pricing["chatgpt"]["plus"]

        savings = (
            team_price - plus_price
        ) * chatgpt["users"]

        results.append({
            "tool": "ChatGPT",
            "recommendation": "Switch to Plus",
            "savings": savings,
            "reason": "Small teams usually do not need Team plan"
        })

        total_savings += savings

    # ---------------------------
    # GitHub Copilot Logic
    # ---------------------------

    copilot = tools.get("copilot")

    if (
        copilot
        and use_case == "coding"
        and copilot["plan"] == "business"
        and copilot["users"] < 3
    ):

        savings = (
            pricing["copilot"]["business"]
            - pricing["copilot"]["individual"]
        ) * copilot["users"]

        results.append({
            "tool": "GitHub Copilot",
            "recommendation": "Switch to Individual",
            "savings": savings,
            "reason": "Business plan is expensive for very small developer teams"
        })

        total_savings += savings

    # ---------------------------
    # Cursor Logic
    # ---------------------------

    cursor = tools.get("cursor")

    if (
        cursor
        and cursor["plan"] == "business"
        and cursor["users"] < 3
    ):

        savings = (
            pricing["cursor"]["business"]
            - pricing["cursor"]["pro"]
        ) * cursor["users"]

        results.append({
            "tool": "Cursor",
            "recommendation": "Switch to Pro",
            "savings": savings,
            "reason": "Business plan is excessive for small teams"
        })

        total_savings += savings

    # ---------------------------
    # Claude Logic
    # ---------------------------

    claude = tools.get("claude")

    if (
        claude
        and claude["plan"] == "team"
        and claude["users"] < 3
    ):

        savings = (
            pricing["claude"]["team"]
            - pricing["claude"]["pro"]
        ) * claude["users"]

        results.append({
            "tool": "Claude",
            "recommendation": "Switch to Pro",
            "savings": savings,
            "reason": "Team plan may not be necessary for smaller teams"
        })

        total_savings += savings

    # ---------------------------
    # Gemini Logic
    # ---------------------------

    gemini = tools.get("gemini")

    if (
        gemini
        and gemini["plan"] == "ultra"
        and gemini["users"] < 3
    ):

        savings = (
            pricing["gemini"]["ultra"]
            - pricing["gemini"]["pro"]
        ) * gemini["users"]

        results.append({
            "tool": "Gemini",
            "recommendation": "Switch to Pro",
            "savings": savings,
            "reason": "Ultra plan may be unnecessary for smaller teams"
        })

        total_savings += savings

    return {
        "results": results,
        "total_savings": total_savings
    }