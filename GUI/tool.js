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


let dt = document.getElementById('date')
let time = document.getElementById('time')
var months = ["January", "Febraury", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
var days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];

function datetime(){
  var d = new Date();
  var day = days[d.getDay()];
  var hr = d.getHours();
  if (hr===0){
    hr=12
  }
  var min = d.getMinutes();
  if (min < 10) {
      min = "0" + min;
  }
  var ampm = "AM";
  if( hr > 12 ) {
      hr -= 12;
      ampm = "PM";
  }
  var date = d.getDate();
  var month = months[d.getMonth()];
  var year = d.getFullYear();
  dt.innerHTML=date + " "+ month + ", " + year;
  time.innerHTML=day + ", " + hr + ":" + min + " " + ampm;
  }
// 

datetime()
setInterval(()=>datetime(),60000)