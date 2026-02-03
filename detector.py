SCAM_KEYWORDS = [
    "blocked", "verify", "urgent", "account", "upi",
    "suspended", "click", "immediately"
]

def detect_scam(text):
    text_lower = text.lower()
    hits = [k for k in SCAM_KEYWORDS if k in text_lower]
    return len(hits) >= 2, hits
