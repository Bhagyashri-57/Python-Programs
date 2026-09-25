num=int(input("Enter the number: "))
if num%2==0 and num>0:
    print("Number is even and Positive ")
elif num%2!=0 and num>0:
    print("Number is odd and positive ")
elif num%2==0 and num<0:
    print("Number is even and Negative ")
else:
    print("Number is odd and Negative")