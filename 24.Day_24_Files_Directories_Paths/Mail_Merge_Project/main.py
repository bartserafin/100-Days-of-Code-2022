#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Names/invited_names.txt', mode='r') as names:
    names_list = names.readlines()

clean_names = []
for name in names_list:
    clean_name = name.strip()
    clean_names.append(clean_name)

with open('./Input/Letters/starting_letter.txt', mode='r') as letter:
    new_letter = letter.read()
    for name in clean_names:
        ready_letter = new_letter.replace('[name]', name)

        with open(f'./Output/ReadyToSend/letter_for_{name}', mode='w') as letter_to_sent:
            letter_to_sent.write(ready_letter)