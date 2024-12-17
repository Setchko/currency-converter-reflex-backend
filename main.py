from fastapi import FastAPI

app = FastAPI()

# Tasas de cambio simuladas (1 USD = X)
# Estas tasas son de un día específico (16/12/2024), lo ideal es obtenerlas de un servicio externo.
rates = {
    "USD": 1.0,
    "EUR": 0.95,
    "JPY": 154.22,
    "GBP": 0.79,
    "AUD": 1.57,
    "CAD": 1.42,
    "CHF": 0.89,
    "CNY": 7.28,
    "SEK": 10.88,
    "NZD": 1.73,
    "COP": 4303.69,
}

@app.get("/convert")
async def convert(from_currency: str, to_currency: str, amount: float):
    """Convierte la cantidad de una moneda a otra."""
    if from_currency not in rates or to_currency not in rates:
        return {"error": "Moneda no soportada"}

    rate = rates[to_currency] / rates[from_currency]
    result = amount * rate
    return {"result": result}