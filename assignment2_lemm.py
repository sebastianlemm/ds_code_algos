import pandas as pd

def MSSDAC(prices, low=0, high=None):
    if high is None:
        high = len(prices) - 1

    if low == high:  # Base case: one element
        return prices[low], low, high if prices[low] > 0 else (0, low, high)

    mid = (low + high) // 2
    max_left, left_low, left_high = MSSDAC(prices, low, mid)
    max_right, right_low, right_high = MSSDAC(prices, mid + 1, high)

    max_left_border_sum = left_border_sum = 0
    left_border_low = mid
    for i in range(mid, low - 1, -1):
        left_border_sum += prices[i]
        if left_border_sum > max_left_border_sum:
            max_left_border_sum = left_border_sum
            left_border_low = i

    max_right_border_sum = right_border_sum = 0
    right_border_high = mid + 1
    for i in range(mid + 1, high + 1):
        right_border_sum += prices[i]
        if right_border_sum > max_right_border_sum:
            max_right_border_sum = right_border_sum
            right_border_high = i

    max_cross = max_left_border_sum + max_right_border_sum
    if max_left >= max_right and max_left >= max_cross:
        return max_left, left_low, left_high
    elif max_right >= max_left and max_right >= max_cross:
        return max_right, right_low, right_high
    else:
        return max_cross, left_border_low, right_border_high

def calculate_potential_profit_and_dates(stock_data):
    # Calculate daily price changes
    price_changes = stock_data['close'].diff().iloc[1:].tolist()
    max_profit, buy_day, sell_day = MSSDAC(price_changes)
    return max_profit, stock_data.iloc[buy_day]['date'], stock_data.iloc[sell_day]['date']

def load_stock_data(filename):
    return pd.read_csv(filename)

def find_best_stock_and_dates(prices_filename, securities_filename):
    stock_df = load_stock_data(prices_filename)
    securities_df = load_stock_data(securities_filename)
    
    best_profit = 0
    best_stock = None
    best_dates = (None, None)

    for symbol in securities_df['Ticker symbol']:
        stock_data = stock_df[stock_df['symbol'] == symbol]
        if not stock_data.empty:
            profit, buy_date, sell_date = calculate_potential_profit_and_dates(stock_data)
            if profit > best_profit:
                best_profit = profit
                best_stock = symbol
                best_dates = (buy_date, sell_date)
    
    return best_stock, best_profit, best_dates

# Load stock data
stock_filename = 'prices-split-adjusted.csv'
securities_filename = 'securities.csv'

# Find the best stock to invest in along with the best dates to buy and sell
best_stock, best_profit, (buy_date, sell_date) = find_best_stock_and_dates(stock_filename, securities_filename)

if best_stock:
    print(f"The best stock to invest in is {best_stock} with a potential profit of ${best_profit:.2f}")
    print(f"Buy on: {buy_date}")
    print(f"Sell on: {sell_date}")
else:
    print("No profitable stock found.")
