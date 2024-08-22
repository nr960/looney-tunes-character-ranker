#inspired by https://dangansort-plus.tumblr.com/
class character:
    def __init__(self, name, place=0):
        self.name = name
        self.place = place

    def __repr__(self):
        return f"{self.name}: {self.place}"

characters = [character('Bugs'),
              character('Daffy'),
              character('Porky'),
              character('Roadrunner'),
              character('Coyote'),
              character('Sylvester'),
              character('Tweety'),
              character('Elmer'),
              character('Sam'),
              character('Marvin'),
              character('Foghorn'),
              character('Speedy'),
              character('Taz'),
              character('Gossamer'),
              character('Lola')]

print(f"Instructions: type the name of the character you prefer.")

def compare_characters(name1, name2):
    print(f"{name1.name} vs. {name2.name}")
    winner = input(f"You choose: ").strip()

    if winner.lower() == name1.name.lower():
        name1.place +=1
    elif winner.lower() == name2.name.lower():
        name2.place +=1
    else:
        print("Please type the character's name")
        compare_characters(name1, name2)

for i in range(len(characters)):
    for j in range(i + 1, len(characters)):
        compare_characters(characters[i], characters[j])

#reverse = true gives the highest "place" first
characters.sort(key=lambda x: x.place, reverse=True)

for character in characters:
    print(character.name)