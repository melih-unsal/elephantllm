import  datetime

def get_current_date():
    today = datetime.date.today()
    return str(today)

MEMORY_NEED_PROMPT = """
Given a user command, determine whether executing the
command requires historical or previous information, or
whether it requires recalling the conversation content.
Conversation Content: My best day is 18th May.
Simply answer yes (A) or no (B) without explaining the
information:
Command: {user_input}
"""

SUMMARY_ENOUGH_CHECK_PROMPT = """
Given a user command, determine if it can be executed
correctly based solely on the summary historical
information provided. Simply answer yes (A) or no (B),
without explaining the information.

Command: {user_input}
"""

SUMMARIZATION_PROMPT = """
Below is a conversation between a user and an AI
assistant. Please provide a summary of the user's
question and the assistant's response in one
sentence each, with separate paragraphs, while
preserving key information as much as possible.

Conversation:

User: {user_input}
Assistant: {system_response}

Summary:
"""

HISTORY_BASED_PROMPT = """
Here is a conversation between a user and an AI
assistant. Please answer the user's current
question based on the history of the conversation:

History of the conversation:

{history_of_related_turn}

Previous conversation:

User: {previous_user_input}
Assistant: {previous_system_response}

###

User: {current_user_input}
Assistant:
"""
