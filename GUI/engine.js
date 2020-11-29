const remote = require("electron").remote;

function userchat(text = "Listening....") {
  let box = document.getElementById("left");
  box.innerHTML = text;
}
function display(text = "Say Something!!!") {
  let box = document.getElementById("right");
  box.innerHTML = text;
}
let btn = document.getElementById("button");

let buttontext = document.getElementById("btn");
buttontext.innerHTML = "Start ";
flag = false;
btn.addEventListener("click", function () {
if (flag) {
  buttontext.innerHTML = "Start ";
  flag = false;
} else {
  buttontext.innerHTML = "Stop ";
  flag = true;
}


  let { PythonShell } = require("python-shell");
  let options = {
    scriptPath:
      "F:/Python/Python project/Personal Assistante/Personal-Assistant/Assistant_Backend",
    args: [],
  };
  let pyshell = new PythonShell("main.py", options);
  pyshell.on("message", function (message) {
    userchat(message)
  });
});

display();
userchat();
