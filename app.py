from flask import Flask, render_template, request
from MainController import AllowedEvents, validate_event  # import your logic

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    errors = []
    selected_event = None

    if request.method == "POST":
        selected_event = request.form.get("event", "")
        errors = validate_event(selected_event)

        if not errors:
            return f"Event '{selected_event}' accepted. Ready to rank plan."

    return render_template(
        "index.html",
        events=sorted(AllowedEvents),
        errors=errors,
        selected_event=selected_event
    )

if __name__ == "__main__":
    app.run(debug=True)
