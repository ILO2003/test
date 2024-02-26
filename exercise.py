'''my_age = 20

print("What is your favorite color?:")

x = input()

print("Your favorite color is " + x)




my_number = int(input("Enter a number: "))
if my_number < 5:
    print("Your number is less than 5")
elif my_number == 5:
    print("Your number is 5")
else:
    print("Your number is greater than 5")  



print("Player 1, start the game. Rock, paper or scissors? Write ur answer:")
Player1 = input()
print("Player 1 chose: " + Player1)

print("Time for Player 2, choose urs: ")
Player2 = input()


if Player1 == Player2:
    print("Error, You aren't allowed to choose same think")
elif Player1 == "rock" and Player2 == "paper":
    print("Player 1 wins with " + Player2)
elif Player1 == "paper" and Player2 == "rock":
    print("Player 1 wins with " + Player1)
elif Player1 == "scissors" and Player2 == "paper":
    print("Player 1 wins with " + Player1)
elif Player1 == "rock" and Player2 == "scissors":
    print("Player 1 wins with " + Player1)
elif Player1 == "paper" and Player2 == "scissors":
    print("Player 2 wins with " + Player2)
elif Player1 == "scissors" and Player2 == "rock":
    print("Player 2 wins with " + Player2)
else:
    print("Something went wrong, try again")

birds = ["robin", "bluebird", "sparrow", "cardinal"]

var = birds[1]

var2 = birds[3]

birds.insert(2, "woodpecker")
print(birds)
two_birds = birds[0:2]

birds.reverse()
print(birds)

print(two_birds)

birds.reverse()
print(birds)

print(birds[-2:])

    if(items[i])
'''

# items = ["steak", "apple", "bread", "butter", "pineapple"]



# for i in items:
#     if i == "apple" or i == "pineapple":
#         print(i + "is a fruit")
#     else:
#         print(i + "is not a fruit")


# counter = 1

# while counter < 1000:
#     counter = counter * 2
#     print(counter)


# def under_tenlist(list_of_numbers):
#     under_ten = []
#     under_fifty=[]

#     for i in list_of_numbers:
#         if i < 10:
#             under_ten.append(i)
#         elif i > 10 and i < 50:
#             under_fifty.append(i)

#     print("Under 10 numbers: ")
#     print(under_ten)
#     print("Over 10 but under 50 numbers: ")
#     print(under_fifty)

# under_tenlist([1, 81, 45, 3, 9, 35, 87, 44 ,6])



# college = {
#     "name": "Yale",
#     "founded": "1701",
#     "motto": "Light and truth",
#     "location": "New Haven, Connecticut",
#     "students": 12060
# }
    
# for i in college:
#     print(i)


# print(college["founded"])


password = input()

if password < 9:
    print("You need more characters!")


