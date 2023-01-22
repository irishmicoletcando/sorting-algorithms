def insertion_sort(nums):
  # loop from 1 to 9
  for i in range(1, len(nums)):
    # inner loop that starts at the index of outer loop and iterates to check if swapping is needed
    j = i
    # swapping condition
    # left is bigger than current element
    while nums[j - 1] > nums[j]: 
      # swapping
      # looks for entry in index j and puts in index j - 1 and simulataneously looks for entry in j - 1 and puts in index j
      nums[j - 1], nums[j] = nums[j], nums[j -  1]
      # going further to the left after swapping
      j -= 1

nums = [53, 82, 9, 13, 98, 73, 18, 61, 16, 62]
insertion_sort(nums)
print(nums)