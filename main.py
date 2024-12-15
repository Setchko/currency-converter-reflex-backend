from fastapi import FastAPI

app = FastAPI()

# Tasas de cambio ficticias (1 USD = X)
rates = {
    "USD": 1.0,
    "EUR": 0.85,
    "JPY": 110.66,
    "GBP": 0.73,
    "AUD": 1.35,
    "CAD": 1.27,
    "CHF": 0.92,
    "CNY": 6.47,
    "SEK": 8.62,
    "NZD": 1.44,
}

@app.get("/convert")
async def convert(from_currency: str, to_currency: str, amount: float):
    """Convierte la cantidad de una moneda a otra."""
    if from_currency not in rates or to_currency not in rates:
        return {"error": "Moneda no soportada"}

    rate = rates[to_currency] / rates[from_currency]
    result = amount * rate
    return {"result": result}