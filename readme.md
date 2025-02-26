# Secure Data Hiding in Images Using Steganography

This project allows you to hide secret messages within an image using encryption and later retrieve the hidden message with decryption. It’s a simple implementation of steganography using Python and OpenCV.

---

## 🛠️ **Technologies Used:**
- Python
- OpenCV
- Tkinter (for file dialog)

---

## 📂 **File Structure:**
- `encryption.py` — Encrypts a secret message into an image.
- `decryption.py` — Decrypts and reveals the hidden message from the encrypted image.

---

## ⚡ **Setup Instructions:**

1. **Install Dependencies:**
```bash
pip install opencv-python
```

2. **Run the Encryption Script:**
```bash
python encryption.py
```
- Select an image file (.jpg, .png, .jpeg).
- Enter your secret message and set a passcode.
- The encrypted image will be saved as `encryptedImage.jpg` in the same directory.

3. **Run the Decryption Script:**
```bash
python decryption.py
```
- Select the encrypted image.
- Enter the passcode to decrypt and view the hidden message.

---

## 🔑 **Encryption Process:**
- The script encodes the message into image pixels using ASCII values.
- The pixel values are modified, embedding the message without noticeable changes to the image.

## 🧠 **Decryption Process:**
- The decryption script retrieves the hidden message by reading pixel values.
- The correct passcode is required to access the message.

---

## 🚀 **Future Improvements:**
- Support for longer messages with custom encoding techniques.
- Add error handling for large images or excessive message lengths.
- Implement image quality preservation and metadata handling.

---

## 📩 **Contributing:**
Feel free to contribute by opening issues or submitting pull requests!

Happy coding! 🚀✨

