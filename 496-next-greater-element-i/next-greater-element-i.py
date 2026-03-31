class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        next_greater = {}

        # Build next greater mapping for nums2
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        # Remaining elements have no greater element
        while stack:
            next_greater[stack.pop()] = -1

        # Build result for nums1
        result = []
        for num in nums1:
            result.append(next_greater[num])

        return result
        