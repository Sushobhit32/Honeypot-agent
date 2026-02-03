sessions = {}

def get_session(session_id):
    if session_id not in sessions:
        sessions[session_id] = {
            "messages": [],
            "extracted": {
                "bankAccounts": [],
                "upiIds": [],
                "phishingLinks": [],
                "phoneNumbers": [],
                "suspiciousKeywords": []
            },
            "scamDetected": False,
            "agentState": "INIT"
        }
    return sessions[session_id]
