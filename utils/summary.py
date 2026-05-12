from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_summary(total_savings, recommendations):

    prompt = f"""
    Summarize this AI spend audit in about 100 words.

    Total monthly savings: ${total_savings}

    Recommendations:
    {recommendations}
    """

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response.choices[0].message.content

    except:
        return f"You could save approximately ${total_savings} per month by optimizing your AI software stack."