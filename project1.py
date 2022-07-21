from library import *
f=input("Enter Your file Name:")
File=open(f+".txt", "w")
File.close()


while True:
    print(
        "1. Odd or Even \n2. Max of two Number\n3. Max of three Number\n4. Fibonacci Series\n5. Pattern Printing\n6. Prime or Not Prime\n7. Close" 
    )
    p=int(input("Select the choice: "))
    File=open(f+".txt", "a")
    if p==1:
        a=int(input("Enter a Number: "))
        OddEven(a)
        File.write("\nYou have done oddeven Function.")
        print("You have done oddeven Function.")
    
    elif p==2:
        a=int(input("Enter a Number: "))
        b=int(input("Enter a Number: "))
        MaxOfTwo(a, b)
        File.write("\nYou have done MaxOfTwo Function.")
        print("You have done MaxOfTwo Function.")


    elif p==3:
        a=int(input("Enter a Number: "))
        b=int(input("Enter a Number: "))
        c=int(input("Enter a Number: "))
        MaxOfThree(a, b, c)
        File.write("\nYou have done MaxOfThree Function.")
        print("You have done MaxOfThree Function.")

    elif p==4:
        a=int(input("Enter a Number: "))
        Fibonacci(a)
        File.write("\nYou have done Fibonacci Function.")
        print("You have done Fibonacci Function.")
    
    elif p==5:
        a=int(input("Enter a Number: "))
        pattern(a)
        File.write("\nYou have done pattern Function.")
        print("You have done pattern Function.")

    elif p==6:
        a=int(input("Enter a Number: "))
        Prime(a)
        File.write("\nYou have done Prime Function.")
        print("You have done Prime Function.")

    elif p==7:
        File.write("\nThank You for visit, Bye.")
        print("Thank You for visit, Bye.")
        break
    else:
        print("Please Enter a correct Number.")

    File.close()

File=open(f+".txt", "r")
print(File.read())
File.close()
