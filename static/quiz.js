const quizSocket = io("/quiz");

quizSocket.on("alert", (data) => {
  // console.log(data.message);
  showAlert(data.message, data.category);
});

quizSocket.on("nextQuestion", (data) => {
  //   console.log("Next Question command");
  quizSocket.emit("nextQuestion");
});

const question = document.getElementById("question");
quizSocket.on("displayQuestion", (data) => {
  question.innerText = data["question"];
});

const answerInput = document.getElementById("answer");
answerInput.addEventListener("keypress", function (event) {
  if (event.key == "Enter") {
    document.getElementById("answerBtn").click();
  }
});

const sendAnswer = () => {
  if (answerInput.value) {
    quizSocket.emit("answer", { data: answerInput.value });
    answerInput.value = "";
  }
};

const showAlert = (message, category) => {
  const alerts = document.getElementById("alerts");

  const div = document.createElement("div");
  div.className = `alert alert-${category} alert-dismissible fade show`;
  div.setAttribute("role", "alert");

  const strong = document.createElement("strong");
  strong.textContent = message;
  div.appendChild(strong);

  const button = document.createElement("button");
  button.type = "button";
  button.id = "close-alert";
  button.className = "btn-close";
  button.setAttribute("data-bs-dismiss", "alert");
  button.setAttribute("aria-label", "Close");
  div.appendChild(button);

  alerts.appendChild(div);

  setTimeout(() => {
    document.getElementById("close-alert").click();
  }, 3000);
};

quizSocket.on("displayTable", (data) => {
  //   console.log(data[0], data[1], data[2]);
  let index = 0;
  table = document.getElementById("leaderboardtable");
  table.innerHTML = "";
  for (const team_code of data[2]) {
    index++;
    const team_name = data[1][team_code][0];
    const score = data[0][team_code];

    const tr = document.createElement("tr");

    const th = document.createElement("th");
    th.scope = "row";
    th.textContent = index;
    tr.appendChild(th);

    const td1 = document.createElement("td");
    td1.textContent = team_name;

    tr.appendChild(td1);

    const td2 = document.createElement("td");
    td2.textContent = score;
    tr.appendChild(td2);

    table.appendChild(tr);
  }
});
