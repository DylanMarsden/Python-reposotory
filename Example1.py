print("Hello my name is Dylan")
name=input("What is your name? ")
print("Nice to meet you",name )


myage = None

while myage is None:
    inputmyage=input("How old are you? ")

    try:
        myage=int(inputmyage)
        if type(myage) == int:
            print("Wow",myage," is a nice age")
        else:
            print("sorry that isnt a number")
        if myage==100:
            print("congratulations on making it to 100")
        gender=input("Are you a girl a boy or non binary?")
        print("Aren't you a big",gender)

    except ValueError:
        print("Dodgy entry")

