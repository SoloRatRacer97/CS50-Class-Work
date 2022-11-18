










credit = list(input("Number: "))
# first we reverse the list
copy_credit = credit[::-1]
# Going to loop through all the numbers by 2, starting at 1
every_other_sum = copy_credit[1::2]
working_list = [int(x) for x in every_other_sum]
# Going to loop through all the numbers by 2, starting at 0
first_sum = copy_credit[0::2]
working_list2 = [int(x) for x in first_sum]

doubled_values = [x * 2 for x in working_list]
print(doubled_values)
Sum = sum(doubled_values)
Sum2 = sum(working_list2)
print(Sum)

