import requests
from config import FINAL_CALLBACK_URL

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
