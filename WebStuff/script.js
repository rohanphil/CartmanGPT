const chatForm = document.querySelector('#chat-form');
const messageInput = document.querySelector('#message-input');
const textBubble = document.querySelector('.text-bubble');

chatForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const message = messageInput.value;
  messageInput.value = '';
  sendMessage(message);
});

async function sendMessage(message) {
  const response = await fetch('/chatbot', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ query: message })
  });
  const data = await response.json();
  const botMessage = data.message;
  showResponse(message, botMessage);
}

function showResponse(userMessage, botMessage) {
  const userMessageElement = document.createElement('p');
  userMessageElement.classList.add('user-message');
  userMessageElement.innerHTML = userMessage;
  textBubble.appendChild(userMessageElement);

  const botMessageElement = document.createElement('p');
  botMessageElement.classList.add('bot-message');
  botMessageElement.innerHTML = botMessage;
  
  // remove the previous bot response, if any
  const prevBotMessageElement = document.querySelector('.bot-message');
  const prevUserMessageElement = document.querySelector('.user-message');
  if (prevBotMessageElement) {
    prevBotMessageElement.remove();
    prevUserMessageElement.remove();
  }

  textBubble.appendChild(botMessageElement);
}


// function showResponse(userMessage, botMessage) {
//   const userMessageElement = document.createElement('p');
//   userMessageElement.classList.add('user-message');
//   userMessageElement.innerHTML = userMessage;
//   textBubble.appendChild(userMessageElement);

//   const botMessageElement = document.createElement('p');
//   botMessageElement.classList.add('bot-message');
//   botMessageElement.innerHTML = botMessage;
//   textBubble.appendChild(botMessageElement);
// }
