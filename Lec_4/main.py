def EvenOdd(arr):
    Even = [] 
    Odd = []

    for i in arr :
        if (i % 2 == 0) :
            Even.append(i)
        else:
            Odd.append(i)
    return f"Even numbers: {Even} \nOdd numbers: {Odd}" 

print(EvenOdd([1,2,3,4,5]))