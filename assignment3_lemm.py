def loadHousingData(filename):
    housing_data = []
    with open(filename, 'r') as file:
        next(file)  
        next(file)  
        for line in file:
            data = line.strip().split(',')
            metro_name = data[1]  
            recent_price = int(data[-1])  
            last_year_price = int(data[-13])  
            yearly_increase = recent_price - last_year_price
            housing_data.append((metro_name, recent_price, yearly_increase))
    return housing_data


def optimizeInvestments(housing_data, budget, increment):
    n = len(housing_data)
    W = budget // increment  
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    trace_back = [[[] for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, W + 1):
            name, cost, roi = housing_data[i - 1]
            cost = cost // increment  
            if cost <= w:
                if roi + dp[i - 1][w - cost] > dp[i - 1][w]:
                    dp[i][w] = roi + dp[i - 1][w - cost]
                    trace_back[i][w] = trace_back[i - 1][w - cost] + [name]
                else:
                    dp[i][w] = dp[i - 1][w]
                    trace_back[i][w] = trace_back[i - 1][w]
            else:
                dp[i][w] = dp[i - 1][w]
                trace_back[i][w] = trace_back[i - 1][w]

    return dp[n][W] * increment, [x for x in trace_back[n][W]]


if __name__ == "__main__":
    housing_file = "Metro.csv"
    budget = 1000000  
    increment = 1000  

    housing_data = loadHousingData(housing_file)
    estimated_profit, selected_cities = optimizeInvestments(housing_data, budget, increment)
    print("Estimated Profit:", estimated_profit)
    print("Selected Cities:", selected_cities)


## Estimated Profit: 102203000
## Selected Cities: ['"Yakima', '"Tyler', '"Joplin', '"Idaho Falls', '"Baraboo']