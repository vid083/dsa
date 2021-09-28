#sum of elements in a array
'''
def get_sum(arr):
    sum = 0
    for i in len(arr):
        sum = sum + arr[i]
    return sum

arr = [1,2,3,4]
print(get_sum(arr))   ----> not excuted

'''
# inbuilt sum funtion to add numbers in list, arrays, tuples

arr = [1,2,3,4]

sum = sum(arr)
print(sum)