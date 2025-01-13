#include <stdio.h>
#include <gmp.h>
#include <stdlib.h>
#include <string.h>

void initialize_gmp_vars(mpz_t* vars, size_t count) {
    for (size_t i = 0; i < count; ++i) {
        mpz_init(vars[i]);
    }
}

void clear_gmp_vars(mpz_t* vars, size_t count) {
    for (size_t i = 0; i < count; ++i) {
        mpz_clear(vars[i]);
    }
}

int main(int argc, char** argv) {
    FILE* file = fopen("secret", "r");
    if (!file) {
        puts("[!] RSA secret key is unreadable...");
        return EXIT_FAILURE;
    }

    // Initialize GMP variables
    mpz_t ciphertext, plaintext, n, d, e;
    mpz_t vars[5] = {ciphertext, plaintext, n, d, e};
    initialize_gmp_vars(vars, 5);

    // Read RSA values from file
    if (mpz_inp_str(n, file, 0) == 0 || mpz_inp_str(d, file, 0) == 0 || mpz_inp_str(e, file, 0) == 0) {
        puts("[!] Error reading RSA values from file.");
        clear_gmp_vars(vars, 5);
        fclose(file);
        return EXIT_FAILURE;
    }

    // Decrypt the ciphertext
    mpz_powm(plaintext, ciphertext, d, n);

    // Convert plaintext to string and print
    char* decrypted_message = mpz_get_str(NULL, 10, plaintext);
    if (decrypted_message) {
        printf("[*] msg = %s\n", decrypted_message);
        free(decrypted_message);
    } else {
        puts("[!] Error converting plaintext to string.");
    }

    // Clean up
    clear_gmp_vars(vars, 5);
    fclose(file);

    return EXIT_SUCCESS;
}