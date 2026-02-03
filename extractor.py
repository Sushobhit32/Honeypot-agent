import re

def extract_intelligence(text, store):
    store["upiIds"].extend(re.findall(r'\b[\w.-]+@[\w.-]+\b', text))
    store["phoneNumbers"].extend(re.findall(r'\+91\d{10}', text))
    store["phishingLinks"].extend(re.findall(r'https?://\S+', text))

    keywords = ["urgent", "verify", "blocked", "suspended"]
    store["suspiciousKeywords"].extend(
        [k for k in keywords if k in text.lower()]
    )
