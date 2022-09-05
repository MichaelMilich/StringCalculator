# This is a sample Python script.
import re


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def check_letters(input):
    return re.search("[a-zA-Z]", input)


def turn_into_numbers_list(input):
    return re.split("[*+-/]", input)


def turn_into_operators_list(input):
    return re.findall("[*+-/]", input)


def calculate_in_order(numbers, operators):
    while operators.count("*") + operators.count("/") > 0:
        for idx, operator in enumerate(operators):
            if operator == "*":
                numbers[idx] = float(numbers[idx]) * float(numbers[idx + 1])
                del numbers[idx + 1]
                del operators[idx]
                break
            elif operator =="/":
                numbers[idx] = float(numbers[idx]) / float(numbers[idx + 1])
                del numbers[idx + 1]
                del operators[idx]
                break
    while operators.count("+") + operators.count("-") > 0:
        for idx, operator in enumerate(operators):
            if operator == "+":
                numbers[idx] = float(numbers[idx]) + float(numbers[idx + 1])
                del numbers[idx + 1]
                del operators[idx]
                break
            elif operator =="-":
                numbers[idx] = float(numbers[idx]) - float(numbers[idx + 1])
                del numbers[idx + 1]
                del operators[idx]
                break
    return numbers[0]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

user_input = input("Welcome to calculator\n "
                   "To escape please write 'esc' \n"
                   "Please write what you want to calculate\n")

while user_input != "esc":
    if check_letters(user_input):
        print("NO LETTERS!")
    else:
        print("Calculating...")
        numbers = turn_into_numbers_list(user_input)
        operators = turn_into_operators_list(user_input)
        num = calculate_in_order(numbers, operators)
        print(num)
    user_input = input("Please write what you want to calculate\n")
print("DONE")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
