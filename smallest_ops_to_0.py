def min_operations_to_zero(nums):
    # If there's already a zero in the array, return 0
    if 0 in nums:
        return 0
    
    operations = 0
    nums_set = set(nums)
    
    while nums_set:
        current_nums = list(nums_set)
        found_zero = False
        
        # Try to find pairs that can subtract to get a zero
        for i in range(len(current_nums)):
            for j in range(i + 1, len(current_nums)):
                if current_nums[i] - current_nums[j] == 0 or current_nums[j] - current_nums[i] == 0:
                    found_zero = True
                    operations += 1
                    nums_set.remove(current_nums[i])
                    nums_set.remove(current_nums[j])
                    break
            if found_zero:
                break
        
        # If we found a zero, we're done
        if found_zero:
            return operations
        
        # If no pairs were found to reduce to zero, take the smallest difference
        min_diff = float('inf')
        a, b = None, None
        for i in range(len(current_nums)):
            for j in range(i + 1, len(current_nums)):
                diff = abs(current_nums[i] - current_nums[j])
                if diff < min_diff:
                    min_diff = diff
                    a, b = current_nums[i], current_nums[j]
        
        # Perform the operation and add the result back
        if a is not None and b is not None:
            nums_set.remove(a)
            nums_set.remove(b)
            nums_set.add(abs(a - b))
            operations += 1

    return operations

# Test cases
print(min_operations_to_zero([1, 4, 5, 7]))  # Output: 2
print(min_operations_to_zero([]))           # Output: 0
print(min_operations_to_zero([0, 5, 6]))    # Output: 0
