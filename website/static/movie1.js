
                   
/* Get the element you want displayed in fullscreen */ 
var elem = document.getElementById("myvideo").value;


// function openFullscreen() {
//     if (elem.requestFullscreen) {
//       elem.requestFullscreen();
//     } else if (elem.webkitRequestFullscreen) { /* Safari */
//       elem.webkitRequestFullscreen();
//     } else if (elem.msRequestFullscreen) { /* IE11 */
//       elem.msRequestFullscreen();
//     }
//   }

var abc = document.getElementById("myvideo1").value;
function pass(){
    console.log(abc);
    if (abc.requestFullscreen) {
        abc.requestFullscreen();
    }}