def merge_sort(nums):
  if len(nums) > 1:
    # from beginning of nums array to middle part of nums array
    left_num_arr = nums[:len(nums)//2]
    # from middle part of nums array to end
    right_num_arr = nums[len(nums)//2:]

    # recursion
    merge_sort(left_num_arr)
    merge_sort(right_num_arr)

  # if len(nums) < 1, array is already sorted


nums = [53, 82, 9, 13, 98, 73, 18, 61, 16, 62]
merge_sort(nums)
print(nums)