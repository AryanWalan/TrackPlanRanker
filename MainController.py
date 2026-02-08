from dataclasses import dataclass

AllowedEvents = {"100m", "200m", "400m"}

def validate_event(event: str) -> list[str]:
    if event not in AllowedEvents:
        return [f"Event '{event}' is not supported."]
    return []

