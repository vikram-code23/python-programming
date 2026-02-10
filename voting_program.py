name=input("Enter a name: ")
age=int(input("Enter age : "))
if age >=18:
    gender=str(input("Enter Gender(M/F/TRANS): ")).upper()
    if gender in ["M","F","TRANS"]:
        if age >=60:
            print("Go to senior citizen line")
        else:
            print("Go to queue 1")
        vote = input("Enter the politician(TVK/DMK):").upper()
        if vote == "TVK" or vote == "DMK":
            print("you voted successfully for ",vote)
        else:
            print("Invalid party name")            
    else:
        print("Invalid character, type only [M/F/TRANS]")
else:
    print("You are not eligible for this vote")

output:
Enter a name: vikram
Enter age : 30
Enter Gender(M/F/TRANS): m
Go to queue 1
Enter the politician(TVK/DMK):tvk
you voted successfully for  TVK


** Process exited - Return Code: 0 **
