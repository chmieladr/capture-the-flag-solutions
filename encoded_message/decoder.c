#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* decode(const char* input) {
    size_t length = strlen(input);
    char* result = malloc(length + 1);

    int16_t transform_value = length % 12 * 0x2a2 / 0x11d + 0x113 & 0x1f;

    for (size_t i = 0; i < length; i++) {
        int16_t new_value;

        if (i % 2 != 0) {
            new_value = (unsigned char)input[i] + transform_value;
        } else {
            new_value = (unsigned char)input[i] - transform_value;
        }

        result[i] = (char)new_value;
    }

    result[length] = '\0';

    for (size_t i = 0; i < length / 2; i++) {
        char temp = result[i];
        result[i] = result[length - i - 1];
        result[length - i - 1] = temp;
    }

    return result;
}

int main() {
    FILE* file = fopen("../encoded_message/encodedMessage", "r");
    if (file == NULL) {
        fwrite("Failed to open file.", 1, 48, stderr);
        return 1;
    }

    char buffer[512];
    if (fgets(buffer, sizeof(buffer), file) == NULL) {
        fwrite("Failed to read from file.", 1, 48, stderr);
        fclose(file);
        return 1;
    }

    fclose(file);

    buffer[strcspn(buffer, "\n")] = '\0';
    char* decoded = decode(buffer);
    printf("Decoded message: %s\n", decoded);

    free(decoded);
    return 0;
}