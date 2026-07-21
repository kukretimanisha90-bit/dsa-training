class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            width = right - left
            container_height = min(height[left], height[right])

            area = width * container_height
            max_water = max(max_water, area)

            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water
        