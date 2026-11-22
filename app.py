from datetime import date
from flask import Flask, jsonify, request
from flask_cors import CORS
from db import get_connection

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

SAMPLE_SERVICES = [
    {"id": 1, "name": "Facial & skincare", "starting_price": 499},
    {"id": 2, "name": "Hair care", "starting_price": 399},
    {"id": 3, "name": "Makeup", "starting_price": 999},
    {"id": 4, "name": "Manicure & pedicure", "starting_price": 599},
]

@app.get("/api/health")
def health():
    return jsonify({"status": "ok", "application": "LushLook API"})

@app.get("/api/services")
def services():
    return jsonify(SAMPLE_SERVICES)

@app.post("/api/bookings")
def create_booking():
    data = request.get_json(silent=True) or {}
    required = ("customer_name", "customer_email", "service_name", "appointment_date")
    missing = [field for field in required if not str(data.get(field, "")).strip()]
    if missing:
        return jsonify({"error": "Missing required fields: " + ", ".join(missing)}), 400
    try:
        appointment_date = date.fromisoformat(data["appointment_date"])
    except (TypeError, ValueError):
        return jsonify({"error": "Appointment date must use YYYY-MM-DD format."}), 400

    values = (
        str(data["customer_name"]).strip()[:100],
        str(data["customer_email"]).strip()[:150],
        str(data["service_name"]).strip()[:100],
        appointment_date,
        str(data.get("notes", "")).strip()[:500],
    )
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO bookings (customer_name, customer_email, service_name, appointment_date, notes) VALUES (%s, %s, %s, %s, %s)",
            values,
        )
        connection.commit()
        booking_id = cursor.lastrowid
        cursor.close()
        return jsonify({"message": "Booking request saved.", "booking_id": booking_id}), 201
    except Exception:
        app.logger.exception("Unable to save booking")
        return jsonify({"error": "Database unavailable. Check MySQL and environment variables."}), 503
    finally:
        if connection is not None:
            connection.close()

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
