class Solution:
    def run(self) -> None:
        r = self.maxProfit([7, 1, 5, 3, 6, 4])
        print(r)

    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0

        profit = 0
        current_buy = prices[0]
        current_profit = 0

        for el in prices[1:]:
            if el - current_buy < current_profit:
                profit += current_profit
                current_profit = 0
                current_buy = el
            else:
                current_profit = el - current_buy

        profit += current_profit
        return profit


Solution().run()
