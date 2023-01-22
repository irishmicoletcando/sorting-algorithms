def merge_sort(nums):
  if len(nums) > 1:
    # from beginning of nums array to middle part of nums array
    left_num_arr = nums[:len(nums)//2]
    # from middle part of nums array to end
    right_num_arr = nums[len(nums)//2:]

    # recursion
    merge_sort(left_num_arr)
    merge_sort(right_num_arr)

    # merge
    i = 0 # tracking elements in leftmost part of the array
    j = 0 # tracking elements in rightmost part of the array
    k = 0 # tracking elements in merged array

    while i < len(left_num_arr) and j < len(right_num_arr):
      # comparison
      if left_num_arr[i] < right_num_arr[j]:
        # saves value of left num arr in merged array
        nums[k] = left_num_arr[i]
        i += 1
        k += 1
      else:
        nums[k] = right_num_arr[j]
        j += 1
        k += 1

  # if len(nums) < 1, array is already sorted


nums = [53, 82, 9, 13, 98, 73, 18, 61, 16, 62]
merge_sort(nums)
print(nums)