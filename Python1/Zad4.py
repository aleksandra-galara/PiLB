correct_code= "1423"
closed=1

while closed:
    code=input("Please enter your code:  ")
    if len(code)!=4:
        print("Your code should be 4 numbers length! Try again!")
    else:
        if code==correct_code:
            print("It's open now!")
            closed=0
        else:
            print("Wrong code!")
