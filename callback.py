import requests
import os

FINAL_CALLBACK_URL = os.getenv("FINAL_CALLBACK_URL")

if not FINAL_CALLBACK_URL:
    raise RuntimeError("FINAL_CALLBACK_URL not set in environment variables")

def send_final_callback(session_id, session):
    payload = {
        "sessionId": session_id,
        "scamDetected": True,
        "totalMessagesExchanged": len(session["messages"]),
        "extractedIntelligence": session["extracted"],
        "agentNotes": "Scammer used urgency and payment redirection tactics"
    }

    try:
        requests.post(
            FINAL_CALLBACK_URL,
            json=payload,
            timeout=5
        )
    except Exception as e:
        print("Callback failed:", e)