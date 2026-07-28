# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 140,
    "MSFT": 420
}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    stock = input("\nEnter stock name (AAPL, TSLA, GOOG, MSFT) or 'done' to finish: ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(f"Investment in {stock}: ${investment}")

    else:
        print("Stock not found!")

print("\n===== PORTFOLIO SUMMARY =====")
print("Total Investment Value: $", total_investment)

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Total Investment Value: $" + str(total_investment))

print("Result saved in portfolio.txt")