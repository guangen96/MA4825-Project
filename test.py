# This program prints Hello, world!
import array

data = "b'[[\"Coffee\", \"Cold\", \"0%\"], [\"Tea\", \"Cold\", \"100%\"]]'"
data = data.split("\"")
print("Length", len(data))
arr = []

# Number of drinks
n = int((len(data)-1)/6)
print("Number of drinks", n)

for x in range(1, len(data), 2):
    print("Number of drinks: ", (len(data)-1)/6)
    arr1 = [data[x]]
    arr = arr + arr1
    print(arr)

for x in range(1, n):
    print("Serving Drink ", x, ":", arr[0+3*(x-1)])
    # Added timer delay for testing in app, please remove after added sequence for moving arm
    drink = arr[3*(x-1)]
    temp = arr[3*(x-1) + 1]
    sugar = arr[3*(x-1) + 2]
    print("Drink details:", drink, temp, sugar)
