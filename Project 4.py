#Guess the password

Password="YoIvRiDaDi"
User_Input=input("Enter the password to gain access:")
while Password!=User_Input:
    print("Incorrect.")
    User_Input=input("Enter the correct password:")
print("Access granted")