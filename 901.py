class StockSpanner:

    def __init__(self):
        self.mono = []

    def next(self, price: int) -> int:
        # time: O(n), space: O(n)
        cnt = 1
        while self.mono and price >= self.mono[-1][0]:
            cnt += self.mono.pop()[1]
        self.mono.append([price, cnt])
        return cnt


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)