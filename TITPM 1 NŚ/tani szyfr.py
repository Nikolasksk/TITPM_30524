
import string

#plain_text = "hello world HIHIHI"
plain_text = "jgnnq yqtnf JKJKJK"

#shift = 2
shift = -2

alphabet = string.ascii_lowercase + string.ascii_uppercase

shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet, shifted)

szyfr = plain_text.translate(table)

print(szyfr)