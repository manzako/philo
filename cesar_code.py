#fonction de cryptage
def cryptage(cle, message):
    resultat=""
    for char in message:
        if char.isalpha():
            if char.isupper():
                char=chr((ord(char)+cle-65)%26+65)
            else:
                char=chr((ord(char)+cle-97)%26+97)
        resultat +=char
    return resultat

def decryptage(cle, message):
    resultat=""
    for char in message:
        if char.isalpha():
            if char.isupper():
                char=chr((ord(char)-cle-65)%26+65)
            else:
                char=chr((ord(char)-cle-97)%26+97)
        resultat +=char
    return resultat