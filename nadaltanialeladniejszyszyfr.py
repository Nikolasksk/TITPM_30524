import string

def salatka(text, shift, alphabets):
    
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]
        
    shifted_alphabets = map(shift_alphabet, alphabets)
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)
        
plain_text = "fbkcncl rnku JKJK"
print(salatka(plain_text, -2, [string.ascii_lowercase, string.ascii_uppercase]))