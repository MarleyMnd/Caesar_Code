def encrypt(string, key):
    """ Helps the user to encrypt a message indicating the key """

    string = tuple(string)
    encrypted_string = ''
    for i, ele in enumerate(string):
        # If the element is anything but a number
        if type(ele) is str:

            """ ------------------------- Special characters ------------------------- """

            # Space
            if ord(ele) == 32:
                encrypted_string += ele

            # Very used special characters (/, !, #, ", etc.)
            if 32 < ord(ele) < 48:
                encrypted_string += ele

            # More special characters
            if 57 < ord(ele) < 65:
                encrypted_string += ele

            # Still special characters
            if 90 < ord(ele) < 97:
                encrypted_string += ele

            # More and more special characters
            if 122 < ord(ele) < 127:
                encrypted_string += ele

            # Reversed '!'
            if ord(ele) == 161:
                encrypted_string += ele

            # Reversed '?'
            if ord(ele) == 191:
                encrypted_string += ele

            # Currencies
            if ele in ['€', '$', '£', '¢', '¥']:
                if ele == '€':
                    encrypted_string += '€'
                if ele == '$':
                    encrypted_string += '$'
                if ele == '£':
                    encrypted_string += '£'
                if ele == '¢':
                    encrypted_string += '¢'
                if ele == '¥':
                    encrypted_string += '¥'

            """ -------------------- Uppercase special characters -------------------- """

            # Uppercase accents on 'A'
            if 191 < ord(ele) < 198:
                ele = 'A'

            # Character 'Ç'
            if ord(ele) == 199:
                ele = 'C'

            # Uppercase accents on 'E'
            if 199 < ord(ele) < 204:
                ele = 'E'

            # Uppercase accents on 'I'
            if 203 < ord(ele) < 208:
                ele = 'I'

            # Character 'Ñ'
            if ord(ele) == 209:
                ele = 'N'

            # Uppercase accents on 'O'
            if 209 < ord(ele) < 215:
                ele = 'O'

            # Uppercase accents on 'U'
            if 216 < ord(ele) < 221:
                ele = 'U'

            # Character 'Ý'
            if ord(ele) == 221:
                ele = 'Y'

            """ -------------------- Lowercase special characters -------------------- """

            # Lowercase accents on 'a'
            if 223 < ord(ele) < 230:
                ele = 'a'

            # Character 'ç'
            if ord(ele) == 231:
                ele = 'c'

            # Lowercase accents on 'e'
            if 231 < ord(ele) < 236:
                ele = 'e'

            # Lowercase accents on 'i'
            if 235 < ord(ele) < 240:
                ele = 'i'

            # Character 'ñ'
            if ord(ele) == 241:
                ele = 'n'

            # Lowercase accents on 'o'
            if 241 < ord(ele) < 247:
                ele = 'o'

            # Lowercase accents on 'u'
            if 248 < ord(ele) < 253:
                ele = 'u'

            # Character 'ý'
            if ord(ele) == 253:
                ele = 'y'

            # Character 'ÿ'
            if ord(ele) == 255:
                ele = 'y'

            # Uppercase
            if 64 < ord(ele) < 91:
                x = ord(ele) + key
                # In case we go past 'Z', we return to the beginning of the alphabet
                if x > 90:
                    x = (ord(ele) + key) - 26
                encrypted_string += chr(x)

            # Lowercase
            if 96 < ord(ele) < 123:
                x = ord(ele) + key
                # In case we go past 'z', we return to the beginning of the alphabet
                if x > 122:
                    x = (ord(ele) + key) - 26
                encrypted_string += chr(x)
        # If the element is a number
        if ele.isdigit():
            encrypted_string += ele

    return encrypted_string
