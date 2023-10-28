def sum_of_elements(numbers, en = False):
    sum = 0
    for i in numbers:
        i=int(i)
        if i < 0 and en:
            continue
        else:
            sum += i
    return "Sum of elements is " + str(sum)


nums = input("Input space-seperated numbers: ")
numbers = nums.split()
answer = input("Do you want to exclude negative numbers?\n")
if answer.lower() == "yes":
    print(sum_of_elements(numbers, True))
elif answer.lower() == 'no':
    print(sum_of_elements(numbers))
else:
    input('Enter yes or no\n')