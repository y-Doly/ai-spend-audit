def generate_summary(total_savings, recommendations):

    if total_savings == 0:
        return "No major savings opportunities detected."

    summary = (
        f"You could save approximately "
        f"${total_savings} per month.\n\n"
    )

    for item in recommendations:

        summary += (
            f"- {item['tool']}: "
            f"{item['recommendation']} "
            f"(Save ${item['savings']})\n"
        )

    return summary