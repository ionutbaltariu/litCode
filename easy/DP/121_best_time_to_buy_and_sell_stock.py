from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        count = len(prices)

        if count in [0, 1]:
            return 0

        max_profit = 0
        left_ptr = 0
        right_ptr = 0

        while right_ptr < count:
            if prices[right_ptr] < prices[left_ptr]:
                # if we find a value that is lesser than the current pointer, it means that we can just
                # start our next max profit search from that pointer
                # since we would only have greater values that would generate smaller profits until that ptr
                left_ptr = right_ptr
                right_ptr += 1
                continue

            profit = prices[right_ptr] - prices[left_ptr]

            if max_profit < profit:
                max_profit = profit

            right_ptr += 1

        return max_profit


if __name__ == "__main__":
    print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
