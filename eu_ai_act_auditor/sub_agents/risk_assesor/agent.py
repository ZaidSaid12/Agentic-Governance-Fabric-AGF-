"""Risk Classification Agent for EU AI Act compliance auditing."""

from google.adk import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.models import LlmResponse
from google.genai import types

from . import prompt

# Prompt template for risk classification
RISK_CLASSIFICATION_PROMPT = """
You are an EU AI Act compliance auditor.

Behavior:
1. Ask the user to describe the AI system (purpose, domain, functionality).
2. Determine if the system falls into a high-risk category according to Annex II of the EU AI Act.
3. Identify which compliance requirements are mandatory for this system.

Output format:
- risk_level: "High-Risk" | "Limited-Risk" | "Minimal-Risk"
- applicable_compliance_areas: List of compliance areas (e.g., Data Governance, Transparency, Human Oversight)
"""

def _format_response(
    callback_context: CallbackContext,
    llm_response: LlmResponse,
) -> LlmResponse:
    """Formats the LLM response into structured output."""
    del callback_context

    # Combine all parts into a single string
    if llm_response.content and llm_response.content.parts:
        full_text = '\n'.join(part.text or '' for part in llm_response.content.parts)
        llm_response.content.parts = [types.Part(text=full_text)]

    return llm_response


risk_assesment_agent = Agent(
    model='gemini-2.5-flash',
    name='risk_assesment_agent',
    instruction=prompt.RISK_CLASSIFICATION_PROMPT,
    tools=[],
    after_model_callback=_format_response,
)
