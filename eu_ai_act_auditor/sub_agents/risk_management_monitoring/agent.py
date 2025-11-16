"""Transparency & Information Provision auditing agent for EU AI Act compliance."""

from google.adk import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmResponse

from . import prompt

def _after_model_callback(
    callback_context: CallbackContext,
    llm_response: LlmResponse,
) -> LlmResponse:
    """
    Post-process LLM output if needed.
    Currently a placeholder; can be extended to clean up or validate output.
    """
    del callback_context  # unused
    return llm_response


risk_managment_monitoring_agent = Agent(
    model='gemini-2.5-flash',
    name='risk_managment_monitoring_agent',
    instruction=prompt.RISK_MANAGEMENT_MONITORING_PROMPT,
    after_model_callback=_after_model_callback,
)
