import os
from google import genai
from dotenv import load_dotenv
from prompts import SYSTEM_PROMPT

# ---------------- Configuration ---------------- #

load_dotenv(encoding='utf-8-sig')

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found. Please add it to your .env file.\n"
        "Get your free key at: https://aistudio.google.com/apikey"
    )

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.5-flash"


def _call(prompt: str) -> str:
    """Central API call — all functions route through here."""
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"


# ---------------- Stock Analysis ---------------- #

def analyze_stock(stock_data, investment_amount=None, risk_appetite="Medium"):
    prompt = f"""
{SYSTEM_PROMPT}

Stock Data:
{stock_data}

Investment Amount:
{investment_amount}

Risk Appetite:
{risk_appetite}

Additionally include:

---------------------------------

Suggested Allocation

If investment amount is given,
recommend how much money should be invested in this stock.

If the stock is risky,
recommend keeping part of the money in cash, ETF or Gold.

---------------------------------

Explain:

• Why PE Ratio matters
• Why EPS matters
• Why ROE matters
• Why Debt matters
• Why Revenue Growth matters

Explain everything in simple English.
"""
    return _call(prompt)


# ---------------- Personal Finance Advisor ---------------- #

def personal_finance_advisor(question):
    prompt = f"""
You are Buffet AI.

You are an expert personal finance advisor.

Answer professionally.

Question:
{question}

Provide:

1. Recommendation
2. Reasoning
3. Risks
4. Best Practices
5. Final Advice
"""
    return _call(prompt)


# ---------------- Portfolio Review ---------------- #

def portfolio_review(portfolio):
    prompt = f"""
You are an experienced equity portfolio manager.

Portfolio:
{portfolio}

Analyze:

• Sector Diversification
• Risk
• Concentration
• Strengths
• Weaknesses
• Missing Sectors
• Overall Rating
• Suggested Improvements
"""
    return _call(prompt)


# ---------------- Retirement Advice ---------------- #

def retirement_advice(age, retirement_age, corpus):
    prompt = f"""
Current Age:
{age}

Retirement Age:
{retirement_age}

Retirement Corpus:
{corpus}

Analyze:

• Will this corpus be sufficient?
• What changes are needed?
• Investment Strategy
• Withdrawal Strategy
• Risks
"""
    return _call(prompt)


# ---------------- Explain Financial Metric ---------------- #

def explain_metric(metric_name, metric_value):
    prompt = f"""
Explain this financial metric in very simple language.

Metric:
{metric_name}

Value:
{metric_value}

Explain:

• What it means
• Why investors use it
• Whether this value is good or bad
• Give one simple example.
"""
    return _call(prompt)