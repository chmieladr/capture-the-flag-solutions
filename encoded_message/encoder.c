#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void* encode(const char* input) {
    size_t length = strlen(input);

    char* result = malloc(length + 1);

    for (size_t i = 0; i < length; i++) {
        result[i] = input[length - i - 1];
    }
    result[length] = '\0';

    const int16_t transform_value = length % 12 * 0x2a2 / 0x11d + 0x113 & 0x1f;

    for (size_t i = 0; i < length; i++) {
        int16_t new_value;

        if (i & 1 != 0)
            new_value = (unsigned char)result[i] - transform_value;
        else
            new_value = (unsigned char)result[i] + transform_value;

        if (new_value < 0 || new_value > 0xff) {
            printf("Invalid character: %d\n", result[i]);
            return NULL;
        }

        result[i] = (char)new_value;
    }

    return result;
}

int main() {
    FILE* fp = fopen("../encoded_message/outputMessage", "w");

    if (fp == NULL) {
        fwrite("Error: Could not open file for writing.\n", 1, 48, stderr);
        return 1;
    }

    char input[0x202] = {0};

    printf("Enter a string to encode: ");

    fgets(input, 0x202, stdin);

    input[strcspn(input, "\n")] = '\0';

    puts(input);

    char* encoded = encode(input);

    if (encoded == NULL) {
        return 1;
    }

    fwrite(encoded, strlen(input) + 1, 1, fp);

    puts("String encoded and written to outputMessage.");

    fclose(fp);
    free(encoded);
    return 0;
}