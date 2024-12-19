from PIL import Image
import random

# Function to encrypt an image
def encrypt_image(input_image_path, output_image_path, key):
    # Open the image
    img = Image.open(input_image_path)
    pixels = img.load()

    # Get the size of the image
    width, height = img.size

    # Encrypt the image by applying a basic transformation to each pixel
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            # Apply the transformation: XOR the color channels with the key
            r = (r + key) % 256
            g = (g + key) % 256
            b = (b + key) % 256
            pixels[i, j] = (r, g, b)
    
    # Save the encrypted image
    img.save(output_image_path)
    print(f"Encrypted image saved as {output_image_path}")

# Function to decrypt an image (reverse of the encryption)
def decrypt_image(input_image_path, output_image_path, key):
    # Open the image
    img = Image.open(input_image_path)
    pixels = img.load()

    # Get the size of the image
    width, height = img.size

    # Decrypt the image by reversing the transformation
    for i in range(width):
        for j in range(height):
            r, g, b = pixels[i, j]
            # Reverse the transformation: XOR the color channels with the key (inverse operation)
            r = (r - key) % 256
            g = (g - key) % 256
            b = (b - key) % 256
            pixels[i, j] = (r, g, b)
    
    # Save the decrypted image
    img.save(output_image_path)
    print(f"Decrypted image saved as {output_image_path}")

# Main function to demonstrate the encryption/decryption tool
def main():
    # Specify paths to the images
    input_image_path = input("Enter the path to the image to encrypt: ")
    encrypted_image_path = "encrypted_image.png"
    decrypted_image_path = "decrypted_image.png"
    
    # Get the encryption key from the user (for simplicity, using a small integer key)
    key = int(input("Enter an encryption key (integer between 1-255): "))

    # Encrypt the image
    encrypt_image(input_image_path, encrypted_image_path, key)

    # Decrypt the image
    decrypt_image(encrypted_image_path, decrypted_image_path, key)

    print(f"Original image: {input_image_path}")
    print(f"Encrypted image: {encrypted_image_path}")
    print(f"Decrypted image: {decrypted_image_path}")

# Run the tool
if __name__ == "__main__":
    main()