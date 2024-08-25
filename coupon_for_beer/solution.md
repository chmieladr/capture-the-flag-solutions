# Coupon for Beer
**_Web Exploitation_** \
Difficulty: Easy

### 1. Inspect element
```js
const correctKeycode = "837412102";

function checkKeycode() {
    const keycodeInput = document.getElementById("keycodeInput").value;
    const imageContainer = document.getElementById("imageContainer");

    if (keycodeInput === correctKeycode) {
        imageContainer.classList.remove("hidden");
    } else {
        alert("Podano błędny kod. Spróbuj ponownie.");
        imageContainer.classList.add("hidden");
    }
}
```

### 2. Solution
- The page shows an image when the correct keycode is entered.
- Download it and check the model in details.
- Base64 decode.

### 3. Result
Model: `RUVfQ1RGe21ZX0Y0djB1UjFUM18zbkMwRDFuR19CM3dEMVAzazQxfQ==` \
Flag: `EE_CTF{mY_F4v0uR1T3_3nC0D1nG_B3wD1P3k41}`