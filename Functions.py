



def armstrong_number(num):
    sum = 0
    temp = num
    while temp > 0:
       digit = temp % 10
       sum += digit ** 3
       temp //= 10

    if num == sum:
       return "Armstrong number"
    else:
       return "not an Armstrong number"


def divisible(num):
    if num % 5==0:
        return "divisible"
    else:
        return "not divisible"


def Largest(a,b,c):
    if a>b:
        return a
    elif b>c:
        return b
    elif c>a:
        return c


def evenorodd(x):
    if x % 2 == 0:
        return "even"
    else:
        return "odd"


if __name__=="__main__":


    # armstrong Number
    print("armstrong or not")
    num = int(input("Enter the Number"))
    result = armstrong_number(num)
    print(result)

    # divisible or not
    print("divisible by 5 or not")
    num = int(input("Enter the Number"))
    result = divisible(num)
    print(result)

    # largest
    print("Largest of 3 numbers")
    x = int(input("Enter num 1 : "))
    y = int(input("Enter num 2 : "))
    z = int(input("Enter num 3 : "))
    result = Largest(x,y,z)
    print(result)

    # odd or even
    print("odd or even")
    x = int(input("Enter the Number"))
    result = evenorodd(x)
    print(result)


