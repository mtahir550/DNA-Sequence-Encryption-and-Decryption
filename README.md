
# Requirements and Usage Instructions

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
GAGTTGCAGCAAGCGGTCCACGCTGGTTTGCCCCAGCAGGCGAAAATCCTGTTTGATGGTGGTTCCGAAATCGGCAAAATCCCTTATAAATCAAAAGAATAGCCCGAGATAGGGTTGAGTGTTGTTCCAGTTTGGAACAAGAGTCCACTATTAAAGAACGTGGACTCCAACGTCAAAGGGCGAAAAACCGTCTATCAGGGCGATGGCCACTACGTGAACCATCACCCAAATCAAGTTTTTTGG
AES 256-bit Key:
b'\x89Q\xf5B\x7f\xa0*\xbeP\xd7A\xf5\xa2T\xf2\xda\x0c\xb7r\xe4}kJ\xaf@\xbf^\xaf\x85\xee\x87\xde'
Encrypted DNA Sequence:
79ELF6eUZwx7yMIq5JegJx2Q3kqMk1ehhUkxSt02F6MaeVj9eSGRBbSjcAT9h6Dqfa/Pbbsc31fg00WVAHPCWFMbNxWZvFAA9xKG6g93tn72Rp238F48NZhHSPBTDhZksJShO245gkpEXx7SzZKPt8QP3t/bMxz5bN/Od9e0M2tUd2XGdT4fb/11Bn4g1AyEtA4O695smxbIiDRasMPKQaE9wyToMfizhxJ6hv8/IK1qxpub0buK5JbZcQLZwFc5PvFMI+kts3fYhUWAI/523oZkXKWGPPEvIZA60pUk8KaWW8BDmRNamF3TrIowIkM78xgTEAkT26Z32VrqtI6z+TwGon2DGpC4PT0hvsfyt1ikw32DtH0N1sf32G50X4Um34GGXxi3HeDx5e809yRvOS9qfqJmAnCf1lOfZ6IaACNpzn9c1u0+611JrweD++lOItSE/VhZk41Kte1PMRAelK+rBL17Rc2zV7PUwffnErntGrNG1n/e+CK2iEm/1J2cd+X+FgVp7Wod1VIpshGDufsuF7Xm94CgGYkvcBRmodQBYH+T4qHKL0uzdhzWGVuYi28kemA6C/gQzG72EOLmY6qJ1e7ND1KdAGhXKdBtaLafVzOvfNCGIMV+NeEGf/IwChUX8ttekXzdxi8pHgtyPg==
Decrypted DNA Sequence:
GAGTTGCAGCAAGCGGTCCACGCTGGTTTGCCCCAGCAGGCGAAAATCCTGTTTGATGGTGGTTCCGAAATCGGCAAAATCCCTTATAAATCAAAAGAATAGCCCGAGATAGGGTTGAGTGTTGTTCCAGTTTGGAACAAGAGTCCACTATTAAAGAACGTGGACTCCAACGTCAAAGGGCGAAAAACCGTCTATCAGGGCGATGGCCACTACGTGAACCATCACCCAAATCAAGTTTTTTGG
```

## Customization and Extension
The script is adaptable for various bioinformatics applications. Users can modify or extend the script to suit different project requirements.
