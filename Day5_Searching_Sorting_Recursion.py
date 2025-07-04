#Merge Sort
def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]

  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysortedlist = mergeSort(mylist)
print("Sorted array:", mysortedlist)



#****************LINEAR SEARCH**********************
def linear_Search(arr,targetVal):
    for i in range (len(arr)):
        if arr[i]==targetVal:
            return i
    return -1        

arr=[1,6,5,4,3]
targetVal=4

ans=  linear_Search(arr,targetVal)

if ans!=-1:
    print ("Found at index: ", ans)
else:
    print("Not found")    



#******************BINARY SEARCH**************
def binary_search_with_original_index(arr, target):
    """
    Performs binary search on an unsorted array while preserving original indices.
    Returns the original index of the target if found, otherwise -1.
    """
    # Step 1: Create list of tuples containing (value, original_index)
    indexed_arr = [(value, idx) for idx, value in enumerate(arr)]
    
    # Step 2: Sort the array based on values
    indexed_arr.sort()
    
    # Step 3: Perform binary search
    left, right = 0, len(indexed_arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_value, original_index = indexed_arr[mid]  # Unpack the tuple
        
        if mid_value == target:
            return original_index  # Return the original index
        elif mid_value < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Target not found

if __name__ == "__main__":
    arr = [1, 6, 5, 4, 3]  # Original unsorted array
    target = 4
    
    result = binary_search_with_original_index(arr, target)
    
    if result != -1:
        print(f"Target {target} found at original index: {result}")
    else:
        print(f"Target {target} not found in the array")


# #***************Bubble Sort******************
mylist=[1,4,6,9,2,7]
n=len(mylist)
for i in range(n-1):
    for j in range(n-i-1):
        if(mylist[j]>mylist[j+1]):
            mylist[j], mylist[j+1]=mylist[j+1], mylist[j]
print(mylist)

 #*************Quick Sort***************
def quicksort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        pivot_index = partition(arr, low, high)
        quicksort(arr, low, pivot_index - 1)
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[low]  # First element as pivot
    i = low + 1       # Pointer for elements <= pivot

    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]  # Swap
            i += 1

    # Place pivot in its correct position
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1  # Return pivot index

# Example Usage
arr = [10, 80, 30, 90, 40, 50, 70]
quicksort(arr)
print("Sorted Array:", arr)  # Output: [10, 30, 40, 50, 70, 80, 90]


# Merge Intervals
def merge(intervals):
    if not intervals:
        return []  
    # Sort intervals based on start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
      #  print(last)
        if current[0] <= last[1]:  # Overlapping intervals
            last[1] = max(last[1], current[1])  # Merge
        else:
            merged.append(current)  # Non-overlapping
    
    return merged

print(merge([[1,3],[2,6],[8,10],[15,18]])) # Output: [[1,6],[8,10],[15,18]]
print(merge([[1,4],[4,5]]))                # Output: [[1,5]]    
print(merge([[5,4],[0,5]]))                # Output: [[0,4]]
print(merge([]))                           # Output: []


 # Search in Rotated Sorted Array
def search(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

nums=[5,6,7,8,9,10,2,3,4]
target=2
ans=search(nums, target)
print(ans)