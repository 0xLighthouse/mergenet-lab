def clamp(value, low, high):
    if low > high:
        raise ValueError("invalid bounds")
    return min(high, max(low, value))
