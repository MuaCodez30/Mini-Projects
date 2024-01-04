#@MuaCodez30

print("Welcome to the One Piece quiz!")

playing = input("Would you like to play? ")

score = 0

if playing.lower() != 'yes':
    quit()

print('Great, Lets start!')

#question 1
answer = input('Who is the author of the One Piece manga? ')

if answer.lower() == 'oda' : 
   print("Correct!")
   score += 1

else:
   print("Incorrect!")

#question 2
answer = input('Who is the main character of the One Piece? ')

if answer.lower() == 'luffy': 
   print("Correct!")
   score += 1
else:
   print("Incorrect!")

#question 3
answer = input('How many crewmates did Luffy say he wanted at the beginning of the series? ')

if answer == '10': 
   print("Correct!")
   score += 1
else:
   print("Incorrect!")

#question 4
answer = input('Who gave Shanks the scar on his eye? ')

if answer.lower() == 'blackbeard': 
   print("Correct!")
   score += 1
else:
   print("Incorrect!")

#question 5
answer = input('Who promised that they would never lose another fight until they defeated a certain someone? ')

if answer.lower() == 'zoro': 
   print("Correct!")
   score += 1
else:
   print("Incorrect!")


if score >= 1:
   print('Congratulations on getting ' + str(score) + ' questions correct!')
   
else: 
   print("Unfortunately you got " + str(score) + " questions correct!")