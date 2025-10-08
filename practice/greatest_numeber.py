class Solution:
    def largestElement(self, nums):
        if not nums:
            return None
        largest_element = nums[0]  
        for i in nums:
            if i > largest_element:
                largest_element = i
        return largest_element

nums = [10, 20, 4, 45, 90]
obj = Solution()
result = obj.largestElement(nums)
print("The largest element is:", result)
