# 
# a=int(input("enter your marks: "))
# if a>=90 and a<=100:
#     print("A+")
# elif a>=80 and a<=89:
#     print("A")
# elif a>=70 and a<=79:
#     print("B+")
# elif a>=60 and a<=69:
#     print("B")
# elif a<=50 and a>=59:
#     print("C")
# else:
#     print("F")
user_input = input("Enter a word: ")

if len(user_input) > 10:
    print("The word has more than 10 letters.")
else:
    print("The word has less than 10 letters.")