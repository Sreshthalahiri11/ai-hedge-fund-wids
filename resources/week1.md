# Week 1 Resources: LLM basics, tool calling and a finance crash course

Expected time: **6–8 hours**. Go in order. Don't worry if some of it feels new, that's the point of week 1.

## Part A: How LLMs work (~2.5 hrs)
- **Intro to Large Language Models**, Andrej Karpathy (YouTube, ~1 hr). Watch this first.
- **But what is a GPT?** and **Attention in transformers**, 3Blue1Brown (YouTube, Deep Learning chapters 5 & 6)
- **Prompt engineering overview:** https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/overview. Read the parts on being clear and direct, giving examples, and structured output.

## Part B: Tool calling and structured outputs (~2 hrs)
- Set up one free model: **Groq** (https://console.groq.com), **Ollama** (https://ollama.com) or **Gemini** (https://aistudio.google.com)
- **LangChain tool calling:** https://python.langchain.com/docs/concepts/tool_calling/
- **Pydantic** (forcing clean JSON outputs): https://docs.pydantic.dev
- **yfinance** (free market data): https://github.com/ranaroussi/yfinance

## Part C: Finance crash course (~2 hrs)
- **Zerodha Varsity, Fundamental Analysis:** https://zerodha.com/varsity/module/fundamental-analysis/. Read the chapters on the P&L, balance sheet, cash flow statement and financial ratios.
- **Screener.in:** https://www.screener.in. Look up any NIFTY 50 company and get used to its 10-year financials.
- Open one real annual report (any NIFTY 50 company's Investor Relations page) and skim the *Management Discussion & Analysis* section. You'll see why we want an AI to read these.

## The paper behind this project (optional, skim)
- **TradingAgents: Multi-Agents LLM Financial Trading Framework** (Xiao et al., 2024): https://arxiv.org/abs/2412.20138. Read the abstract and look at the architecture figure.
- Code: https://github.com/TauricResearch/TradingAgents

➡️ Assignment: [`week1/README.md`](../week1/README.md)
