const socket = io();
let currentRoom = 'General';
socket.emit('join', { room: currentRoom });

function sendMessage() {
  const msg = document.getElementById('messageInput').value;
  const encrypted = encryptWithAES(msg, 'dummyKey');
  socket.emit('send_message', { room: currentRoom, msg: encrypted });
}

function switchRoom(room) {
  currentRoom = room;
  socket.emit('join', { room });
}



socket.on('message', (data) => {
  const box = document.getElementById('chatBox');
  const p = document.createElement('p');
  p.innerText = `${data.sender || 'System'}: ${decryptWithAES(data.msg, 'dummyKey')}`;
  box.appendChild(p);
});