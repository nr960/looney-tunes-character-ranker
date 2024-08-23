#inspired by https://dangansort-plus.tumblr.com/
class character:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __repr__(self):
        return f"{self.name}: {self.score}"

characters = [character('Bugs'),
              character('Daffy'),
              character('Porky'),
              character('Coyote'),
              character('Roadrunner'),
              character('Sylvester'),
              character('Tweety'),
              character('Elmer'),
              character('Sam'),
              character('Marvin'),
              character('Foghorn'),
              character('Speedy'),
              character('Taz'),
              character('Gossamer'),
              character('Lola')
              ]

print(f"Instructions: type the name of the character you prefer, or 'tie'.")

def compare_characters(name1, name2):
    print(f"{name1.name} vs. {name2.name}")
    winner = input(f"You choose: ").strip()

    if winner.lower() == name1.name.lower():
        name1.score +=1
    elif winner.lower() == name2.name.lower():
        name2.score +=1
    elif winner.lower() == "tie":
        name1.score +=0
        name2.score +=0
    else:
        print("Please type the character's name")
        compare_characters(name1, name2)

for i in range(len(characters)):
    for j in range(i + 1, len(characters)):
        compare_characters(characters[i], characters[j])

#reverse = true gives the highest score first
characters.sort(key=lambda x: x.score, reverse=True)

scores = []

for character in characters:
    scores.append(character.score)

#print(scores)

sort_scores = sorted(enumerate(scores), key=lambda x: x[1], reverse=True)

places = [0] * len(scores)

current_place = 1
for i, (index, score) in enumerate(sort_scores):
    if i > 0 and score == sort_scores[i-1][1]:
        places[index] = current_place - 1
    else:
        places[index] = current_place
    current_place +=1

#print(places)

#the zip function allows simultaneous looping through tuples
for character, place in zip(characters, places):
    print(f"{place}. {character.name}")