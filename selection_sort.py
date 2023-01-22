def sort(nums):
  # loop until index 9
  for i in range(len(nums)- 1):
    minpos = i # holds the minimum position
    # loop for minpos
    for j in range(i, len(nums)):
      # value is less than minpos, change min position
      if nums[j] < nums[minpos]:
        minpos = j

    # swapping the index value i
    temp = nums[i]
    nums[i] = nums[minpos]
    nums[minpos] = temp

nums = [53, 82, 9, 13, 98, 73, 18, 61, 16, 62]