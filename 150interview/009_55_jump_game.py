class Solution:
    def run(self) -> None:
        r = self.canJump([3, 2, 1, 0, 4])
        print(r)

    def canJump(self, nums: list[int]) -> bool:
        jumps_left = 1
        n = len(nums)
        for i, max_jump in enumerate(nums):
            jumps_left -= 1
            jumps_left = max(jumps_left, max_jump)
            if jumps_left >= n - i - 1:
                return True
            if jumps_left == 0:
                return False

        raise Exception()


Solution().run()
