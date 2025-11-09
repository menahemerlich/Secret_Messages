
def atbash_cipher(text):
    result = ""
    for char in text:
        if 'a' <= char <= 'z':
            result += chr(ord('a') + ord('z') - ord(char))
        elif 'A' <= char <= 'Z':
            result += chr(ord('A') + ord('Z') - ord(char))
        else:
            result += char
    return result

message = input("Enter your message: ")
s_message = atbash_cipher(message)

with open("secret.txt", "w") as f:
    f.write(f"{s_message}\n")

with open("secret.txt", "r") as f:
    print(f.read())

message = atbash_cipher(s_message)

with open("secret.txt", "a") as f:
    f.write(message)





