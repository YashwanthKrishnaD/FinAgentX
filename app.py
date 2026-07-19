import streamlit as st
import pandas as pd
import plotly.express as px

try:
    from tools import *
    print("TOOLS IMPORTED SUCCESSFULLY")
except Exception as e:
    print("TOOLS IMPORT FAILED:", e)
    raise
from calculators import *
from agent import *

st.set_page_config(
    page_title="FinAgentX",
    page_icon="💸",
    layout="wide"
)
st.markdown("""
<style>

/* Hide Streamlit branding */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Premium background */
.stApp{
    background:
    radial-gradient(circle at top left,#1e3a8a 0%,transparent 30%),
    radial-gradient(circle at top right,#7c3aed 0%,transparent 25%),
    linear-gradient(135deg,#0f172a,#111827,#020617);
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#0B1220;
}

/* Buttons */
.stButton > button{
    border-radius:12px;
    background:linear-gradient(90deg,#06b6d4,#8b5cf6);
    color:white;
    border:none;
    transition:0.3s;
}

.stButton > button:hover{
    transform:translateY(-2px);
    box-shadow:0 0 20px rgba(139,92,246,.4);
}

/* Inputs */
.stTextInput input,
.stNumberInput input{
    border-radius:12px;
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<h1 style='
text-align:center;
font-size:55px;
font-weight:800;
background:linear-gradient(90deg,#00E5FF,#8B5CF6);
-webkit-background-clip:text;
-webkit-text-fill-color:transparent;
'>
🚀 FinAgentX
</h1>
""", unsafe_allow_html=True) 
st.caption("Where AI meets investing. ")

# ---------------- Sidebar ---------------- #

st.sidebar.title("🗺️ Navigation")

page = st.sidebar.radio(
    "Choose Module",
    [
        "📃 Dashboard",
        "📈 Stock Analyzer",
        "👨🏻‍💼 AI Financial Advisor",
        "💼 Portfolio Analyzer",
        "🧮 Financial Calculators",
        "💰 Budget Planner",
        "❤️ Financial Health"
    ]
)

# ===================================================
# DASHBOARD
# ===================================================

if page == "📃 Dashboard":

    st.header("📊 Dashboard")

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("Features", "25+")

    with c2:
        st.metric("AI Model", "Gemini")

    with c3:
        st.metric("Stock Data", "Live")

    with c4:
        st.metric("Calculators", "8")

    st.divider()

    st.subheader("🚀 What FinAgentX Can Do")

    col1, col2 = st.columns(2)

    with col1:

        st.success("📈 AI Stock Analysis")

        st.write("""
- Live Stock Price
- PE Ratio
- EPS
- ROE
- Debt Analysis
- Revenue Growth
- Buffett Score
- Risk Score
- Buy / Hold / Sell Recommendation
- Investment Allocation
        """)

        st.success("💰 Personal Finance")

        st.write("""
- Budget Planner
- Savings Analysis
- Net Worth
- Emergency Fund
- Financial Health Score
        """)

    with col2:

        st.success("🧮 Financial Calculators")

        st.write("""
- EMI Calculator
- SIP Calculator
- SWP Calculator
- Retirement Planner
- Lumpsum Calculator
- CAGR Calculator
        """)

        st.success("👨🏻‍💼 AI Advisor")

        st.write("""
- Investment Advice
- Retirement Advice
- Portfolio Review
- Wealth Planning
- Goal Planning
        """)

    st.divider()

    st.subheader("⭐ Why FinAgentX?")

    st.info("""
Unlike traditional stock apps,

FinAgentX explains

✔ WHY a stock is good

✔ WHY a stock is risky

✔ WHY PE matters

✔ WHY EPS matters

✔ WHY ROE matters

instead of only displaying numbers.
""")

    st.subheader("🎯 Workflow")

    st.write("""
1. Select Stock Analyzer.

2. Enter Stock Symbol.

3. View Live Financial Data.

4. AI Generates Professional Equity Research Report.

5. Get Buy / Hold / Sell Recommendation.

6. Explore Calculators.

7. Ask AI Financial Questions.
""")
    
# ===================================================
# STOCK ANALYZER
# ===================================================

