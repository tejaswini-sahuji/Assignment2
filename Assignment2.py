# task 1 check the input value is even or odd
# Ask the user to input a number and convert the input string to an integer
n = int(input("Enter any number : "))
# Check if the number is divisible by 2 (i.e., no remainder)
if n % 2 == 0:
    # If divisible by 2, it is an even number
    print(n, "is even number")
else:
    # Otherwise, it is an odd number
    print(n, "is odd number")

# task 2 sum of int 1 to 50 using for loop
# Initialize a variable to hold the running total of the sum
sum = 0
# Loop from 1 to 50 (inclusive)
for i in range(1,51):
    # Add the current value of i to total_sum
    sum += i
# Print the final result    
print(sum)
