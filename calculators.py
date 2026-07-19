import math

# ---------------- EMI ---------------- #

def emi(principal, annual_rate, years):

    r = annual_rate / (12 * 100)
    n = years * 12

    if n <= 0:
        return 0, 0, 0

    if annual_rate == 0:
        emi_value = principal / n
        return round(emi_value, 2), round(principal, 2), 0

    emi_value = principal * r * ((1 + r) ** n) / (((1 + r) ** n) - 1)

    total = emi_value * n
    interest = total - principal

    return (
        round(emi_value, 2),
        round(total, 2),
        round(interest, 2)
    )


# ---------------- SIP ---------------- #

def sip(monthly, annual_rate, years):

    r = annual_rate / (12 * 100)
    n = years * 12

    invested = monthly * n

    if annual_rate == 0:
        return round(invested, 2), round(invested, 2)

    fv = monthly * ((((1 + r) ** n) - 1) * (1 + r)) / r

    return round(fv, 2), round(invested, 2)


# ---------------- SWP ---------------- #

def swp(initial, monthly_withdrawal, annual_rate, years):

    balance = initial
    r = annual_rate / 12 / 100
    months = years * 12

    for _ in range(months):

        balance *= (1 + r)
        balance -= monthly_withdrawal

        if balance <= 0:
            return 0

    return round(balance, 2)


# ---------------- Lumpsum ---------------- #

def lumpsum(principal, annual_rate, years):

    future = principal * ((1 + annual_rate / 100) ** years)

    return round(future, 2)


# ---------------- Retirement ---------------- #

def retirement(
    monthly_expense,
    current_age,
    retirement_age,
    life_expectancy,
    inflation,
    return_rate
):

    years = retirement_age - current_age

    if years < 0:
        return 0, 0

    future_expense = monthly_expense * ((1 + inflation / 100) ** years)

    retirement_years = life_expectancy - retirement_age

    if retirement_years <= 0:
        return round(future_expense, 2), 0

    # Simple corpus estimate
    corpus = future_expense * 12 * retirement_years

    return (
        round(future_expense, 2),
        round(corpus, 2)
    )


# ---------------- Emergency Fund ---------------- #

def emergency(monthly_expense):

    return round(monthly_expense * 6, 2)


# ---------------- Savings Rate ---------------- #

def savings_rate(income, expense):

    if income <= 0:
        return 0

    saved = income - expense

    rate = (saved / income) * 100

    return round(rate, 2)


# ---------------- Net Worth ---------------- #

def networth(assets, liabilities):

    return round(assets - liabilities, 2)


# ---------------- Financial Health ---------------- #

def health_score(savings, debt, emergency):

    score = 0

    if savings >= 20:
        score += 35
    elif savings >= 10:
        score += 20

    if debt < 30:
        score += 35
    elif debt < 50:
        score += 20

    if emergency >= 6:
        score += 30
    elif emergency >= 3:
        score += 15

    return score


# ---------------- CAGR ---------------- #

def cagr(begin, end, years):

    if begin <= 0 or end <= 0 or years <= 0:
        return 0

    return round((((end / begin) ** (1 / years)) - 1) * 100, 2)