def kadane(arr: list[int]) -> tuple[int, int, int]:
    max_sum = arr[0]
    curr_sum = arr[0]
    start = 0
    best_l = 0
    best_r = 0
    for i in range(1, len(arr)):
        if curr_sum + arr[i] < arr[i]:
            curr_sum = arr[i]
            start = i
        else:
            curr_sum += arr[i]
        if curr_sum > max_sum:
            max_sum = curr_sum
            best_l = start
            best_r = i
    return max_sum, best_l, best_r

def max_sum_submatrix(mat: list[list[int]]):
    if not mat or not mat[0]:
        return 0, (None, None, None, None)
    R, C = len(mat), len(mat[0])
    best_sum = None
    best_rect = (0, 0, 0, 0)  

    for left in range(C):
        temp = [0] * R
        for right in range(left, C):
            for r in range(R):
                temp[r] += mat[r][right]

            curr_sum, top, bottom = kadane(temp)

            if best_sum is None or curr_sum > best_sum:
                best_sum = curr_sum
                best_rect = (top, left, bottom, right)

    return best_sum, best_rect