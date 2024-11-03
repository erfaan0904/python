def quick_sort(arr):
    # Base case: if the array is empty or has one element, it's already sorted
    if len(arr) <= 1:
        return arr
    
    # Choose a pivot element (we're choosing the last element here)
    pivot = arr[-1]
    
    # Arrays to hold elements less than and greater than the pivot
    left  = []  # Elements less than the pivot
    right = []  # Elements greater than the pivot

    # Iterate through all elements except the pivot
    for i in range(len(arr) - 1):
        if arr[i] < pivot:
            left.append(arr[i])  # Add to left if less than pivot
        else:
            right.append(arr[i])  # Add to right if greater than or equal to pivot
    
    # Recursively sort the left and right subarrays, then combine
    return quick_sort(left) + [pivot] + quick_sort(right)

#----------------------------------------------------------------------------------------------

array = []  # create an empty array
print("-" * 20)
print("Enter values for the array (type 'done' to stop): ")

while True:  # get array from user
    n = input("> ")
    if n == 'done':   #........Stop input when the user enters 'done'
        break
    try:
        n = int(n) #........Convert input to integer
        array.append(n) #...Add the integer to the array
    except ValueError:
        print("Invalid input, please enter a number or 'done' to stop.")
    # try except is using for control errors

#----------------------------------------------------------------------------------------------

unsorted_array = array
sorted_array = quick_sort(unsorted_array)
print("Sorted array:", sorted_array)
