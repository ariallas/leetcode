class Solution:
    def run(self) -> None:
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        self.removeDuplicates(nums)
        print(nums)

    def removeDuplicates(self, nums: list[int]) -> int:
        p = 1
        for i in range(1, len(nums)):
            el = nums[i]
            if el != nums[p - 1]:
                nums[p] = el
                p += 1
        return p


Solution().run()
