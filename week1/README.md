# Week 1 Assignment: your first finance agent

Read [`resources/week1.md`](../resources/week1.md) first.

## Tasks
1. **Setup.** Get one free LLM working and run `python week1/agent.py` without errors.
2. **Finish the tools** in `week1/tools.py`:
   - `get_price(ticker)` is already done. Read it and understand it.
   - `get_ratios(ticker)` is **TODO**. Return the P/E ratio, profit margin and debt-to-equity.
3. **Make the agent answer:** *"Is TCS more profitable than Infosys right now?"* It should call your tools and return a structured answer (verdict, numbers used, one-line reasoning). The skeleton is in `agent.py`.
4. **Write half a page** (`week1/notes.md`): what did the LLM get right, and where did it guess or get something wrong?

## Tips
- Indian tickers on yfinance end in `.NS`: `TCS.NS`, `INFY.NS`, `RELIANCE.NS`, `HDFCBANK.NS`.
- If the model "answers" without calling a tool, that's a hallucination. Make your prompt stricter.
- `yf.Ticker("TCS.NS").info` returns a big dictionary. Print it once and look around.

## Submit
Push to your repo and share the link in the group before the Week 1 check-in.
