def get_message(name, student, age):
    message = f"Hello {name}"

    if student and (age <= 18 or age > 65):
        message += " - congratulations, you are entitled to a 20% discount"
    elif student or (age <= 18 or age > 65):
        message += " - congratulations, you are entitled to a 10% discount"
    else:
        message += " - sorry, you must pay the regular price"

    return message

name = input("What is your name? ")

student_str = input("Are you a student [y/n]? ")
student = student_str.lower() in ("y", "yes")

age_str = input("How old are you? ")
age = int(age_str)

message = get_message(name, student, age)
print(message)

print()
input("Press return to continue ...")