elif page == "📈 Stock Analyzer":

    st.header("📈 AI Stock Analyzer")

    col1, col2 = st.columns([2, 1])

    with col1:
        symbol = st.text_input(
            "Enter Stock Symbol",
            placeholder="AAPL, NVDA, TSLA, MSFT..."
        )

    with col2:
        risk = st.selectbox(
            "Risk Appetite",
            ["Low", "Medium", "High"]
        )

    investment = st.number_input(
        "Investment Amount",
        min_value=0.0,
        value=100000.0,
        step=1000.0
    )

    analyze = st.button(
        "🔍 Analyze Stock",
        use_container_width=True
    )

    if analyze:

        if symbol == "":
            st.warning("Please enter a stock symbol.")

        else:

            with st.spinner("Fetching stock data..."):

                try:

                    
                    data = get_stock_data(symbol)   

                    st.success("Stock data loaded successfully!")

                    st.divider()

                    st.subheader("🏢 Company Overview")

                    c1, c2 = st.columns(2)

                    with c1:

                        st.write("**Company** :", data["company"])
                        st.write("**Sector** :", data["sector"])
                        st.write("**Industry** :", data["industry"])
                        st.write("**Country** :", data["country"])
                        st.write("**Employees** :", data["employees"])

                    with c2:

                        st.write("**Market Cap** :", data["marketCap"])
                        st.write("**Enterprise Value** :", data["enterpriseValue"])
                        st.write("**Website** :", data["website"])

                    st.divider()

                    st.subheader("📊 Financial Metrics")

                    m1, m2, m3, m4 = st.columns(4)

                    with m1:
                        st.metric(
                            "Current Price",
                            data["currentPrice"]
                        )

                    with m2:
                        st.metric(
                            "PE Ratio",
                            data["pe"]
                        )

                    with m3:
                        st.metric(
                            "EPS",
                            data["eps"]
                        )

                    with m4:
                        st.metric(
                            "Forward PE",
                            data["forwardPE"]
                        )

                    m5, m6, m7, m8 = st.columns(4)

                    with m5:
                        st.metric(
                            "Revenue Growth",
                            data["revenueGrowth"]
                        )

                    with m6:
                        st.metric(
                            "ROE",
                            data["roe"]
                        )

                    with m7:
                        st.metric(
                            "Debt/Equity",
                            data["debtToEquity"]
                        )

                    with m8:
                        st.metric(
                            "Beta",
                            data["beta"]
                        )

                    m9, m10, m11, m12 = st.columns(4)

                    with m9:
                        st.metric(
                            "Profit Margin",
                            data["profitMargins"]
                        )

                    with m10:
                        st.metric(
                            "Dividend Yield",
                            data["dividendYield"]
                        )

                    with m11:
                        st.metric(
                            "52W High",
                            data["fiftyTwoWeekHigh"]
                        )

                    with m12:
                        st.metric(
                            "52W Low",
                            data["fiftyTwoWeekLow"]
                        )

                    st.divider()

                    score = buffett_score(data)

                    risk_score_value, risk_level = risk_score(data)

                    c1, c2 = st.columns(2)

                    with c1:

                        st.subheader("⭐ Buffett Score")

                        st.progress(score / 100)

                        st.metric(
                            "Score",
                            f"{score}/100"
                        )

                    with c2:

                        st.subheader("⚠ Risk Level")

                        st.metric(
                            "Risk Score",
                            risk_score_value
                        )

                        st.metric(
                            "Risk",
                            risk_level
                        )

                    st.divider()

                    st.subheader("📈 Stock Price History")

                    hist = history(symbol)

                    if not hist.empty:

                        fig = px.line(
                            hist,
                            x=hist.index,
                            y="Close",
                            title="1 Year Price History"
                        )

                        st.plotly_chart(
                            fig,
                            use_container_width=True
                        )

                    st.divider()

                    st.subheader("🤖 AI Equity Research Report")

                    with st.spinner("FinAgentX is analyzing the company..."):

                        report = analyze_stock(
                            data,
                            investment,
                            risk
                        )

                    st.markdown(report)

                except Exception as e:

                    st.error(e)

# ===================================================
# AI FINANCIAL ADVISOR
# ===================================================

elif page == "👨🏻‍💼 AI Financial Advisor":

    st.header("🤖 Buffet AI: The  Financial Advisor")

    st.write("Ask any finance or investment question.")

    question = st.text_area(
        "Your Question",
        placeholder="""Examples

Should I buy a house?

Should I invest ₹5 lakh?

Can I retire at 50?

Should I buy Gold or Stocks?

How much emergency fund do I need?

How should I diversify my portfolio?
"""
    )

    if st.button("Ask Buffet AI", use_container_width=True):

        if question.strip() == "":
            st.warning("Please enter a question.")

        else:

            with st.spinner("Thinking..."):

                answer = personal_finance_advisor(question)

            st.markdown(answer)


