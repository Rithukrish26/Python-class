#Use conditional statement and get the marks
# print the result for the following marks
# 90 to 100=A grade
# 80 to 90=B grade
# 70 to 80= C grade
# 60 to 70= D grade
# below 60= E grade

eng=int(input("Enter your English marks"))
tam=int(input("Enter your Tamil marks"))
math=int(input("Enter your Math marks"))
sci=int(input("Enter your Science marks"))
sst=int(input("Enter your Social Studies marks"))
total=(eng+tam+math+sci+sst)
print("Your total marks :",total)
avg=((eng+tam+math+sci+sst)/5)
print("Your average marks :",avg)

if avg>=90 and avg<=100:
    print("A Grade")
elif avg >= 80 and avg <=90:
    print("B Grade")
elif avg>=70 and avg<=80:
    print("C Grade")
elif avg>=60 and avg<=70:
    print("D Grade")
else:
    print ("E grade")

