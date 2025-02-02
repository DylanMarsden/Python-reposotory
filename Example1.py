def Tell_me_a_number(passednumber,question):
    while passednumber is None:
        inputmyage=input(question)

        try:
            passednumber=int(inputmyage)
            if type(passednumber) == int:
                print("Wow",passednumber," is a nice number")
                return passednumber
            else:
                print("sorry that isnt a number")
          
        except ValueError:
            print("Dodgy entry")

        



print("Hello my name is Dylan")
name=input("What is your name? ")
print("Nice to meet you",name )

myage = None
question= "How old are you? "
myage = Tell_me_a_number(myage, question)
 
legs=None
question= "How many legs? "
legs = Tell_me_a_number(legs,question)


genderList = {"boy","girl","non binary"}

gender = None

while gender not in genderList:
    gender=input("Are you a girl a boy or non binary?").lower()


    if gender in genderList:
        print(f"You are called {name}, you are {myage}.  Arent you big {gender}")
    else:
        print("That isnt a valid answer, Try again")

siblings=None
question="How many siblings do you have?"
siblings = Tell_me_a_number(siblings,question)

print("legs=", legs)
print("siblngs=", siblings)
print("age=", myage)