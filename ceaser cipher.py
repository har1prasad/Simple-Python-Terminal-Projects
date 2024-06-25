alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def caeser(texte,shifte,directionl):
    texte = list(texte)
    for i in range(len(texte)):
        if texte[i] in alphabet:
            if directionl == "encode":
                 texte[i] = alphabet[(alphabet.index(texte[i]) + shift) % len(alphabet)]
            elif directionl == "decode":
                 texte[i] = alphabet[(alphabet.index(texte[i]) - shift) % len(alphabet)]
            else:
                 print("wrong instruction")     
        else:
             texte[i] = texte[i]
  
    texte = ''.join(texte)
    print(f"The {directionl}d text is {texte}")

caeser(texte = text,shifte = shift,directionl = direction)

   
