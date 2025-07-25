class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreaterMap = {}

        # Build the map using Monotonic Stack
        for num in nums2:
            while stack and stack[-1] < num:
                nextGreaterMap[stack.pop()] = num
            stack.append(num)

        # Build the result
        result = []
        for num in nums1:
            result.append(nextGreaterMap.get(num, -1))

        return result
