class Solution:
    def run(self) -> None:
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        self.removeDuplicates(nums)
        print(nums)

    def removeDuplicates(self, nums: list[int]) -> int:
        p = 1
        cnt = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[p - 1]:
                nums[p] = nums[i]
                p += 1
                cnt = 1
            elif cnt == 1:
                nums[p] = nums[i]
                p += 1
                cnt += 1
        return p


Solution().run()
