def sum_path(root, target, sum, running_sums):
    if root is None:
        return 0
    running_sum += root.value
    sum = running_sum - target_sum
    if sum not in running_sums:
        total_paths = 0
    else:
        total_paths = running_sums[sum]
    if running_sum == target:
        total_paths += 1
    if running_sum not in running_sums:
        running_sums[running_sum] = 1
    else:
        running_sums[running_sum] += 1
    total_paths += sum_path(root.left, target, sum, paths)
    total_paths += sum_path(root.right, target, sum, paths)
    running_sum[running_sum] -= 1
    if running_sum[running_sum] == 0:
        del running_sum[running_sum]
    return total_paths


def paths_with_sum(root, target):
    if root is None:
        return 0
    runningSums = {}
    total_paths = sum_path(root, target, 0, running_sums)

def sub_arrays_with_sum(arr, target):
    running_sum = 0
    running_sums = {}
    total_paths = 0
    for i in range(0, len(arr)):
        running_sum += arr[i]
        if running_sum == target:
            total_paths += 1
        if (running_sum - target) in running_sums:
            total_paths += running_sums[running_sum - target]

        if running_sum in running_sums:
            running_sums[running_sum] += 1
        else:
            running_sums[running_sum] = 1
    return total_paths

print(str(sub_arrays_with_sum([1,2,3, 5], 5)))