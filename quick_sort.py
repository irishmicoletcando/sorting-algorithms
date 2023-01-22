def quick_sort(nums, left, right):
  if left < right: # sub-array contains 2 elements
      partition_pos = partition(nums, left, right)
      quick_sort(nums, left, partition_pos -1)
      quick_sort(nums, partition_pos + 1, right)
  # if length of subarray = 1, do nothing


def partition(nums, left, right): # returns the index of pivot element after the first step of quick sort
  i = left # defines the left point of area to sort
  j = right - 1 # defines the right point of pivot
  pivot = nums[right]

  while i < j:
    # moves i to the right
    # moves j to the left
    while i < right and nums[i] < pivot:
      i += 1
    while j > left and nums[j] >= pivot:
      j -= 1

  # checks if elements crossed, if not, swap
    if i < j:
      nums[i], nums[j] = nums[j], nums[i]

  # if i and j crossed, swap elements
  if nums[i] > pivot:
    # right is the index that points to the pivot element so swap area at index i with the array at index right
    nums[i], nums[right] = nums[right], nums[i]
  # determines where to split i to call quick sort recursively
  return i


nums = [53, 82, 9, 13, 98, 73, 18, 61, 16, 62]
quick_sort(nums, 0, len(nums) - 1)
print(nums)