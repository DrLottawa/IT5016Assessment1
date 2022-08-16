#Hello, hello! So I decided to try and go replicate a merge-sort sorting algorithm that works by dividing an unsorted list of values to its smallest parts, swapping around these values
#so that they are ordered properly and then taking these sorted arrays and merging them together until the full list is returned sorted. This merge sort is replicated from this link
#and annotated soley from my understanding and interpretation. https://realpython.com/sorting-algorithms-python/#the-merge-sort-algorithm-in-python


#Here I'm importing the random module included in python's libraries. This will be used to generate a random, unsorted list of values for us to sort using the algorithm
import random

#Said list is initialised here as an empty array.
sortinglist = []

#These two lines of code begin a for loop which iterates the code in line 18 according to the range and its specified number. In this case I have set the range to 75. The for loop
#is capable of taking that range of numbers and using at as an iterater or number of times to loop.
for i in range(75,1,-1):
    #This line of code here calls on the random module we initated earlier to call its randint method. This method will generate a pseudo-random number between the values I indicate
    #in parameters. In this case the minimum number for it to generate is 1 and the maximum number is 1000. Once this number is generated it is appended to the sorting list and the
    #for loop will move on to the next interation to generate another number to append to the sortinglist. This will continue until the loop has been run the specified number of times,
    #in this case 75 times.
    sortinglist.append(i)


#Here I define a function that takes an unsorted array as a parameter. This will be called recursively by itself in order to divide the arrays fed into it for the algorithm as
#will be explained later
def merge_sort(array):
    #This array will continuously split the arrays fed into it in half. If ever it gets to the point that it cannot be split in half any further (ie only one or none elements are in it)
    #this if statement will simply return the array that was fed in thus ending the recursions. In laymans terms, this is the exit condition.
    if len(array) < 2:

        return array

    #Simple calculation for the mid point of whatever array has been fed in. It will take the number of elements in the array and divide it by 2, flooring the result.
    midpoint = len(array) // 2

    #Here is where some of the magic happens. This return will continuously self call the merge-sort function its in with the left input array taking the first half of the split array.
    #From here we will jump back to line 23 with the now halved set of values and repeat the process. This will continuously call until the condition specifed on line 26 becomes true
    #or to put, it is 1 or less and thus cannot be halved any longer. at this point the array itself is returned and the other half of this now tiny array can now be inserted into the
    #right parameter. With these tiny arrays we can now run the merge function which is able to take these two arrays and sort their values accordingly. This process is repeated until
    #each split array is compared and sorted against each other.
    return merge(
        #This left parameter along with the right parameter recall the merge_sort function feeding in the parameters of everything left of the midpoint of the array in the left parameter
        #and feeding everything to the right of the midpoint, including the midpoint itself as the right array.
        left=merge_sort(array[:midpoint]),

        right=merge_sort(array[midpoint:]))


#Here we start defining the merge function. This function will get called as the return for the merge_sort function and is properly hit when both the left and right parameters return an
#array, in this case when the merge sort has stopped calling itself and starts returning the array it was fed
def merge(left, right):
    #This along with the if comparison below check to see if any of the arrays fed in are empty. If so there is no array to compare and sort itself against and so it is safe to just
    #return the array that was passed in
    if len(left) == 0:
        return right

    if len(right) == 0:
        return left
    
    #Here we create an array called result. This will be returned at the end of the function. This exists to hold the sorted values and to be used to check if every value has been
    #sorted later on.
    result = []
    #Here we declare two variables equal to each other which both equal 0. These will be used to access the index of the currently being accessed value of each array which will be
    #expanded upon later when we look at how the function compares values and 'saves' already compared values.
    index_left = index_right = 0

    #Here we have a while loop that gets the number of items in the result array and loops everything within it for as long as the number of items in the both the left and the right
    #arrays is larger than the number of items in the result array. This means that if the number of items in the result array is equal to the number in the two arrays each item in
    #the two arrays has already been processed and no more comparisons need to be made. The function is ready to return the result array.
    while len(result) < len(left) + len(right):
        #So this is where the sorting magic happens. What this is is a comparison that checks if the item at the index of our index_left variable of the left array is lesser or equal
        #than the item at the index of the index_right variable of the right array. When either the if or else is finished processing the index variable of the array that had the
        #higher value in the comparison will be incremented by 1. This way any further comparisons will use the next value of that array as the previous value has been processed and
        #added to the result array already.
        if left[index_left] <= right[index_right]:
            #Here the lowest value has been found and so will be appended to the result array. Appending a value to an array will always put it at the end of the array and so anything
            #being appended will be higher in value than the items to its left. In other terms the earlier something is appended the smaller its value will be thus having the result be
            #sorted from lowest value at the left to highest to the right.
            result.append(left[index_left])
            #and then once we have appended that value we increment the index variable of that array by one so that if we come back around to compare the arrays again we are comparing
            #the next item in our respective array and we dont reprocess items already sorted into the result array.
            index_left += 1
        else:
            #See line 74
            result.append(right[index_right])
            #See line 78
            index_right += 1
        
        #These two if statements serve to check if the index variable of the respective array is equal to the arrays length or number of items. This is for the case of the left or right
        #array having differing amounts of items within them. One may have an extra item over the other which would cause the comparison at line 73 to fail as the index is now out of bounds.
        #To avoid this we run these statements at the end of each comparison to make sure that if any of these indexs hit their limit we get the other respective array and append its last
        #item to the result array as this is the last unsorted item which is guaranteed to be the largest. Now the result array is sorted and ready to be returned.
        if index_right == len(right):
            #this appends the last item of the other respective array as explained in line 87
            result += left[index_left:]
            break
        #see line 87
        if index_left == len(left):
            result += right[index_right:]
            break

    #And finally by the time we hit this return the result array has been fully populated and sorted. We return the array where it can either be merged with another array or fully returned
    #depending on if the entire original array generated at the begining of this process has been sorted or not.
    return result

#Finally, this is the statement that starts it all. Here we call the print method and feed the merge_sort method with the sortinglist as its parameter. This means what the merge_sort
#returns is what will be printed to the console for the user to see. This merge_sort will the result of all of the deeper calls and processes finishing their calculation and returning
#a sorted list. Thanks for reading this far!
print(merge_sort(sortinglist))