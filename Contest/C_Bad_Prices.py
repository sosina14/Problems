t = int(input())
results = []

for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    
    min_price = prices[-1]
    bad_days = 0

    for i in range(n - 2, -1, -1):
        if prices[i] > min_price:
            bad_days += 1
        min_price = min(min_price, prices[i])

    results.append(bad_days)

for res in results:
    print(res)
