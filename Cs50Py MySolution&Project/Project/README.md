    # Project on Encryption
    #### Video Demo:  https://www.youtube.com/live/KhFR0JQ-x5U
    #### Description:
    Python packages: pycryptodome

    This project is a Python-based line application designed to securely encrypt files using AES (Advanced Encryption Standard) or RSA (Rivest-Shamir-Adleman) encryption methods, combined with SHA-3 hashing to ensure file integrity. This project also includes a suite of automated tests using pytest to validate its functionality.

    Here's how it works:
        File Input: The user starts by providing the path to the file they wish to encrypt. This could be any file on their system.

        Choosing an Encryption Method: The program prompts the user to choose between AES and RSA for encryption.

        AES: If the user opts for AES, the program generates a random 32-byte key and uses it to encrypt the file in CBC (Cipher Block Chaining) mode. The encrypted output is saved with a .enc extension.

        RSA: If RSA is chosen, the program checks for existing RSA keys. If they aren’t found, it generates a new pair (public and private keys). The public key is used to encrypt the file, and, similar to AES, the result is saved with a .enc extension.

        Hashing the Original File: After the encryption process, the program computes a SHA-3-256 hash of the original file. This hash serves as a digital fingerprint, allowing the user to verify that the file hasn’t been altered.

        Output: The program creates two new files: the encrypted file and the hash file, both stored in the same directory as the original file (plus the two keys if they don't already exist).

        Key Features:

            Key generation: Utilizes a 256-bit random key generated with get_random_bytes.
            Padding: Applies PKCS7 padding to ensure the plaintext aligns with AES block size requirements.
            Key management: Checks for existing RSA key pairs (public.pem, private.pem). If absent, it generates a new 2048-bit RSA key pair and stores them securely.

            Encryption Process: Utilizes the public key to encrypt the file.
        Hash:

            Reads the file's binary data and computes its SHA-3-256 hash. Saved in a .hash file for future integrity checks.

        Automated Tests with Pytest:

            Ensures the reliability and correctness of the encryption and hashing functionalities.

            Verifies that the AES and RSA encrypted files are created successfully.

            Confirms the generation of RSA keys and hash files; the hash file is generated after encryption to ensure integrity.

            Removes generated files after each test to maintain a clean testing environment.
