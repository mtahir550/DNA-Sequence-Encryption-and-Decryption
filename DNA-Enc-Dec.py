from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import secrets
from Bio import SeqIO
import Bio
import cv2
import pytesseract

def rotate_crossover(dna_sequence, rotation_offset):
    rotated_sequence = dna_sequence[-rotation_offset:] + \
        dna_sequence[:-rotation_offset]
    return rotated_sequence


def reverse_rotate_crossover(population, rotation_offset):
    new_population = []
    for chromosome in population:
        reversed_chromosome = chromosome[rotation_offset:] + \
            chromosome[:rotation_offset]
        new_population.append(reversed_chromosome)
    return new_population


def mutation(dna_sequence):
    mutated_sequence = ''
    mutation_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    for base in dna_sequence:
        mutated_sequence += mutation_map.get(base, base)
    return mutated_sequence


def reverse_mutation(dna_sequence):
    reverse_mutation_map = {'T': 'A', 'A': 'T', 'G': 'C', 'C': 'G'}
    new_sequence = ''
    for base in dna_sequence:
        new_sequence += reverse_mutation_map.get(base, base)
    return new_sequence


def reshape(dna_sequence, chromosome_length):
    chromosomes = []
    for i in range(0, len(dna_sequence), chromosome_length):
        chromosomes.append(dna_sequence[i:i + chromosome_length])
    return ''.join(chromosomes)


def reverse_reshape(population):
    return ''.join(population)


def dna_to_binary(dna_sequence):
    binary_sequence = ''
    binary_map = {'A': '00', 'T': '01', 'C': '10', 'G': '11'}
    for letter in dna_sequence:
        if letter in binary_map:
            binary_sequence += binary_map[letter]
        else:
            binary_sequence += '00'
    return binary_sequence


def binary_to_dna(binary_sequence):
    dna_map = {'00': 'A', '01': 'T', '10': 'C', '11': 'G'}
    dna_sequence = [binary_sequence[i:i+2]
                    for i in range(0, len(binary_sequence), 2)]
    return ''.join(dna_map[binary] for binary in dna_sequence)


def aes_encrypt(data, key):
    backend = default_backend()
    iv = b'0123456789012345'  # Initialization Vector (IV)

    # Apply rotate_crossover before mutation
    # Specify the rotation offset here
    rotated_dna = rotate_crossover(data, 10)
    # Apply mutation to the rotated DNA
    mutated_dna = mutation(rotated_dna)
    # You can specify the chromosome length here
    reshaped_dna = reshape(mutated_dna, 3)
    # Convert reshaped DNA data to binary
    binary_dna = dna_to_binary(reshaped_dna)

    cipher = Cipher(algorithms.AES(key), modes.CFB(
        iv), backend=backend)
    encryptor = cipher.encryptor()

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(binary_dna.encode()) + padder.finalize()

    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()
    return base64.b64encode(encrypted_data).decode()


def aes_decrypt(encrypted_data, key):
    backend = default_backend()
    iv = b'0123456789012345'  # Initialization Vector (IV)

    cipher = Cipher(algorithms.AES(key), modes.CFB(
        iv), backend=backend)
    decryptor = cipher.decryptor()

    decrypted_data = decryptor.update(base64.b64decode(
        encrypted_data.encode())) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()

    # convert binary to DNA
    bin_2_dna = binary_to_dna(unpadded_data.decode())
    # Reverse reshape
    reverse_resh = reverse_reshape(bin_2_dna)
    # Reverse mutation
    reverse_mut = reverse_mutation(reverse_resh)
    # Apply reverse_rotate_crossover after reverse_mutation
    original_dna = reverse_rotate_crossover(
        [reverse_mut], 10)[0]  # Specify the rotation offset here
    return original_dna


def generate_aes_key():
    return secrets.token_bytes(32)  # 256-bit key


def extract_specific_characters(image_path, target_characters):
    # Load image using OpenCV
    image = cv2.imread(image_path)

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur to reduce high-frequency noise
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply Median Filtering to reduce salt-and-pepper noise
    denoised = cv2.medianBlur(blurred, 5)  # Adjust the kernel size as needed

    # Apply thresholding to enhance characters
    _, thresholded = cv2.threshold(
        denoised, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find contours and bounding boxes
    contours, _ = cv2.findContours(
        thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    extracted_characters = []

    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)

        # Extract bounding box
        character_roi = thresholded[y:y+h, x:x+w]

        # Perform OCR on the character ROI
        extracted_text = pytesseract.image_to_string(
            character_roi)

        # Filter and concatenate specific characters
        extracted_characters.extend(
            [char for char in extracted_text if char in target_characters])

    extracted_string = "".join(extracted_characters)

    return extracted_string


def main():
    fasta_file = "file.fasta"  # Replace with the path to your FASTA file

    dna_sequence = ""
    with open(fasta_file, "r") as handle:
        for record in SeqIO.parse(handle, "fasta"):
            dna_sequence = str(record.seq)
    encryption_key_aes = generate_aes_key()  # 256-bit encryption key
    print("Input DNA Sequence:\n", dna_sequence)
    print("AES 256-bit Key:\n", encryption_key_aes)
    encrypted_dna_aes = aes_encrypt(dna_sequence, encryption_key_aes)
    print("Encrypted DNA Sequence:\n", encrypted_dna_aes)
    decrypted_dna_aes = aes_decrypt(encrypted_dna_aes, encryption_key_aes)
    print("Decrypted DNA Sequence:\n", decrypted_dna_aes)

    # DNA sequence Output Image used for DNA sequence Extraction and encryption
    """
    image_path = "01.jpg"
    target_characters = "ACGT"  # Example: Extract digits

    dna_sequence = extract_specific_characters(
        image_path, target_characters)
    encryption_key_aes = generate_aes_key()  # 256-bit encryption key
    print("Input DNA:\n", dna_sequence)
    print("AES 256-bit Key:\n", encryption_key_aes)
    encrypted_dna_aes = aes_encrypt(dna_sequence, encryption_key_aes)
    print("Encrypted DNA:\n", encrypted_dna_aes)
    decrypted_dna_aes = aes_decrypt(encrypted_dna_aes, encryption_key_aes)
    print("Decrypted DNA:\n", decrypted_dna_aes)
    """


if __name__ == "__main__":
    main()
