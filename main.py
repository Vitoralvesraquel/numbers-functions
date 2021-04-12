def perfect_power(n: int):
    """A perfect power is a positive integer n of the form m^k, where m>1 is a positive integer and k>=2.
    This function returns [m, K]."""
    k = 2
    max_k = round(n ** (1/2))
    while True:
        m = round(n ** (1/k))
        if m ** k == n:
            return [m, k]
        elif k > max_k:
            return None
        else:
            k += 1


def distinct_partition(n: int):
    """Returns the number of partitions of n in at least 2 distinct parts."""
    p_list = [1] + [0]*n
    for i in range(1, n+1):
        for j in reversed(range(i, n+1)):
            p_list[j] += p_list[j - i]
    return p_list[n] - 1
