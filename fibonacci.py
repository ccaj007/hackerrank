cube = lambda x: x**3 # complete the lambda function

# def fibonacci(n):
#     # return a list of fibonacci numbers
#     if n in {0, 1}:
#         return n
#     return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci(n):
    if n<2:
        return range(n)
    init = [0,1]
    for i in range(0,n-2):
        add =init[i+1]+init[i]
        init.append(add)
    return(init)

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
#    print(fibonacci(n))
