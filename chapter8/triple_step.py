def triple_step(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return triple_step(n-1) + triple_step(n-2) 

def triple_step_memoized(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    step_n_minus_1 = 1
    step_n_minus_2 = 0
    step_n_minus_3 = 0
    step_n = step_n_minus_1 + step_n_minus_2 + step_n_minus_3
    for i in range(1, n+1):
        step_n = step_n_minus_1 + step_n_minus_2 + step_n_minus_3
        step_n_minus_3 = step_n_minus_2
        step_n_minus_2 = step_n_minus_1
        step_n_minus_1 = step_n
    return step_n