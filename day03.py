
print("===== ELIGIBILITY CHECKER =====")

age = int(input("Enter your age: "))
has_account = input("Do you have an account? (yes/no): ")

if age >= 18 and has_account.lower() == "yes":
    print("You meet the eligibility conditions.")

elif age >= 18 and has_account.lower() == "no":
    print("You meet the age condition, but need an account.")

else:
    print("You do not meet the age condition.")

print("Thank you for using the program!")
