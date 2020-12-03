document.body.addEventListener('mouseover', clickAlert)
var clicks = 0
function clickAlert(){
    colors = ['red', 'green', 'blue']
    document.body.style.backgroundColor = colors[clicks % 3];
    clicks++;
}