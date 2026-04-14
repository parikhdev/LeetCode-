class StockSpanner:
    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and self.stack[-1][0] <= price:
            span += self.stack.pop()[1]
        self.stack.append((price, span))
        return span

spanner = StockSpanner()
prices = [100, 80, 60, 70, 60, 75, 85]
results = [None]

for price in prices:
    results.append(spanner.next(price))

print(results)