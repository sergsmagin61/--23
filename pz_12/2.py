#2.Составить генератор (yield), который выводит из строки только цифры.
def extract_digits(string):
    for char in string:
        if char.isdigit():
            yield char

string = "ab8c123def456ghi7899090"
digits_generator = extract_digits(string)
digits = ''.join(digits_generator)
print(digits)  
