import day_8_project_art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(text, shift, direction):
    end_text = ""

    if shift > 25:
        shift %= 26

    if direction == "decode":
        shift *= -1

    for letter in text:
        if not letter.isalpha():
            end_text += letter
            continue

        letter_idx = alphabet.index(letter)
        letter_idx += shift

        if letter_idx > 25:
            letter_idx = letter_idx % 25 - 1
        elif letter_idx < 0:
            letter_idx += 26

        end_text += alphabet[letter_idx]
    print(f"The {direction} text is {end_text}.")


keepGoing = True
while keepGoing:
    print(day_8_project_art.logo)
    direction_code = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text_org = input("Type your message:\n").lower()
    shift_amount = int(input("Type the shift number:\n"))

    caesar(text_org, shift_amount, direction_code)

    should_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'. ").lower()
    if should_continue == 'no':
        print("Goodbye.")
        keepGoing = False