# ===================================================
# PORTFOLIO ANALYZER
# ===================================================

elif page == "💼 Portfolio Analyzer":

    st.header("💼 AI Portfolio Analyzer")

    st.write(
        "Enter stock symbols separated by commas.\n\nExample:\nAAPL,MSFT,NVDA,TSLA"
    )

    portfolio = st.text_area(
        "Portfolio",
        placeholder="AAPL,MSFT,NVDA"
    )

    if st.button("Analyze Portfolio", use_container_width=True):

        if portfolio.strip() == "":
            st.warning("Enter at least one stock.")

        else:

            with st.spinner("Analyzing Portfolio..."):

                result = portfolio_review(portfolio)

            st.markdown(result)

# ===================================================
# FINANCIAL CALCULATORS
# ===================================================

elif page == "🧮 Financial Calculators":

    st.header("🧮 Financial Calculators")

    calc = st.selectbox(
    "Choose Calculator",
    [
        "EMI Calculator",
        "SIP Calculator",
        "SWP Calculator",
        "Lumpsum Calculator",
        "Retirement Planner",
        "CAGR Calculator",
        "Emergency Fund",
        "Net Worth",
        "Financial Health",
        "Savings Rate"
    ]
)
    

    # ---------------- EMI ---------------- #

    if calc == "EMI Calculator":

        st.subheader("🏠 EMI Calculator")

        principal = st.number_input(
            "Loan Amount",
            min_value=0.0,
            value=1000000.0
        )

        rate = st.number_input(
            "Interest Rate (%)",
            min_value=0.0,
            value=8.5
        )

        years = st.number_input(
            "Loan Tenure (Years)",
            min_value=1,
            value=20
        )

        if st.button("Calculate EMI"):

            emi_value, total, interest = emi(
                principal,
                rate,
                years
            )

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric("Monthly EMI", f"₹ {emi_value:,.2f}")

            with c2:
                st.metric("Total Payment", f"₹ {total:,.2f}")

            with c3:
                st.metric("Total Interest", f"₹ {interest:,.2f}")

    # ---------------- SIP ---------------- #

    elif calc == "SIP Calculator":

        st.subheader("📈 SIP Calculator")

        monthly = st.number_input(
            "Monthly Investment",
            min_value=0.0,
            value=10000.0
        )

        rate = st.number_input(
            "Expected Return (%)",
            min_value=0.0,
            value=12.0,
            key="sip_rate"
        )

        years = st.number_input(
            "Investment Years",
            min_value=1,
            value=20,
            key="sip_years"
        )

        if st.button("Calculate SIP"):

            future, invested = sip(
                monthly,
                rate,
                years
            )

            gain = future - invested

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric("Invested", f"₹ {invested:,.2f}")

            with c2:
                st.metric("Future Value", f"₹ {future:,.2f}")

            with c3:
                st.metric("Profit", f"₹ {gain:,.2f}")

    # ---------------- SWP ---------------- #

    elif calc == "SWP Calculator":

        st.subheader("💸 SWP Calculator")

        corpus = st.number_input(
            "Initial Corpus",
            min_value=0.0,
            value=1000000.0
        )

        withdrawal = st.number_input(
            "Monthly Withdrawal",
            min_value=0.0,
            value=10000.0
        )

        rate = st.number_input(
            "Annual Return (%)",
            min_value=0.0,
            value=10.0,
            key="swp_rate"
        )

        years = st.number_input(
            "Withdrawal Years",
            min_value=1,
            value=20,
            key="swp_years"
        )

        if st.button("Calculate SWP"):

            remaining = swp(
                corpus,
                withdrawal,
                rate,
                years
            )

            st.metric(
                "Remaining Corpus",
                f"₹ {remaining:,.2f}"
            )

    # ---------------- LUMPSUM ---------------- #

    elif calc == "Lumpsum Calculator":

        st.subheader("💰 Lumpsum Investment Calculator")

        principal = st.number_input(
            "Investment Amount",
            min_value=0.0,
            value=100000.0,
            key="lump_principal"
        )

        rate = st.number_input(
            "Expected Return (%)",
            min_value=0.0,
            value=12.0,
            key="lump_rate"
        )

        years = st.number_input(
            "Investment Years",
            min_value=1,
            value=15,
            key="lump_years"
        )

        if st.button("Calculate Lumpsum"):

            future = lumpsum(
                principal,
                rate,
                years
            )

            st.metric(
                "Future Value",
                f"₹ {future:,.2f}"
            )

    # ---------------- RETIREMENT ---------------- #

    elif calc == "Retirement Planner":

        st.subheader("🏖 Retirement Planner")

        monthly_expense = st.number_input(
            "Current Monthly Expense",
            min_value=0.0,
            value=50000.0
        )

        current_age = st.number_input(
            "Current Age",
            min_value=18,
            value=25
        )

        retirement_age = st.number_input(
            "Retirement Age",
            min_value=current_age + 1,
            value=60
        )

        life_expectancy = st.number_input(
            "Life Expectancy",
            min_value=retirement_age + 1,
            value=85
        )

        inflation = st.number_input(
            "Inflation (%)",
            min_value=0.0,
            value=6.0
        )

        returns = st.number_input(
            "Expected Return (%)",
            min_value=0.0,
            value=10.0
        )

        if st.button("Plan Retirement"):

            future_expense, corpus = retirement(
                monthly_expense,
                current_age,
                retirement_age,
                life_expectancy,
                inflation,
                returns
            )

            c1, c2 = st.columns(2)

            with c1:
                st.metric(
                    "Monthly Expense at Retirement",
                    f"₹ {future_expense:,.2f}"
                )

            with c2:
                st.metric(
                    "Required Retirement Corpus",
                    f"₹ {corpus:,.2f}"
                )

    # ---------------- CAGR ---------------- #

    elif calc == "CAGR Calculator":

        st.subheader("📈 CAGR Calculator")

        beginning = st.number_input(
            "Beginning Value",
            min_value=1.0,
            value=100000.0
        )

        ending = st.number_input(
            "Ending Value",
            min_value=1.0,
            value=250000.0
        )

        years = st.number_input(
            "Years",
            min_value=1,
            value=5,
            key="cagr_years"
        )

        if st.button("Calculate CAGR"):

            growth = cagr(
                beginning,
                ending,
                years
            )

            st.metric(
                "CAGR",
                f"{growth:.2f}%"
            )

    # ---------------- EMERGENCY FUND ---------------- #

    elif calc == "Emergency Fund":

        st.subheader("🛡 Emergency Fund Calculator")

        expense = st.number_input(
            "Monthly Expense",
            min_value=0.0,
            value=50000.0,
            key="emergency_expense"
        )

        if st.button("Calculate Emergency Fund"):

            fund = emergency(expense)

            st.metric(
                "Recommended Emergency Fund",
                f"₹ {fund:,.2f}"
            )

    # ---------------- NET WORTH ---------------- #

    elif calc == "Net Worth":

        st.subheader("💰 Net Worth Calculator")

        assets = st.number_input(
            "Total Assets",
            min_value=0.0,
            value=5000000.0
        )

        liabilities = st.number_input(
            "Total Liabilities",
            min_value=0.0,
            value=1000000.0
        )

        if st.button("Calculate Net Worth"):

            worth = networth(
                assets,
                liabilities
            )

            st.metric(
                "Net Worth",
                f"₹ {worth:,.2f}"
            )

    # ---------------- FINANCIAL HEALTH ---------------- #

    elif calc == "Financial Health":

        st.subheader("❤️ Financial Health Score")

        savings = st.slider(
            "Savings Rate (%)",
            0,
            100,
            20
        )

        debt = st.slider(
            "Debt Ratio (%)",
            0,
            100,
            30
        )

        emergency_months = st.slider(
            "Emergency Fund (Months)",
            0,
            12,
            6
        )

        if st.button("Calculate Health Score"):

            score = health_score(
                savings,
                debt,
                emergency_months
            )

            st.progress(score / 100)

            st.metric(
                "Financial Health Score",
                f"{score}/100"
            )

            if score >= 80:
                st.success("Excellent Financial Health 🎉")

            elif score >= 60:
                st.info("Good Financial Health 👍")

            elif score >= 40:
                st.warning("Needs Improvement ⚠")

            else:
                st.error("Poor Financial Health ❌")

    # ---------------- SAVINGS RATE ---------------- #

    elif calc == "Savings Rate":

        st.subheader("💵 Savings Rate Calculator")

        income = st.number_input(
            "Monthly Income",
            min_value=0.0,
            value=100000.0
        )

        expense = st.number_input(
            "Monthly Expense",
            min_value=0.0,
            value=60000.0,
            key="saving_expense"
        )

        if st.button("Calculate Savings Rate"):

            rate = savings_rate(
                income,
                expense
            )

            st.metric(
                "Savings Rate",
                f"{rate:.2f}%"
            )

