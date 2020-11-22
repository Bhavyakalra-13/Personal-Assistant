// loader
let loader = document.getElementById('loader') 
setTimeout(()=>{
    loader.classList.add("hidden");
    typewriter();
},0)


// Typing effect
function typing(text){
    return text
}
let aText = typing("Welcome sir!")

    let iSpeed = 100; // time delay of print out
    let iIndex = 0; // start printing array at this posision
    let iArrLength = aText.length; // the length of the text array
    let iTextPos = 0; // initialise text position
    
    function typewriter()
    {
     let sContents =  '';
     let iRow =0;
     let destination = document.getElementById("typedtext");
     
     while ( iRow < iIndex ) {
      sContents += aText[iRow++];
     }
     destination.innerHTML = sContents + aText[iIndex].substring(0, iTextPos) + '|';
     if ( iTextPos++ == iArrLength ) {
      iTextPos = 0;
      iIndex++;
      if ( iIndex != aText.length ) {
       iArrLength = aText[iIndex].length;
       setTimeout("typewriter()", iSpeed);
      }
     } else {
      typewriter()
     }
    }
    
    
    