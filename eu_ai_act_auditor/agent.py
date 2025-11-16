

"""LLM Auditor for verifying AI agents against the EU AI Act."""

from google.adk.agents import LlmAgent
from google.adk.tools import agent_tool
from . import prompt

from .sub_agents.risk_assesor import risk_assesment_agent
from .sub_agents.data_governor import data_governance_agent
from .sub_agents.transparency_assesor import transparency_agent
from .sub_agents.accuracy_robustness_security import accuracy_robustness_security_agent
from .sub_agents.conformity_assessment import conformity_assessment_agent
from .sub_agents.human_oversight import human_oversight_agent
from .sub_agents.post_market_monitoring import post_market_monitoring_agent
from .sub_agents.technical_documentation import technical_documentation_agent
from .sub_agents.risk_management_monitoring import risk_managment_monitoring_agent

risk_assesment_tool = agent_tool.AgentTool(agent=risk_assesment_agent)
data_governance_tool = agent_tool.AgentTool(agent=data_governance_agent)
transparency_tool = agent_tool.AgentTool(agent=transparency_agent)
accuracy_robustness_security_tool = agent_tool.AgentTool(agent=accuracy_robustness_security_agent)
conformity_assessment_tool = agent_tool.AgentTool(agent=conformity_assessment_agent)
human_oversight_tool = agent_tool.AgentTool(agent=human_oversight_agent)
post_market_monitoring_tool = agent_tool.AgentTool(agent=post_market_monitoring_agent)
technical_documentation_tool = agent_tool.AgentTool(agent=technical_documentation_agent)
risk_management_monitoring_tool = agent_tool.AgentTool(agent=risk_managment_monitoring_agent)

root_agent = LlmAgent(
    model= 'gemini-2.0-flash',
    name='eu_ai_act_auditor',
    instruction=prompt.ORCHESTRATOR_PROMPT,
    tools = [
        risk_assesment_tool,
        data_governance_tool,
        transparency_tool,
        accuracy_robustness_security_tool,
        conformity_assessment_tool,
        human_oversight_tool,
        post_market_monitoring_tool,
        technical_documentation_tool,
        risk_management_monitoring_tool
    ]
)
