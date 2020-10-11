name = input("Enter Name: ")
VOWEL = "aeiou"

for word in name:
    if word in VOWEL:
        print("Vowel ", word)