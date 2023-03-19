def factorial(n):
  global fact
  if n == 1:
    print("factorial(%d) before called %d! = %d" % (n, n, fact))
    print("The recursive termination condition is reached when n == 1")
    fact = 1
    print("factorial(%d) after called %d! = %d" % (n, n, fact))
    return fact
  else:
    print("factorial(%d) before called %d! = %d" % (n, n, fact))
    fact = n * factorial(n-1)
    print("factorial(%d) after called %d! = %d" % (n, n, fact))
    return fact

fact = 0
N = eval(input("Enter the factorial number: "))
print(N, " The factorial result is: ", factorial(N))