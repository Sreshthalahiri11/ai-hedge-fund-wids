# Build Your Own AI Hedge Fund 🤖📈
### Multi-agent LLMs that research, debate and trade Indian stocks · WiDS 6.0

When an equity analyst covers a stock, they read a 300-page annual report, go through the earnings call, check the news, look at the price trend, and argue both sides before they put a rating on it. In this project we build a team of AI agents that does that whole process for NIFTY 50 stocks.

```
 Fundamental Analyst ─┐
 Sentiment Analyst  ──┼──▶  Bull 🐂 vs Bear 🐻 debate ──▶ Risk Manager ──▶ Portfolio Manager ──▶ BUY / HOLD / SELL
 Technical Analyst  ──┘
```

Everything runs on **free or open models**, so you don't need paid API keys, and you don't need a finance background either.

---

## 🗺️ Roadmap

| Week | What we build | Resources |
|---|---|---|
| 1 | LLM basics, tool calling, finance crash course | [`resources/week1.md`](resources/week1.md) · [`week1/`](week1/) |
| 2 | Fundamental Analyst: agentic RAG over annual reports | coming soon |
| 3 | Sentiment and Technical Analysts (as MCP servers) | coming soon |
| 4 | The full multi-agent firm in LangGraph | coming soon |
| 5 | Backtesting and evals: does it actually work? | coming soon |
| 6 | Live dashboard, final demo, GRPO fine-tuning (stretch) | coming soon |

New folders get added each week, so run `git pull` at the start of every week.

---

## ⚙️ Setup

```bash
git clone https://github.com/Sreshthalahiri11/ai-hedge-fund-wids.git
cd ai-hedge-fund-wids
python -m venv venv
# Windows: venv\Scripts\activate     Mac/Linux: source venv/bin/activate
pip install -r requirements.txt
```

Then pick **one** free LLM:

- **Groq (easiest, free tier):** make a key at https://console.groq.com, copy `.env.example` to `.env`, and paste the key in.
- **Ollama (fully local, no key):** install from https://ollama.com, run `ollama pull llama3.1`, and set `LLM_PROVIDER=ollama` in `.env`.

Check that it works:

```bash
python week1/agent.py
```

Google Colab works too: clone the repo in a cell and use Groq.

---

## 📬 How submissions work

1. Fork this repo (or make your own) and push your work to it every week.
2. Every weekly folder has a `README.md` with that week's assignment.
3. Share your repo link in the group before the weekly check-in.

Stuck? Ask in the group. Nobody gets judged for asking basic doubts. Half of this stuff is new for everyone, me included.

---

**Mentor:** Sreshtha Lahiri (24B0614)
