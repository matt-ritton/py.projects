list = [] #List for valid letters

secret_word = 'Python'.upper()
chances = 3

while True:

    #Check how many chances the player has left
    if chances <= 0:
        print("YOU LOSE!")
        print(f'The secret word was {secret_word}!')
        break

    char = input('Insert one character: ').upper()

    #String lenght checker for valid inputs
    if len(char) > 1:
        print('Only one character!')
        continue

    #Check if the character is part of the secret word
    if char in secret_word:
        print("This character is in the secret word!")
        list.append(char) #Only add character to our list if this condition is true
    else:
        print("This character don't be part of secret word.\n")
        chances -= 1
        print(f'You have {chances} chances.')

    #The magic is here...
    temp = ''

    #First: for every character present in the secret word
    for string_char in secret_word:

        #If this character is valid (only valid character are added to our list)
        if string_char in list:
            temp += string_char #Our temporary variable receives the character in the current position
        else:
            temp += '#' #Add # in the current position

    print('Secret Word: ' + temp)

    if temp == secret_word:
        print("YOU WIN!")
        break