# ===================================================
# BUDGET PLANNER
# ===================================================

elif page == "💰 Budget Planner":

    st.header("💰 Monthly Budget Planner")

    income = st.number_input(
        "Monthly Income",
        min_value=0.0,
        value=100000.0
    )

    st.subheader("Monthly Expenses")

    rent = st.number_input("🏠 Rent / EMI", min_value=0.0, value=25000.0)
    food = st.number_input("🍽 Food", min_value=0.0, value=10000.0)
    transport = st.number_input("🚗 Transportation", min_value=0.0, value=5000.0)
    utilities = st.number_input("💡 Utilities", min_value=0.0, value=5000.0)
    entertainment = st.number_input("🎮 Entertainment", min_value=0.0, value=5000.0)
    others = st.number_input("📦 Other Expenses", min_value=0.0, value=5000.0)

    if st.button("Generate Budget Summary"):

        total = (
            rent
            + food
            + transport
            + utilities
            + entertainment
            + others
        )

        savings = income - total

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric("Income", f"₹ {income:,.2f}")

        with c2:
            st.metric("Expenses", f"₹ {total:,.2f}")

        with c3:
            st.metric("Savings", f"₹ {savings:,.2f}")

        budget = pd.DataFrame(
            {
                "Category": [
                    "Rent/EMI",
                    "Food",
                    "Transport",
                    "Utilities",
                    "Entertainment",
                    "Others"
                ],
                "Amount": [
                    rent,
                    food,
                    transport,
                    utilities,
                    entertainment,
                    others
                ]
            }
        )

        fig = px.pie(
            budget,
            names="Category",
            values="Amount",
            title="Expense Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

        rate = savings_rate(income, total)

        st.metric("Savings Rate", f"{rate:.2f}%")

        if rate >= 20:
            st.success("Excellent budgeting! 🎉")

        elif rate >= 10:
            st.info("Good budget. Try increasing savings.")

        else:
            st.warning("Your expenses are quite high.")

# ===================================================
# FINANCIAL HEALTH
# ===================================================

elif page == "❤️ Financial Health":

    st.header("❤️ Financial Health Dashboard")

    monthly_income = st.number_input(
        "Monthly Income",
        min_value=0.0,
        value=100000.0
    )

    monthly_expense = st.number_input(
        "Monthly Expenses",
        min_value=0.0,
        value=60000.0
    )

    debt_ratio = st.slider(
        "Debt Ratio (%)",
        0,
        100,
        30
    )

    emergency_months = st.slider(
        "Emergency Fund (Months)",
        0,
        12,
        6
    )

    if st.button("Analyze Financial Health"):

        save_rate = savings_rate(
            monthly_income,
            monthly_expense
        )

        score = health_score(
            save_rate,
            debt_ratio,
            emergency_months
        )

        st.subheader("Overall Financial Health")

        st.progress(score / 100)

        st.metric(
            "Health Score",
            f"{score}/100"
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Savings Rate",
                f"{save_rate:.2f}%"
            )

        with c2:
            st.metric(
                "Debt Ratio",
                f"{debt_ratio}%"
            )

        with c3:
            st.metric(
                "Emergency Fund",
                f"{emergency_months} Months"
            )

        st.divider()

        st.subheader("Recommendations")

        if save_rate < 20:
            st.warning("Increase your monthly savings.")

        else:
            st.success("Healthy savings rate.")

        if debt_ratio > 50:
            st.error("Debt ratio is high. Reduce liabilities.")

        else:
            st.success("Debt level is manageable.")

        if emergency_months < 6:
            st.warning("Build an emergency fund covering at least 6 months.")

        else:
            st.success("Emergency fund is adequate.")

        if score >= 80:
            st.balloons()
            st.success("Excellent financial health! Keep it up!")

        elif score >= 60:
            st.info("Good financial health with room for improvement.")

        elif score >= 40:
            st.warning("Average financial health. Focus on saving more.")

        else:
            st.error("Financial health needs significant improvement.")

st.divider()

st.caption("💸FinAgnetX")

st.caption(
    "Built using Streamlit • Gemini AI • Yahoo Finance • Plotly"
)

st.caption(
    "Created for Hackathon Demonstration Purposes"
)

