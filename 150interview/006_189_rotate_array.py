class Solution:
    def run(self) -> None:
        nums = [1, 2, 3, 4, 5, 6, 7]
        self.rotate(nums, 3)
        print(nums)

    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        if k == 0 or k == n:
            return
        cnt = 0
        for start in range(k):
            if cnt == n:
                break
            ptr = start
            prev = nums[(ptr - k) % n]
            while True:
                cnt += 1
                t = nums[ptr]
                nums[ptr] = prev
                prev = t
                ptr = (ptr + k) % n
                if ptr == start:
                    break


Solution().run()
