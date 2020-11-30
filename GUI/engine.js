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
let flag = false;


btn.addEventListener("click", function () {
  let { PythonShell } = require("python-shell");
  
  let options = {
    scriptPath:
      "F:/Python/Python project/Personal Assistante/Personal-Assistant/Assistant_Backend",
    args: [],
  };

  let pyget = new PythonShell("voice.py", options);
  pyget.on("message", function (message) {
    if (message==="None"){
      display("")
    }
    else{
    display(message)
    }
  });
  
  
  if (flag) {
    buttontext.innerHTML = "Start ";   
    flag = false;
    let terminate = new PythonShell("pid.py", options);
    terminate.on("message", function (message) {
    userchat(message)
    });
    setTimeout(()=>{
      userchat("Press start Listening")
    },2000)
  } else {
    buttontext.innerHTML = "Stop ";
    flag = true;
    let pyshell = new PythonShell("main.py", options);
    pyshell.on("message", function (message) {
    userchat(message)
  });
  
  }
});

display();
userchat();
