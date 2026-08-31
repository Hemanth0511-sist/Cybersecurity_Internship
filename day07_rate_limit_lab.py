from flask import Flask, request, jsonify
from time import time

app = Flask(__name__)

# Simple in-memory rate limiter
attempt_log = {}

MAX_ATTEMPTS = 5
WINDOW_SECONDS = 30


@app.route("/login", methods=["POST"])
def login():

    client_ip = request.remote_addr
    current_time = time()

    # Get previous attempts
    attempts = attempt_log.get(client_ip, [])

    # Keep only attempts from the current time window
    attempts = [
        timestamp
        for timestamp in attempts
        if current_time - timestamp < WINDOW_SECONDS
    ]

    # Check rate limit
    if len(attempts) >= MAX_ATTEMPTS:
        return jsonify({
            "status": "blocked",
            "message": "Too many login attempts. Try again later."
        }), 429

    # Record this attempt
    attempts.append(current_time)
    attempt_log[client_ip] = attempts

    username = request.form.get("username", "")

    return jsonify({
        "status": "failed",
        "message": f"Login failed for {username}",
        "attempts_in_window": len(attempts)
    }), 401


@app.route("/")
def home():
    return """
    <h1>Day 7 Password Attack Defense Lab</h1>
    <p>Local Flask server is running.</p>
    <p>Rate limit: 5 attempts per 30 seconds.</p>
    """


if __name__ == "__main__":
    print("=" * 60)
    print("       DAY 7 - RATE LIMIT DEFENSE LAB")
    print("=" * 60)
    print("Server: http://127.0.0.1:5000")
    print("Limit : 5 attempts per 30 seconds")
    print("=" * 60)

    app.run(host="127.0.0.1", port=5000)