# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

# Moja wersja
if year % 4 != 0:
    print("That's not a leap year.")
else:
    if year % 100 != 0:
        print("That's a leap year.")
    elif year % 400 == 0:
        print("That's a leap year.")
    else:
        print("That's not a leap year.")
###############################################

# Jak powinno byc
# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not leap year.")
#     else:
#         print("leap year.")
# else:
#     print("Not leap year.")
