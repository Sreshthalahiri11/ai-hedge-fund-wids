"""Week 1 tools: functions our agent can call instead of guessing."""
import yfinance as yf
from langchain_core.tools import tool


@tool
def get_price(ticker: str) -> dict:
    """Get the latest closing price and 1-month % change for an NSE stock.
    Use tickers like 'TCS.NS' or 'INFY.NS'."""
    hist = yf.Ticker(ticker).history(period="1mo")
    if hist.empty:
        return {"error": f"No data for {ticker}. Did you add .NS?"}
    last = float(hist["Close"].iloc[-1])
    first = float(hist["Close"].iloc[0])
    return {
        "ticker": ticker,
        "last_close": round(last, 2),
        "change_1m_pct": round((last / first - 1) * 100, 2),
    }


@tool
def get_ratios(ticker: str) -> dict:
    """Get key financial ratios for an NSE stock: P/E, profit margin and debt-to-equity."""
    # TODO (Week 1): use yf.Ticker(ticker).info and return a dict like
    # {"ticker": ..., "pe_ratio": ..., "profit_margin_pct": ..., "debt_to_equity": ...}
    # Hint: look for keys like 'trailingPE', 'profitMargins', 'debtToEquity'.
    # Some keys can be missing, so handle that instead of crashing.
    raise NotImplementedError("Finish get_ratios in week1/tools.py")


TOOLS = [get_price, get_ratios]
