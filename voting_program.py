name=input("Enter a name: ")
age=int(input("Enter age : "))
if age >=18:
    gender=str(input("Enter Gender(M/F/TRANS): ")).upper()
    if gender in ["M","F","TRANS"]:
        if age >=60:
            print("Go to senior citizen line")
        elif age >=18 and age <60:
            if gender == "M":
                print("Go to male line")
            elif gender == "F":
                print("Go to female line")
            else:
                print("Go to transgender line")
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
Enter a name: sandhiya
Enter age : 20
Enter Gender(M/F/TRANS): f
Go to female line
Enter the politician(TVK/DMK):dmk
you voted successfully for  DMK


** Process exited - Return Code: 0 **

