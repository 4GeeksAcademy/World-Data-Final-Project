from flask import Flask, request, render_template
from pickle import load

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def index():
    image_path = None
    vehicle_type = None

    if request.method == "POST":
        vehicle_type = request.form.get("vehicle_type")
        # By default, Flask renders static files from the static directory
        image_path = f"/static/images/{vehicle_type}/arima_forecast_vs_actual.png"

    return render_template("index.html", image_path=image_path, vehicle_type=vehicle_type)

    