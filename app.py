from flask import Flask, request, jsonify
from config import API_KEY
from sessions import get_session
from detector import detect_scam
from extractor import extract_intelligence
from agent import agent_reply
from callback import send_final_callback

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze():
    if request.headers.get("x-api-key") != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

    data = request.json
    session_id = data["sessionId"]
    message_text = data["message"]["text"]

    session = get_session(session_id)
    session["messages"].append(message_text)

    scam, _ = detect_scam(message_text)
    if scam:
        session["scamDetected"] = True

    extract_intelligence(message_text, session["extracted"])
    print("Extracted Data :",
    session["extracted"])

    reply = "Okay."
    if session["scamDetected"]:
        reply = agent_reply(session, message_text)

    if session["agentState"] == "END":
        send_final_callback(session_id, session)

    return jsonify({
        "status": "success",
        "reply": reply
    })

if __name__ == "__main__":
    app.run(debug=True)
