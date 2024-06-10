# numbers =[5,3,2,4, 56,94,76,4,23,0,756,8]
# numbers=[1,2,3,4,5]
numbers=[2]

value = numbers[0]
second_num = numbers[0]
for number in numbers[1:]:
    if number>value:
        value=number
for num in numbers[1:] :     
    if num>second_num and num!=value:
        second_num = num
print(value)
print(second_num)

