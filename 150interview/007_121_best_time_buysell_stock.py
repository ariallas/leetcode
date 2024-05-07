class Solution:
    def run(self) -> None:
        r = self.maxProfit([7, 1, 5, 3, 6, 4])
        print(r)

    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0

        current_min = prices[0]
        best_profit = 0

        for el in prices[1:]:
            best_profit = max(best_profit, el - current_min)
            if el < current_min:
                current_min = el

        return best_profit


Solution().run()
