# caesar cipher encoder and decoder

import urllib.request

response = urllib.request.urlopen("http://www-personal.umich.edu/~jlawler/wordlist")
word_list = response.read().decode("utf-8")

alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
symbols_nums = "?!#@£$%^&*()[]{}/\<>=+-'~`|:;.,\"0123456789" 
again = "yes"
while again == "yes":
    print("=" * 20)
    choice = input("Which would you like to use (enter the number 1 or 2):\n\t1. Encoder\n\t2. Decoder\n")
    while choice != "1" and choice != "2":
        choice = input("Choice not in range. Please reselect:\n\t1. Encoder\n\t2. Decoder\n")
    if choice == "1":
        words = (input("\nInput the word or sentence you would like to be encoded:\n")).split(" ")
        key = int(input("\nInput the key (the amount to be shifted by)- must be between 1 and 25 inclusive:\n"))
        while key not in range(1, 26):
            key = int(input("\nError: key not in range. Please try again:\n"))
        encrypted = []
        for word in words:
            e_word = ""
            for letter in word:
                if letter in symbols_nums:
                    e_letter = letter
                else:
                    e_letter = alphabet[alphabet.index(letter) + key]
                e_word += e_letter
            encrypted.append(e_word)
        encrypted = " ".join(encrypted)
        print("Output: " + encrypted)

    else:
        encrypted = (input("\nInput the word or sentence you would like to be decoded:\n")).split(" ")
        all_options = {}
        printed_out = 0
        for key in range(1, 26):
            decrypted = []
            real = 0
            total = len(encrypted)
            for e_word in encrypted:
                d_word = ""
                for e_letter in e_word:
                    if e_letter in symbols_nums:
                        d_letter = e_letter 
                    else:
                      d_letter = alphabet[alphabet.rindex(e_letter) - key]
                    d_word += d_letter
                decrypted.append(d_word)
                if d_word.lower() in word_list:
                    real += 1
            decrypted = " ".join(decrypted)
            all_options[key] = decrypted
            percentage = (real / total) * 100
            if percentage >= 80:
                print("\nKey: " + str(key) + "\nText: " + decrypted)
                printed_out += 1
        if printed_out == 0:
            print("\nNo suitable result found. Printing out all possibilities:\n")
            for key in all_options:
                print("Key: " + str(key) + "\nText: " + all_options[key])

    again = input("\nWould you like to encode or decode anything else? (yes/no) ")
