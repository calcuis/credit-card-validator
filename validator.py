from tkinter import *

def get_digit(number):
    return number % 10 + (number // 10 % 10)

def sum_odd_digits(card_number):
    sum_odd = 0
    for i in range(len(card_number) - 1, -1, -2):
        sum_odd += int(card_number[i])
    return sum_odd

def sum_even_digits(card_number):
    sum_even = 0
    for i in range(len(card_number) - 2, -1, -2):
        sum_even += get_digit(int(card_number[i]) * 2)
    return sum_even

def validate_number():
    card = input_number.get()

    try:
        result = sum_even_digits(card) + sum_odd_digits(card)

        if card == "":
            output["text"] = "cannot be empty!"
        elif result % 10 == 0:
            output["text"] = f"{card} is valid!"
        else:
            output["text"] = f"{card} is not valid!"
            
    except ValueError:
            output["text"] = "accept numbers only!"

root = Tk()
root.title("check")
root.geometry("200x80")

input_number = Entry()
input_number.pack()
btn_click = Button(text="validate", command=validate_number)
btn_click.pack()
output = Label()
output.pack()

root.mainloop()
