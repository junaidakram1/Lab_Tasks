def binary_search_recursive(arr, target, low, high):
    """
    Recursive binary search for a target in a sorted array.
    :param arr: List of integers (sorted).
    :param target: The value to search for.
    :param low: The lower index of the current search range.
    :param high: The upper index of the current search range.
    :return: Index of the target if found, else -1.
    """
    if low > high:  # Base case: Search range is empty
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:  # Target found
        return mid
    elif arr[mid] < target:  # Target in the right half
        return binary_search_recursive(arr, target, mid + 1, high)
    else:  # Target in the left half
        return binary_search_recursive(arr, target, low, mid - 1)


# Enhanced to find all occurrences of the target
def binary_search_all_indices(arr, target, low, high, indices):
    """
    Recursive binary search to find all indices of a target in a sorted array.
    :param arr: List of elements (sorted).
    :param target: The value to search for.
    :param low: The lower index of the current search range.
    :param high: The upper index of the current search range.
    :param indices: A list to collect indices where the target appears.
    :return: List of all indices of the target.
    """
    if low > high:
        return indices
    mid = (low + high) // 2
    if arr[mid] == target:
        indices.append(mid)
        binary_search_all_indices(arr, target, low, mid - 1, indices)
        binary_search_all_indices(arr, target, mid + 1, high, indices)
    elif arr[mid] < target:
        binary_search_all_indices(arr, target, mid + 1, high, indices)
    else:
        binary_search_all_indices(arr, target, low, mid - 1, indices)
    return sorted(indices)


# Test case to handle strings
def binary_search_recursive_strings(arr, target, low, high):
    """
    Recursive binary search for a target string in a sorted array of strings.
    :param arr: List of strings (sorted).
    :param target: The string to search for.
    :param low: The lower index of the current search range.
    :param high: The upper index of the current search range.
    :return: Index of the target if found, else -1.
    """
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive_strings(arr, target, mid + 1, high)
    else:
        return binary_search_recursive_strings(arr, target, low, mid - 1)
