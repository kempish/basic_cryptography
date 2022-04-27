from msvcrt import getwch


def limited_answer(prompt, valid_input):
    print(prompt)
    answer = getwch().capitalize()

    try:
        answer = int(answer)
    except:
        answer = str(answer)

    if answer not in valid_input or type(answer) != type(valid_input[0]):
        return limited_answer(f"Please enter valid data: ", valid_input)
    else:
        return answer


def limited_characters(prompt):
    verboten_characters = [chr(x) for x in range(0, 48)] + [chr(x) for x in range(58, 65)] + [chr(x) for x in range(91, 97)] + [chr(x) for x in range(123, 400)]
    answer = input(prompt)
    
    if any(char in verboten_characters for char in answer):
        return limited_characters('You have used not allowed characters. Please use only numbers and letters: ')
    else:
        return answer


def encrpyt_password():
    encrypt_or_decrypt = limited_answer('do you want do encrypt [E] or decrypt your password [D]? ', ['E', 'D'])

    if encrypt_or_decrypt == 'E':
        key_number = limited_answer('enter your key number (from 1 to 9) - required to encrypt main password: ', range(1, 9))
        main_password = list(limited_characters('enter your main password - please use only numbers and letters (this password will be encrypted): '))
    elif encrypt_or_decrypt == 'D':
        key_number = limited_answer('enter your key number (from 1 to 9) - required to decrypt main password (enter same key number used to crypted!): ', range(1, 9))
        main_password = list(input('enter your main password - this password will be decrypted: '))
    
    main_password_ascii = [ord(letter) for letter in main_password]

    encrypted_main_password_ascii = [x - key_number for x in main_password_ascii] if encrypt_or_decrypt == 'E' else [x + key_number for x in main_password_ascii]
    encrypted_main_password = [chr(x) for x in encrypted_main_password_ascii]

    pass_input = ''.join(main_password)
    pass_output = ''.join(encrypted_main_password)

    print(f'initial:\t{pass_input}')
    print(f'encrypted:\t{pass_output}')

    return pass_output


encrpyt_password()