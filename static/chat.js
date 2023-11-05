const chatSocket = io("/chat");

const messageChatInput = document.getElementById("messageChat");
messageChatInput.addEventListener("keypress", function (event) {
  if (event.key == "Enter") {
    document.getElementById("messageChatBtn").click();
  }
});

const messageChatBody = document.getElementById("messagesChat");
const createChatMessage = (name, msg) => {
  div = document.createElement("div");
  div.classList = "text";
  span = document.createElement("span");
  strong = document.createElement("strong");
  strong.innerText = name;
  text = document.createTextNode(` : ${msg}`);

  span.appendChild(strong);
  span.appendChild(text);
  div.appendChild(span);
  messageChatBody.appendChild(div);
  messageChatBody.scrollTop = messageChatBody.scrollHeight;
  console.log(name, msg);
};

const sendChatMessage = () => {
  if (messageChatInput.value) {
    chatSocket.emit("message", { data: messageChatInput.value });
    messageChatInput.value = "";
  }
};

chatSocket.on("message", (data) => {
  createChatMessage(data.name, data.message);
});

chatSocket.on("connect", () => {
  // console.log("Connected");
});
