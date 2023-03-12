# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#import main
#print("the code is looping")
#Data is a list [] with a nested list that contains a string, list[], string.  eg ["string", ["a","b", "c"], "string"]]
trivia = [
['\nWho ate the "Chop-Chop" devil fruit?', ["A. Bon Clay", "B. Buggy the Clown", "C. Daz Bones", "D. Clawador"], "B"],
["\nWho was the 3rd person to become member of the Straw Hat Pirates?", ["A. Sanji", "B. Nami", "C. Ussop", "D. Zoro"], "B"],
["\nWhat is White Beard's full name?", ["A. Edward Newgate", "B. Marshal D. Teach", "C. Basil Hawkins", "D. Demoaro Black"], "A"],
["\nWho was the first person Luffy fought in the beginning of One Piece?", ["A. Alvida", "B. Buggy the Clown", "C. Clawador", "D. Don Kreig"], "A"],
["\nWhat is this highest position within the Marines?", ["A. Admiral", "B. Fleet Admiral", "C. Vice Admiral", "D. Grand Admiral"], "B"],
["\nWhat sound did the Skyipeans hear when the Shandia were sent into the sky via 'the Knock Up Stream'", ["A. Bird", "B. Thunder", "C. Bell", "D. Explosion"], "C"],
["\nWhat animal is Chopper constantly mistaken for?", ["A. Dog", "B. Squirell", "C. Reindeer", "D. Raccoon"], "D"],
["\nThere are 10 CP9 agents. How many went undercover at the Galley La shipwright place?", ["A. 4", "B. 6", "C. 5", "D. 3"], "D"],
["\nHow old is Luffy after the time-skip?", ["A. 17", "B. 19", "C. 21", "D. 23"], "B"],
["\nWhat is Katakuri's devil fruit type?", ["A. Paramecia", "B. Logia", "C. Zoan", "D. Smile"], "A"],
["\nWho gave Luffy his scar under his eye?", ["A. Shanks", "B. Black Beard", "C. Demaoro Black", "D. Luffy"], "D"]
]

print("Welcome to One Piece Trivia!")
input("Hello contestant! Ready to play? ")
#test for yes. if not yes break in future code

name = input("\nAwesome To start off, what is your name? ")
print(f"Nice to meet you {name}!")
print("\nNow, let us get started with our first question")
score = 0



def trivia_stack(myList):
  question = myList[0]     # this is the  first string in the nested list
  choices = myList[1]      # this is a list of answers
  answer = myList[2]       # this is the last string in the nested list

  print(question)
  for choice in choices:
    print(choice)
  ans = input("\n")
  ans = ans.upper()
  if ans == answer:
    print("\nAwesome! Here are 10 points.")
    main.score += 10
  else:
    print(f"\nSorry, that is incorrect. The answer is {answer}")
  print("your score is", main.score)

def return_score(innerScore):
  #the game ended, let the user know about their overall score
  print("\n*\n*\n*\n*")
  if innerScore > 0 & innerScore <50:
    print("Your score is ",innerScore, ". Not bad but you should watch more One Piece")
  elif innerScore > 50 & innerScore <80:
    print("Your score is ",innerScore, ". You did pretty good but you should watch more One Piece")
  elif innerScore > 80 & innerScore <100:
    print("Your score is ",innerScore, ". Awesome job!")
  elif innerScore == 110:
    print("Your score is ",innerScore, ". You did perfect. Maybe you watch too much One Piece")


for triv in trivia:
  #trivia_stack(triv)
  print(triv)

return_score(score)








#
# trivia_stack('\nWho ate the "C