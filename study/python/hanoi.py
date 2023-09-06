def hanoi(number_, from_, to_, via_):
    if number_==1:
        print(from_,to_)
    else:
        hanoi(number_-1, from_, via_, to_)
        print(from_,to_)
        hanoi(number_-1, via_, to_, from_)

n=int(input())
print(2**n-1)
hanoi(n, 1, 3, 2)