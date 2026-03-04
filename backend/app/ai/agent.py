from langchain.agents import initialize_agent, AgentType
from app.ai.registry import ProviderRegistry
from app.ai.tools.finance import calculate_affordability
from app.ai.tools.insurance import compare_life_insurance
from app.ai.tools.profile import extract_life_stage
from langchain_core.messages import SystemMessage

tools = [calculate_affordability, compare_life_insurance, extract_life_stage]

SYSTEM_PROMPT = """You are a highly skilled, professional lifetime financial consulting AI.
Your purpose is to help users understand their financial health, manage life stages, check affordability for major purchases, and understand life insurance options.
Use the provided tools whenever calculating affordability, comparing life insurance policies (Term vs Whole), or extracting the user's life stage (age, marital status, income, dependents).
Always be polite, encouraging, and clear.
Crucially, you MUST reply in the language specified by the user's preferences: {language}.
If the user specifies 繁體中文, your entire response (including tool thought processes if exposed) should ideally be in Traditional Chinese.
"""

def create_agent(provider_name: str, language: str = "English", model_kwargs: dict = None):
    kwargs = model_kwargs or {}
    llm = ProviderRegistry.get_provider(provider_name, **kwargs)

    # LangChain v0.1.20 initialize_agent for STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION
    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        agent_kwargs={
            "system_message": SystemMessage(content=SYSTEM_PROMPT.format(language=language))
        }
    )
    return agent
