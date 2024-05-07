class Solution:
    def run(self) -> None:
        r = self.jump([2, 3, 1, 1, 4])
        print(r)

    def jump(self, nums: list[int]) -> int:
        min_jumps = [99999] * len(nums)
        min_jumps[0] = 0

        for i, max_jump in enumerate(nums):
            num_jumps = min_jumps[i]
            for j in range(i + 1, min(i + max_jump + 1, len(nums))):
                min_jumps[j] = min(min_jumps[j], num_jumps + 1)

        return min_jumps[-1]


Solution().run()
