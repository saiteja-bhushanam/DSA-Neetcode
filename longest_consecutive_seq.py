def longest_consecutive(nums) -> int:
    max_count = 0
    for i in range(len(nums)):
        count = 1
        for j in range(i + 1, len(nums)):
            if nums[j] == nums[i] + 1:
                count += 1
                nums[i] += 1
            max_count = max(count, max_count)
    return max_count
            
    
    
    
    
arr = [2,20,4,10,3,4,5]
print(longest_consecutive(arr))
