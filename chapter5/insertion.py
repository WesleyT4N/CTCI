def clear(n, i, j):
    right_mask = ~(-1 << i)
    left_mask = (-1 << (j + 1))
    mask = left_mask | right_mask
    print(bin(right_mask))
    print(bin(left_mask))
    print(bin(n & mask))
    return n & mask

def insert(n, m, i, j):
    n = clear(n, i, j)
    m_shifted = m << i
    return n | m_shifted

print(bin(insert(9, 1, 1, 2)))