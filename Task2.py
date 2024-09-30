from PIL import Image
import numpy as np 

# Function to encrypt the image
def encrypt_image(image_path, key, output_path):
    # Open the image and convert it to a NumPy array
    img = Image.open(image_path)
    img_array = np.array(img)

    # Encrypt by adding the key value to each pixel
    encrypted_array = (img_array + key) % 256

    # Convert back to image and save
    encrypted_img = Image.fromarray(encrypted_array.astype('uint8'))
    encrypted_img.save(output_path)
    print(f"Image encrypted and saved as {output_path}")

# Function to decrypt the image
def decrypt_image(image_path, key, output_path):
    # Open the image and convert it to a NumPy array
    img = Image.open(image_path)
    img_array = np.array(img)

    # Decrypt by subtracting the key value from each pixel
    decrypted_array = (img_array - key) % 256

    # Convert back to image and save
    decrypted_img = Image.fromarray(decrypted_array.astype('uint8'))
    decrypted_img.save(output_path)
    print(f"Image decrypted and saved as {output_path}")

# Main function
def main():
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()
    image_path = input("Enter the path of the image: ")
    output_path = input("Enter the output path for the processed image: ")
    key = int(input("Enter the encryption/decryption key (a number): "))

    if choice == 'encrypt':
        encrypt_image(image_path, key, output_path)
    elif choice == 'decrypt':
        decrypt_image(image_path, key, output_path)
    else:
        print("Invalid choice! Please select either 'encrypt' or 'decrypt'.")

# Run the program
if __name__ == "__main__":
    main()
