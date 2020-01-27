num, arr , ans= 5, [2,3,4,5,6], 1
num2, arr2, ans2= 5, [8,16,16,16,16], 8

# First we know that we have to find the max possible number, so we assume that max number is the min value in array
# If initial max number leaves reminders for any value from the array, we decrease max possible number by one until
# we find the true value
# We could start iterating from 1 and by increasing this value find our max number, but it is not cost-effective
# if values in the array are large
# Time complexity O(n*2) and Space complexity O(n)
def generalizedGCD(num, arr):
    # take the minimum value from array, this value the maximum possible value for the given array
    current = min(arr)
    # now loop over each possible value starting with the maximum and decreasing the number each iteration
    # The loop always terminates with return statement
    # because in case we reach number 1 in our range it guarantees that all reminders are zero
    for l in reversed(range(0, current+1)):
        # loop over the given array with list comprehension and output all reminders with modulo operator
        reminders = [arr[i] % l for i in range(num)]
        # check if all reminders are zero
        # if yes - that is our maximum number that divides all values in the array
        if max(reminders) == 0:
            return l


print(generalizedGCD(num, arr))
