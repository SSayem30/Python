alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def encryption(plane_text,shift_key):
    cipher_text=""
    for char in plane_text:
        position=alphabet.index(char)
        new_pos=(position+shift_key)%26
        cipher_text+=alphabet[new_pos]
    print(f"Encrypted message is {cipher_text}")    

def decryption(cipher_text,shift_key):
    plane_text=""
    for char in cipher_text:
        position=alphabet.index(char)
        new_pos=(position-shift_key)%26
        plane_text+=alphabet[new_pos]
    print(f"Decrypted message is {plane_text}")

while True:
    what_do=input("Type 1 for encryption and 2 for decryption and 3 for end: ")
    if what_do=='3':
        print("Have a nice day!")
        break
    text=input("Enter your message: ").lower()
    key=int(input("Enter the shift key: "))
    if what_do=='1':
        encryption(text,key)
    elif what_do=='2':
        decryption(text,key)
    else:
        print("Invalid")
        
