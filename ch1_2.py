#ch1_2.py
def factorial(n):
  "Calculate the factorial of n, where n must be an integer."
  if n == 1:
    return 1
  else:
    return (n * factorial(n - 1))

N = eval(input("Please enter an integer:"))
print(N, "The factorial result is = ", factorial(N))

times = 1000 * 1000 * 1000 * 1000 * 10 # The number of sequences that the computer can process per second.
day_secs = 60 * 60 * 24 # The number of seconds in a day.
year_secs = 365 * day_secs # The number of seconds in a year.
combinations = factorial(N) # Combination method
years = combinations / (year_secs * times)
print("The number %d of data points, the number of combinations in the sequence = %d.", N, combinations)
print("How many years %d are needed to obtain the result?", years)