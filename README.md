
# DNA Sequence Manipulation and Encryption Script

## Introduction
This Python script provides advanced functionalities for DNA sequence manipulation and encryption. It's designed for bioinformatics applications requiring secure handling of DNA data and includes features for DNA sequence processing, AES encryption/decryption, and character extraction from images using OCR.

## Requirements

### Python Environment
- Python 3.x

### External Libraries
- `cryptography`: For encryption and decryption.
- `Biopython`: For parsing FASTA files.
- `OpenCV (cv2)`: For image processing.
- `pytesseract`: For Optical Character Recognition (OCR).

### Installation
Install the required libraries using pip:
```bash
pip install cryptography biopython opencv-python pytesseract
```

### Tesseract OCR
- Install Tesseract OCR from [here](https://github.com/tesseract-ocr/tesseract).
- Ensure Tesseract is added to the system path.

### Other Dependencies
- A FASTA file for DNA sequences.
- An image file for character extraction.

## Usage Instructions

### Script Setup
- Ensure the script is in a Python environment with the required libraries.
- Place the FASTA file and image for OCR in accessible locations.

### Customization
Modify the `fasta_file` and `image_path` variables to point to your specific FASTA file and image file.

### Executing the Script
Run the script with Python:
```bash
python script_name.py
```
The script performs the following:
- Parses DNA sequence from a FASTA file.
- Encrypts and decrypts the DNA sequence using AES encryption.
- Extracts characters from an image and performs encryption/decryption on the extracted sequence.

### Output
The script outputs the original, encrypted, and decrypted DNA sequences, along with the AES encryption key used.

## Note
- For accurate OCR extraction, ensure the image is clear and the characters of interest are prominent.
- The script is pre-configured for specific use cases and may require modifications for different requirements.

## Example Output
```
Input DNA Sequence:
[Original DNA Sequence from FASTA file]
AES 256-bit Key:
[Generated AES Key]
Encrypted DNA Sequence:
[Encrypted DNA Sequence]
Decrypted DNA Sequence:
[Decrypted DNA Sequence]
```

## Customization and Extension
The script is adaptable for various bioinformatics applications. Users can modify or extend the script to suit different project requirements.
