def find_missing_number(array):
    n=len(array)+1
    total_sum=n*(n+1)//2
    array_sum=sum(array)
    return total_sum-array_sum
array=[1,2,3,5,6,7]
missing_number=find_missing_number(array)
print("The Missing Number is:",missing_number)