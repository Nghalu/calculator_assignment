# Calculator Assignment
#Creating a simple Python program that asks the user to input two numbers and a mathematical operation (addition, subtraction, multiplication, or division).
first_num = float(input("Enter the first number: "))
second_num = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
sum_result = first_num + second_num
difference_result = first_num - second_num
product_result = first_num * second_num
quotient_result = first_num / second_num
# Displaying the results based on the operation chosen by the user.
print("first number:", first_num)
print("second number:", second_num)
print("sum_result:", sum_result)
print("difference_result:", difference_result)
print("product_result:", product_result)
print("quotient_result:", quotient_result)