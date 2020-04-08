def getMode():
    while True:
        mode=input("Vous voulez crypter 'c' ou decrypter votre message 'd' ? \n")
        if mode in 'c d':
            return mode
        else:
            print("veillez saisir 'c' pour crypter ou 'd' pour decrypter \n")


def getKey():
    while True: 
        key= int(input("Veuillez saisir la valeur de la cle entre 1 et 26 \n"))
        if (key >=1  and key <= 26):
            return(key)
        
def getMessage(): 
    while True: 
        message=input("Veuillez saisir le message a crypter/decypter \n")
        if (len(message) in range(1,200)):
            return(message)

def getTranslated(mode, message, key):
    if mode == "d":
        key=-key
    translated=''
    for char in message:
         if char.isalpha():
            nbr=ord(char)
            nbr+=key
            if char.isupper():
                 if nbr > ord("Z"):
                    nbr-=26
                 elif nbr < ord("A"):
                    nbr-=26
            elif char.islower():
                 if nbr > ord("z"):
                    nbr-=26
                 elif nbr < ord ("a"):
                    nbr +=26
            translated+=chr(nbr)
         else:
                translated+=char
    return(translated)    


mode=getMode()
message=getMessage()
key=getKey()
print(getTranslated(mode,message,key))


