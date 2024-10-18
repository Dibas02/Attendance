medical = input("Do you have a medical cause? type 'y' for yes and 'n' for no: ")

if medical == 'y' or medical == 'Y':
    print("You are allowed in the exam.")

else:
    attendance = int(input("Enter your rate of attendace: "))

    if attendance >75 :
        print("You are allowed in the exam.")

    else:
         print("You are not allowed in the exam.")

