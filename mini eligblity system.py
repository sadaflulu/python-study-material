age=int(input("enter age: "))
exam_mark=int(input("enter mark: "))
document=input('weather the document are available(yes or no): ')

print(age)
print(exam_mark)
print(document)


if age >= 18 or exam_mark >=50 or document=="yes":
    print("admission eligible")
else:
    print("admission not eligible")


# age = int(input("Enter age: "))
# exam_mark = int(input("Enter mark: "))
# document = input("Whether the documents are available (yes or no): ")

# print(age >= 18)
# print(exam_mark >= 50)
# print(document == "yes")

# if age >= 18 or exam_mark >= 50 or document == "yes":
#     print("Admission eligible")
# else:
#     print("Admission not eligible")
 