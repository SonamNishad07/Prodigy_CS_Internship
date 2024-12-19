def caesar_cipher(text, shift, mode='encrypt'):
    """
    Caesar Cipher function to encrypt or decrypt a text.

    Parameters:
    - text (str): The input text.
    - shift (int): The shift value (key).
    - mode (str): Either 'encrypt' or 'decrypt'.

    Returns:
    - str: The resulting text after applying the Caesar Cipher.
    """
    result = ''
    
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            result += shifted_char
        else:
            result += char

    return result


# Example Usage
if __name__ == "__main__":
    print("Caesar Cipher Program")
    choice = input("Choose mode (encrypt/decrypt): ").strip().lower()
    text = input("Enter the text: ")
    shift = int(input("Enter the shift value (key): "))

    output = caesar_cipher(text, shift, mode=choice)
    print(f"Result: {output}")