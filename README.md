# Securechatapp-e2ee-Project
Project-- Secure Chat App with End-to-End Encryption


# Secure Chat App with End-to-End Encryption (E2EE)

This project is a real-time secure messaging app built with **Python (Flask-SocketIO)** and **JavaScript (CryptoJS)** that enables **end-to-end encrypted (E2EE)** conversations similar to chat app.

Only the clients can decrypt messages — the server just routes encrypted data, ensuring maximum privacy.

---

## Summary

**Project Name**: Secure Chat App with E2EE  
**Developed Using**: Python, Flask-SocketIO, HTML/CSS/JS  
**Encryption**: AES (for message encryption), RSA (for secure key exchange)  
**Purpose**: To build a secure real-time communication tool where privacy is guaranteed by strong encryption.

---

##  Key Features

-  **End-to-End Encryption (E2EE)**:  
  Messages are encrypted in the browser before being sent — even the server can't see the content.

-  **Real-time Communication**:  
  Built using Flask + Flask-SocketIO for fast, responsive messaging.

-  **RSA + AES Hybrid Encryption**:  
  - AES (symmetric) encrypts the actual message  
  - RSA (asymmetric) encrypts the AES key securely between users

-  **User Authentication**:  
  Simple login/register system with optional public key storage.

-  **Frontend Encryption**:  
  Done using **CryptoJS** (AES) in browser, RSA public key handling in JS.

-  **Encrypted Chat Logs**:  
  Optionally save encrypted messages for future retrieval.

---

##  Tech Stack

| Layer        | Tools Used                         |
|--------------|------------------------------------|
| Frontend     | HTML, CSS, JavaScript, CryptoJS    |
| Backend      | Python, Flask, Flask-SocketIO      |
| Encryption   | AES (symmetric) + RSA (asymmetric) |
| Others       | Jinja2 Templates, JSON             |

---

##  Project Folder Structure 

securechate2ee/
├── app.py # Flask application entry
├── requirements.txt # Python dependencies
├── templates/
│ └── chat.html # HTML frontend
├── static/
│ └── chat.js # JS with AES encryption logic
├── encryption/
│ └── crypto_utils.py # RSA/AES logic in Python
└── chat_logs/ (optional) # Encrypted logs storage

