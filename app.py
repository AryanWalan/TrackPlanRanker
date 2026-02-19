from flask import Flask, render_template, request
from MainController import AllowedEvents, validate_event  

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    errors = []
    selected_event = None
    success_message = None
    schedule = None

    if request.method == "POST":
        selected_event = request.form.get("event", "")
        errors = validate_event(selected_event)

        schedule = {
            "mon": request.form.get("mon", "").strip(),
            "tue": request.form.get("tue", "").strip(),
            "wed": request.form.get("wed", "").strip(),
            "thu": request.form.get("thu", "").strip(),
            "fri": request.form.get("fri", "").strip(),
            "sat": request.form.get("sat", "").strip(),
            "sun": request.form.get("sun", "").strip(),
        }

        if not any(schedule.values()):
            errors.append("Please enter at least one day of training.")

        if not errors:
            success_message = f"Event '{selected_event}' accepted. Plan received!"

    return render_template(
        "index.html",
        events=sorted(AllowedEvents),
        errors=errors,
        selected_event=selected_event,
        schedule=schedule,
        success_message=success_message
    )

if __name__ == "__main__":
    app.run(debug=True)
