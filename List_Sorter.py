#=================================== List Sorter ========================
print("=================================== List Sorter ========================")

Lists= [1, 2, 89, 4,7 ,5 , 10,8, 6, 11 ]
print("The originl list is ", Lists)
sum=0
for i in Lists:
    sum+= i
average= sum/len(Lists)

Lists.sort()
print("The order version acsending ",Lists)
print("The smallest element in the list is ", Lists[0])
print("The biggest element in this list is ", Lists[-1])
print(" The sum of all the numbers in this list is ", sum, " and the average f all the numbers in this list is ", average)