def bubble_sort(nums):
  # outer loop
  for i in range(len(nums) - 1, 0, -1):
    # inner loop
    for j in range(i):
      if nums[j] > nums[j+1]:
        temp = nums[j]
        nums[j] = nums[j+1]
        nums[j+1] = temp


nums = [53, 82, 9, 13, 98, 73, 18, 61, 16, 62]
bubble_sort(nums)
print(nums)