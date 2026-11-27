"""Week 1: a tiny finance agent that uses tools and returns structured output."""
import os
import sys

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from pydantic import BaseModel, Field

sys.path.append(os.path.dirname(__file__))
from tools import TOOLS  # noqa: E402

load_dotenv()


def get_llm():
    provider = os.getenv("LLM_PROVIDER", "groq").lower()
    if provider == "ollama":
        from langchain_ollama import ChatOllama
        return ChatOllama(model=os.getenv("OLLAMA_MODEL", "llama3.1"), temperature=0)
    from langchain_groq import ChatGroq
    return ChatGroq(model=os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile"), temperature=0)


class Verdict(BaseModel):
    """The agent's final structured answer."""
    verdict: str = Field(description="Short answer to the question")
    numbers_used: dict = Field(description="The exact numbers the answer is based on")
    reasoning: str = Field(description="One-line explanation")


SYSTEM = (
    "You are a careful equity research analyst covering Indian stocks. "
    "Never guess numbers. Always call a tool to get data. NSE tickers end in .NS."
)


def run(question: str, max_steps: int = 6) -> Verdict:
    llm = get_llm()
    llm_tools = llm.bind_tools(TOOLS)
    tool_map = {t.name: t for t in TOOLS}
    messages = [SystemMessage(SYSTEM), HumanMessage(question)]

    for _ in range(max_steps):
        ai = llm_tools.invoke(messages)
        messages.append(ai)
        if not ai.tool_calls:
            break
        for call in ai.tool_calls:
            print(f"  🔧 {call['name']}({call['args']})")
            try:
                result = tool_map[call["name"]].invoke(call["args"])
            except Exception as e:  # e.g. get_ratios not finished yet
                result = {"error": str(e)}
            messages.append(ToolMessage(content=str(result), tool_call_id=call["id"]))

    # Second pass: force the final answer into our Pydantic schema
    return llm.with_structured_output(Verdict).invoke(
        messages + [HumanMessage("Give your final answer in the required format.")]
    )


if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else "Is TCS more profitable than Infosys right now?"
    print(f"❓ {q}")
    answer = run(q)
    print(answer.model_dump_json(indent=2))
