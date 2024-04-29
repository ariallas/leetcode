class Solution:
    def run(self) -> None:
        nums = [0, 1, 2, 2, 3, 0, 4, 2]
        self.removeElement(nums, 2)
        print(nums)

    def removeElement(self, nums: list[int], val: int) -> int:
        p = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[p] = nums[i]
                p += 1
        return p


Solution().run()
