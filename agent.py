from bot import groq_chat

SYSTEM_PROMPT = """
You are a normal Indian user.
You are slightly confused, cautious, and cooperative.
You do NOT know this is a scam.
You never accuse the sender.
You ask natural follow-up questions.
Keep replies short and human-like.
"""

def agent_reply(session, last_message):
    state = session["agentState"]

    if state == "INIT":
        session["agentState"] = "ENGAGE"
        return groq_chat(
            SYSTEM_PROMPT,
            f"The message says: '{last_message}'. Reply naturally."
        )

    if state == "ENGAGE":
        session["agentState"] = "GATHER"
        return groq_chat(
            SYSTEM_PROMPT,
            "Ask which bank or service this is related to."
        )

    if state == "GATHER":
        session["agentState"] = "CONFIRM"
        return groq_chat(
            SYSTEM_PROMPT,
            "Ask what exactly needs to be done."
        )

    if state == "CONFIRM":
        session["agentState"] = "END"
        return groq_chat(
            SYSTEM_PROMPT,
            "Say you are checking and ask them to wait."
        )

    return "Okay."
