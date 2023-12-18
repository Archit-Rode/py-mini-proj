import tkinter as tk

import Tokenize


def createEncryptionWindow():
    def disp_encrypt():
        text_to_encrypt = message_text.get(1.0, "end-1c")
        encrypted_text, encryption_key = Tokenize.encrypt_message(text_to_encrypt)
        message_text.destroy()
        encrypt_button.destroy()
        message_text_label.destroy()
        encrypted_text_label = tk.Label(EncryptWindow, text="Encrypted Text")
        encrypted_text_label.pack()
        encrypted_text = tk.Label(EncryptWindow, text=encrypted_text)
        encrypted_text.pack()
        encryption_key_label = tk.Label(EncryptWindow, text="Encryption Key")
        encryption_key_label.pack()
        encryption_key_text = tk.Label(EncryptWindow, text=encryption_key)
        encryption_key_text.pack()

    EncryptWindow = tk.Tk()
    EncryptWindow.geometry("1000x1000")
    message_text = tk.Text()
    encrypt_button = tk.Button(text="Encrypt Text", command=disp_encrypt)
    message_text_label = tk.Label(EncryptWindow, text="Enter the plaintext")
    message_text_label.pack()
    message_text.pack()
    encrypt_button.pack()
    EncryptWindow.mainloop()


def createDecryptionWindow():
    def disp_decrypt():
        encryptedMessage = encrypted_textbox.get(1.0, "end-1c")
        encryptionKey = encryption_key_textbox.get(1.0, "end-1c")
        decryptedMessage = Tokenize.decrypt_message(encryptedMessage, encryptionKey)
        encrypted_text_label.destroy()
        encrypted_textbox.destroy()
        encryption_key_label.destroy()
        encryption_key_textbox.destroy()
        decrypt_button.destroy()
        decrypted_message_label = tk.Label(DecryptWindow, text=decryptedMessage)
        message_text_label = tk.Label(DecryptWindow, text="Plaintext")
        message_text_label.pack()
        decrypted_message_label.pack()

    DecryptWindow = tk.Tk()
    DecryptWindow.geometry("1000x1000")
    encrypted_text_label = tk.Label(DecryptWindow, text="Encrypted Text")
    encrypted_text_label.pack()
    encrypted_textbox = tk.Text()
    encrypted_textbox.pack()
    encryption_key_label = tk.Label(DecryptWindow, text="Encryption Key")
    encryption_key_label.pack()
    encryption_key_textbox = tk.Text()
    encryption_key_textbox.pack()
    decrypt_button = tk.Button(text="Decrypt Text", command=disp_decrypt)
    decrypt_button.pack()
    DecryptWindow.mainloop()
