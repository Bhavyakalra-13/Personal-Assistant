// loader
let loader = document.getElementById("loader");
setTimeout(() => {
  loader.classList.add("hidden");
  typewriter();
}, 4000);

// Typing effect
function typing(text) {
  return text;
}
let aText = typing("Welcome sir, I am J.A.R.V.I.S!");

let iSpeed = 100; // time delay of print out
let iIndex = 0; // start printing array at this posision
let iArrLength = aText.length; // the length of the text array
let iTextPos = 0; // initialise text position

function typewriter() {
  let sContents = "";
  let iRow = 0;
  let destination = document.getElementById("typedtext");

  while (iRow < iIndex) {
    sContents += aText[iRow++];
  }
  destination.innerHTML =
    sContents + aText[iIndex].substring(0, iTextPos) + "|";
  if (iTextPos++ == iArrLength) {
    iTextPos = 0;
    iIndex++;
    if (iIndex != aText.length) {
      iArrLength = aText[iIndex].length;
      setTimeout("typewriter()", iSpeed);
    }
  } else {
    typewriter();
  }
}

// speech to text

let right = document.getElementById("right");
var speechRecognizer = new webkitSpeechRecognition();

function startConverting() {
  if ("webkitSpeechRecognition" in window) {
    speechRecognizer.continuous = true;
    speechRecognizer.interimResults = true;
    speechRecognizer.lang = "en-US";
    speechRecognizer.start();

    var finalTranscripts = "";

    speechRecognizer.onresult = function (event) {
      var interimTranscripts = "";
      for (var i = event.resultIndex; i < event.results.length; i++) {
        var transcript = event.results[i][0].transcript;
        transcript.replace("\n", "<br>");
        if (event.results[i].isFinal) {
          finalTranscripts += transcript;
        } else {
          interimTranscripts += transcript;
        }
      }
      right.innerHTML = finalTranscripts + interimTranscripts;
 
    };
    speechRecognizer.onerror = function (event) {
      console.error(event);
    };
  } else {
    alert(
      "Your browser is not supported. Please download Google chrome or Update your Google chrome!!"
    );
  }
}


// button
let button = document.getElementById("button");
let buttontext = document.getElementById("btn");
buttontext.innerHTML = "Start ";
flag = false;
function start() {
  if (flag) {
    buttontext.innerHTML = "Start ";
    flag=false;
    speechRecognizer.stop();
  } else {
    buttontext.innerHTML = "Stop ";
    flag = true;
    startConverting();
  }
}
