class Solution:
    def run(self) -> None:
        num1 = [1, 2, 3, 0, 0, 0]
        self.merge(
            num1,
            3,
            [2, 5, 6],
            3,
        )
        print(num1)

    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p = n + m - 1
        p1 = m - 1
        p2 = n - 1
        while p >= 0:
            if p2 < 0 or (p1 >= 0 and nums1[p1] >= nums2[p2]):
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1


Solution().run()

# Simple and unoptimal
# def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
#     """
#     Do not return anything, modify nums1 in-place instead.
#     """
#     l = n + m
#     p1, p2 = 0, 0
#     while p2 < n:
#         if nums1[p1] == 0:
#             nums1[p1] = nums2[p2]
#             p1 += 1
#             p2 += 1
#         elif nums2[p2] < nums1[p1]:
#             for i in range(l - 1, p1, -1):
#                 nums1[i] = nums1[i - 1]
#             nums1[p1] = nums2[p2]
#             p1 += 1
#             p2 += 1
#         else:
#             p1 += 1
#         print(nums1)
