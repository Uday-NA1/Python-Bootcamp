alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(original_text, shift_amount, decode_or_encode):
    output_text = ""

    for letter in original_text:
        if decode_or_encode == "encode":
            shifted_position = alphabet.index(letter) + shift_amount
        if decode_or_encode == "decode":
            shifted_position = alphabet.index(letter) - shift_amount
        

        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]

    print(f"Here is the encoded result: {output_text}")

should_continue = True

while should_continue: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type your shift number:\n"))

    caeser(original_text=text, shift_amount=shift, decode_or_encode=direction)

    restart = input("Type `yes` if you want to go again. Otherwise, type `no`. \n").lower()

    if restart == "no":
        should_continue = False
        print("Goodbye")