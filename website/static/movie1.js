
                   
/* Get the element you want displayed in fullscreen */ 

var elem = document.getElementById("myvideo" );

/* Function to open fullscreen mode */
function openFullscreen() {
    if (elem.requestFullscreen) {
    elem.requestFullscreen();
    } else if (elem.webkitRequestFullscreen) { /* Safari */
    elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) { /* IE11 */
    elem.msRequestFullscreen();
    }
}
