
# this is the key for offset of ten
alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "

def decode_it(message, offset):

    receiving_message = message
    translated_message = ""
    for letter in receiving_message:
        # this looks for the punctuation
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            # This added letters while using the offset and checks for numbers that go over the alphabet
            translated_message += alphabet[(letter_value + offset) % 26]
        else:
            translated_message += letter
    return translated_message
print(decode_it(" bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!", 14))

# this encodes messages
def coder(message, offset):
    receiving_message = message
    translated_message = ""
    for letter in receiving_message:
        if not letter in punctuation:
            letter_value = alphabet.find(letter)
            translated_message += alphabet[(letter_value - offset) % 26]
        else:
            translated_message += letter
    return translated_message
print(coder("this is making more sense", 14))

coded_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
# This brute forces out the offset number
# for i in range(1, 26):
#     print("offset: " + str(i))
#     print("\t" + decode_it(coded_message, i) + "\n")

def vigenere_decoder(coded_message, keyword):
    letter_pointer = 0
    keyword_final = ""
    # this combs over the given code
    for i in range(0,len(coded_message)):
        # this goes over punctuation
        if coded_message[i] in punctuation:
            keyword_final += coded_message[i]
        else:
            # This adds the letters to the empty sting
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    translated_message = ""
    for i in range(0,len(coded_message)):
        if not coded_message[i] in punctuation:
            ln = alphabet.find(coded_message[i]) - alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += coded_message[i]
    return translated_message
message = "dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!"
keyword = "friends"

print(vigenere_decoder(message, keyword))

def vigenere_coder(message, keyword):
    letter_pointer = 0
    keyword_final = ""
    for i in range(0,len(message)):
        if message[i] in punctuation:
            keyword_final += message[i]
        else:
            keyword_final += keyword[letter_pointer]
            letter_pointer = (letter_pointer+1)%len(keyword)
    translated_message = ""
    for i in range(0,len(message)):
        if not message[i] in punctuation:
            ln = alphabet.find(message[i]) + alphabet.find(keyword_final[i])
            translated_message += alphabet[ln % 26]
        else:
            translated_message += message[i]
    return translated_message
message_for_v = "thanks for teaching me all these cool ciphers! you really are the best!"
keyword = "besties"

print(vigenere_coder(message_for_v,keyword))
print(vigenere_decoder(vigenere_coder(message_for_v, keyword), keyword))