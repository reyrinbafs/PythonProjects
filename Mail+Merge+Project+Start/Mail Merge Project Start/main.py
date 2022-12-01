#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp

letter_read = open("./input/letters/starting_letter.txt")
name_read = open("./input/names/invited_names.txt")
name = name_read.read()

for names in name.split():
    with open(f"./output/ReadyToSend/letter_for_{names}.txt", "w") as letter:
        letter.write(letter_read.read().replace("[name]", names))



#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp