#ch1_1.py
def factorial(n):
  "Calculate the factorial of n, where n must be an integer."
  if n == 1:
    return 1
  else:
    return (n * factorial(n - 1))
N = eval(input("Please enter an integer:"))
print(N, "The factorial result is = ", factorial(N))