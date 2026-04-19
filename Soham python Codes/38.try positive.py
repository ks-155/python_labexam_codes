while True:
    try:
        n=int(input("entre the number :"))
        if n<=0:
            print("error number must be positive .try again")
            
        else:
            print("valid input")
           
    except ValueError:
        print("error invalid input ples enter the valid")