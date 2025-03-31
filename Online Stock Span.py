class StockSpanner:

    def __init__(self):
        # Create 2 variables
        self.prices = []
        self.spans = []

    def next(self, price: int) -> int:
        # Create a default Span
        span = 1
        # now we will check from last and last -1 price and increase span
        while self.prices and self.prices[-1] < price:
            self.prices.pop()
            # Now the critical step is this
            # Now why we pop spans is because if we add new element then it should update span
            span = span + self.spans.pop()
        self.prices.append(price)
        self.spans.append(span)
        return span
