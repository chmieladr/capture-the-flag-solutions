#include <cstdio.h>
#include <stdlib.h>
#include <string.h>
#include <gmp.h>

// Function declarations
void process_keys(FILE *file, const char *flag);

int main(int argc, char **argv) {
    // Retrieve the FLAG environment variable
    const char *flag = getenv("FLAG");
    if (!flag) {
        puts("[!] No FLAG provided");
        return 1;
    }

    // Open the "recipients" file for reading
    FILE *file = fopen("recipients", "r");
    if (!file) {
        puts("[!] RSA public keys are unreadable");
        return 2;
    }

    // Process the keys and perform encryption
    process_keys(file, flag);

    // Close the file
    fclose(file);
    return 0;
}

void process_keys(FILE *file, const char *flag) {
    // GMP variables for encryption
    mpz_t ciphertext, plaintext, n, e, kid;

    // Initialize GMP variables
    mpz_inits(ciphertext, plaintext, n, e, NULL);
    mpz_init(kid);

    // RSA exponent (public exponent, commonly 65537)
    const char *EXP = "65537";

    // Process each line in the file
    while (!feof(file)) {
        if (mpz_inp_str(kid, file, 0) && mpz_inp_str(n, file, 0)) {
            // Set exponent and import plaintext
            mpz_set_str(e, EXP, 10);
            mpz_import(plaintext, strlen(flag), 1, 1, 1, 0, flag);

            // Perform encryption: ciphertext = plaintext^e mod n
            mpz_powm(ciphertext, plaintext, e, n);

            // Print results
            printf("[*] kid = %s\n", mpz_get_str(NULL, 10, kid));
            printf("[*] mod = %s\n", mpz_get_str(NULL, 10, n));
            printf("[*] enc = %s\n", mpz_get_str(NULL, 10, ciphertext));
            putchar('\n');
        }
    }

    // Clear GMP variables
    mpz_clears(ciphertext, plaintext, n, e, NULL);
    mpz_clear(kid);
}