abc = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar_encoder(offset, code):
    msg = []
    for letter in code:
        if letter in abc:
            msg.append(abc[(abc.index(letter) - offset) % 26])
        else:
            msg.append(letter)

    return "".join(msg)

def caesar_decoder(offset, code):
    msg = []
    for letter in code:
        if letter in abc:
            msg.append(abc[(abc.index(letter) + offset) % 26])
        else:
            msg.append(letter)

    return "".join(msg)

def vignere_encoder(key, code):
    offsets = [abc.index(i) for i in key]
    msg = []
    key_index = 0
    for letter in code:
        if letter in abc:
            shift = offsets[key_index % len(offsets)]
            msg.append(abc[(abc.index(letter) - shift) % 26])
            key_index += 1
        else:
            msg.append(letter)
    return "".join(msg)

def vignere_decoder(key, code):
    offsets = [abc.index(i) for i in key]
    msg = []
    key_index = 0
    for letter in code:
        if letter in abc:
            shift = offsets[key_index % len(offsets)]
            msg.append(abc[(abc.index(letter) + shift) % 26])
            key_index += 1
        else:
            msg.append(letter)
    return "".join(msg)

def caesar_output():
    user_response = input("Encode(1) or Decode(2) or Back(0): ").lower().strip()
    if user_response == "1" or user_response == "encode":
        print("Starting Encoding...")
        offset = int(input("Enter offset: "))
        code = input("Enter message: ").lower()
        print(caesar_encoder(offset, code))
    elif user_response == "2" or user_response == "decode":
        print("Starting Decoding...")
        offset = int(input("Enter offset: "))
        code = input("Enter encoded message: ").lower()
        print(caesar_decoder(offset, code))
    elif user_response == "0" or user_response == "back":
        output()
    else:
        caesar_output()

def vignere_output():
    user_response = input("Encode(1) or Decode(2) or Back(0): ").lower().strip()
    if user_response == "1" or user_response == "encode":
        print("Starting Encoding...")
        key = input("Enter key: ").lower()
        code = input("Enter message: ").lower()
        print(vignere_encoder(key, code))
    elif user_response == "2" or user_response == "decode":
        print("Starting Decoding...")
        key = input("Enter Key: ").lower()
        code = input("Enter encoded message: ").lower()
        print(vignere_decoder(key, code))
    elif user_response == "0" or user_response == "back":
        output()
    else:
        vignere_output()

def output():
    try:
        print("\n\n***Welcome to my Caesar/Vignere Cipher encoding/decoding program!***")
        user_response = input("\n\nChoose your cipher:\nCaesar(1) or Vignere(2): ").lower().strip()
        if user_response == "1" or user_response == "caesar":
            caesar_output()
        elif user_response == "2" or user_response == "vignere":
            vignere_output()
        else:
            print("you done goofed!")
            output()
        output()
    except Exception as e:
        print("you done goofed very bad. Try again... \n🔴ERROR MESSAGE:", e)
    finally:
        output()
output()

