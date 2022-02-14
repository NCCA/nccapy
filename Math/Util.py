

def clamp(num, low, high):
    "clamp to range min and max will throw ValueError is low>=high"
    if low > high or low == high :
        raise ValueError
    return max(min(num, high), low)
        