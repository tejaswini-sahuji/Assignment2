# task 1 check the input value is even or odd
n = int(input("Enter any number : "))
if n % 2 == 0:
    print(n, "is even number")
else:
    print(n, "is odd number")

# task 2 sum of int 1 to 50 using for loop
sum = 0
for i in range(1,51):
    sum += i
print(sum)