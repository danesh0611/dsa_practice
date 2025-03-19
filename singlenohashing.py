class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count_map = {} 


        for num in nums:
            count_map[num] = count_map.get(num, 0) + 1

        # Second pass: Find the unique number (O(n))
        for num in count_map:
            if count_map[num] == 1:
                return num
    
        return -1
