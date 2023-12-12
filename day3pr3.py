def num_identical_pairs(nums):
    num_count = {}    
    good_pairs = 0    
    for num in nums:
        if num in num_count:
            good_pairs += num_count[num]
            num_count[num] += 1
        else:
            num_count[num] = 1
    
    return good_pairs
nums = [1, 2, 3, 1, 1, 3]
result = num_identical_pairs(nums)
print(result)
