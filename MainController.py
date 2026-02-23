import os
from openai import OpenAI

AllowedEvents = {"100m", "200m", "400m"}

def validate_event(event: str) -> list[str]:
    if event not in AllowedEvents:
        return [f"Event '{event}' is not supported."]
    return []

def schedule_to_text(schedule: dict) -> str:
    day_names = {"mon":"Mon","tue":"Tue","wed":"Wed","thu":"Thu","fri":"Fri","sat":"Sat","sun":"Sun"}
    lines = []
    for key in ["mon","tue","wed","thu","fri","sat","sun"]:
        text = (schedule.get(key) or "").strip()
        if text:
            lines.append(f"{day_names[key]}: {text}")
    return "\n".join(lines)

def generate_ai_feedback(event: str, plan_text: str) -> str:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        return "Missing OPENAI_API_KEY environment variable."

    client = OpenAI(api_key=api_key)

    instructions = (
        "You are a sprint coach assistant. Only discuss 100m/200m/400m. "
        "Use ONLY the plan provided. Do not invent extra sessions. "
        "Return: 3 strengths, 3 risks, 3 specific improvements."
    )

    prompt = f"Event: {event}\nWeekly plan:\n{plan_text}"

    resp = client.responses.create(
        model="gpt-5.2",
        instructions=instructions,
        input=prompt,
    )
    return resp.output_text