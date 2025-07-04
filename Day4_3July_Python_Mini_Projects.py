#Guess the Number
import random
import string
randomno= random.randint(1,101)
print("************START GAME***************")
game=True
while game: 
    number = (input ("\nGuess the number or Quit(Q/q) the game: "))
    if (number.isnumeric()==True or number.isalpha()==True):
        if(number=="Q" or number=="q"):
            print("Quit the game...")
            #game=False
            break
        number=int(number)
        if (number==randomno):
            print("You guessed right...")
            break
        elif (number<randomno):
            print("You guessed wrong. Make a bigger guess...")  
        else:
            print("Your guessed wrong. Make lesser guess... ")
    else:
        print("Please enter valid number.")                  
print("**************END GAME**************")        



# Random Password Generator
char_string=string.digits + string.punctuation + string.ascii_letters
while True:
    password=[]
    choice=input("Want to generate password? (y/n)")
    if (choice=="y" or choice=="Y"):
        for i in range(1, 9, 1):
            random_char= random.choice(char_string)
            password.append(random_char)
        pass_string="".join(password)
        print(pass_string)
    elif(choice=='n' or choice=='N'):
        print("Bye Bye..")
        break
print("My password is: ", pass_string)


#***********LEETCODE PROBLEM 1*********** 
# Given an array of integers 'nums' and an integer 'mylist', return indices of the two numbers such that they add up to target.
def check(mylist, target):
    list_lenght=len(mylist)
    for i in range(0, list_lenght,1):
        for j in range(0, i+1, 1):
            if (i!=j):
                if (mylist[i]+mylist[j])==target:
                    return (i,j)

mylist=[1,2,3,4,5,6,7,8,9]
target=5
ans=check(mylist, target)
print(ans)



#Bubble Sort
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(n-1):
  for j in range(n-i-1):
    if mylist[j] > mylist[j+1]:
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

print(mylist)



#Linear Search
def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal:
      return i
  return -1

mylist = [3, 7, 2, 9, 5, 1, 8, 4, 6]
x = 4

result = linearSearch(mylist, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")



#Binary Search
def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid

    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1

mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 11

result = binarySearch(mylist, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")



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



#Quick Sort
def partition(array, low, high):
    pivot = array[low]  # Pivot is now the first element
    i = low + 1         # Pointer for elements <= pivot

    for j in range(low + 1, high + 1):
        if array[j] <= pivot:
            array[i], array[j] = array[j], array[i]
            i += 1

    # Move pivot to its correct position
    array[low], array[i - 1] = array[i - 1], array[low]
    return i - 1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)

# Test the code
mylist = [64, 34, 25, 5, 22, 11, 90, 12]
quicksort(mylist)
print(mylist)  # Output: [5, 11, 12, 22, 25, 34, 64, 90]


