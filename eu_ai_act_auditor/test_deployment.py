from google.adk.client import ADKClient

# Your deployed agent engine ID
AGENT_ENGINE_ID = "2012700015109079040"
USER_ID = "esra_test_user"

# Create the ADK client
client = ADKClient(resource_id=AGENT_ENGINE_ID)

# Create a session for the user
session = client.create_session(user_id=USER_ID)

# Send a message to the agent
response = session.send_message("Hello, what can you do for me?")
print("Agent response:", response.text)

# Example: continue conversation
response = session.send_message("I want to analyze AAPL stock")
print("Agent response:", response.text)

# To close session if needed
session.close()
