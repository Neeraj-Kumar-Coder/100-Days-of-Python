def max(args):
    """Returns the maximum element among the provided values"""
    max_element = args[0]
    for element in args:
        max_element = element if element > max_element else max_element
    return max_element


def min(args):
    """Returns the minimum element among the provided values"""
    min_element = args[0]
    for element in args:
        min_element = element if element < min_element else min_element
    return min_element


if __name__ == "__main__":
    print("This will be executed if this module is run directly as main")
