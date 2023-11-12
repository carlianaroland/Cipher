# Carliana Roland 2/21/23 Comp163

word = input('Type message here. Type QUIT to end: ')
# THIS IS YOUR WHILE LOOP, IT WILL NOT END UNTIL YOU TYPE THE WORD QUIT.
while word != 'QUIT':
    encrypt_decrypt = input('Type ENCRYPT or DECRYPT: ')
    alphabet_letters = {'a': 'u', 'b': 'v', 'c': 'w', 'd': 'x', 'e': 'y', 'f': 'z', 'g': 'a', 'h': 'b', 'i': 'c',
                        'j': 'd', 'k': 'e', 'l': 'f', 'm': 'g', 'n': 'h', 'o': 'i', 'p': 'j', 'q': 'k', 'r': 'l',
                        's': 'm', 't': 'n', 'u': 'o', 'v': 'p', 'w': 'q', 'x': 'r', 'y': 's', 'z': 't', 'A': 'D',
                        'B': 'E', 'C': 'F', 'D': 'G', 'E': 'H', 'F': 'I', 'G': 'J', 'H': 'K', 'I': 'L', 'J': 'M',
                        'K': 'N', 'L': 'O', 'M': 'P', 'N': 'Q', 'O': 'R', 'P': 'S', 'Q': 'T', 'R': 'U', 'S': 'V',
                        'T': 'W', 'U': 'X', 'V': 'Y', 'W': 'Z', 'X': 'A', 'Y': 'B', 'Z': 'C'}
# YOU ARE TO USE THIS IF LOOP TO ENCRYPT A CODE
    if encrypt_decrypt == 'ENCRYPT':
        encrypt = ''
        for i in word:
            if i in alphabet_letters:
                encrypt += alphabet_letters[i]
        print('ENCRYPT MESSAGE IS: ', encrypt)
# THIS IS FOR THE OPTION OF DECRYPTING A MESSAGE
    elif encrypt_decrypt == 'DECRYPT':
        decrypt = ''
        for i in word:
            for k, v in alphabet_letters.items():
                if i == k:
                    decrypt += k
        print('DECRYPT MESSAGE IS: ', decrypt)
# THE LOOP WILL EXIT AFTER THE BREAK STATEMENT
        break
