class Solution:
  def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
    max_consecutive_count = 0
    current_consecutive_count =0
    
    for num in nums:
        if num == 1:
            current_consecutive_count += 1
            max_consecutive_count = max(current_consecutive_count, max_consecutive_count)
        else:
            current_consecutive_count = 0
    return max_consecutive_count

