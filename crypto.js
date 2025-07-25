// Client-side RSA/AES encryption
// RSA encryption/decryption logic
function encryptWithAES(message, aesKey) {
  return btoa(message); // replace with real AES
}

function decryptWithAES(message, aesKey) {
  return atob(message); // replace with real AES
}

const socket = io();
let currentRoom = 'General';
socket.emit('join', { room: currentRoom });

function sendMessage() {
  const msg = document.getElementById('messageInput').value;
  const encrypted = encryptWithAES(msg, 'dummyKey');
  socket.emit('send_message', { room: currentRoom, msg: encrypted });
}

socket.on('message', (data) => {
  const box = document.getElementById('chatBox');
  const p = document.createElement('p');
  p.innerText = data.sender + ': ' + decryptWithAES(data.msg, 'dummyKey');
  box.appendChild(p);
});