def insertion_sort(arr):
    """
    Sorts a list in ascending order using the insertion sort algorithm.
    Args:
        arr (list): The list to be sorted.
    Returns:
        list: The sorted list.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Example usage:
if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]
    print("Original:", data)
    sorted_data = insertion_sort(data)
    print("Sorted:", sorted_data)