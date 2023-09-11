PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt") as names:
    names = names.readlines()

with open("./Input/Letters/starting_letter.txt") as Letter_names:
    Letter_contents = Letter_names.read()
    for name in names:
        stripped_names = name.strip()
        new_letter = Letter_contents.replace(PLACEHOLDER, stripped_names)

        with open(f"./Output/ReadyToSend/Letter_for_{stripped_names}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)





