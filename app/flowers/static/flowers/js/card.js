let items1 = document.querySelectorAll('.slider1 .item1');
let next1 = document.getElementById('next1');
let prev1 = document.getElementById('prev1');
let active1 = Math.floor(items1.length / 2);

// Define the second slider
let items2 = document.querySelectorAll('.slider2 .item2');
let next2 = document.getElementById('next2');
let prev2 = document.getElementById('prev2');
let active2 = Math.floor(items2.length / 2);

// Define the third slider
let items3 = document.querySelectorAll('.slider3 .item3');
let next3 = document.getElementById('next3');
let prev3 = document.getElementById('prev3');
let active3 = Math.floor(items2.length / 2);

// Define the fourth slider
let items4 = document.querySelectorAll('.slider4 .item4');
let next4 = document.getElementById('next4');
let prev4 = document.getElementById('prev4');
let active4 = Math.floor(items2.length / 2);

// Define the loadShow() function
function loadShow(items, next, prev, active) {
    let stt = 0;
    items[active].style.transform = `none`;
    items[active].style.zIndex = 1;
    items[active].style.filter = 'none';
    items[active].style.opacity = 1;
    for (var i = active + 1; i < items.length; i++) {
        stt++;
        items[i].style.transform = `translateX(${120 * stt}px) scale(${1 - 0.2 * stt}) perspective(16px) rotateY(-1deg)`;
        items[i].style.zIndex = -stt;
        items[i].style.filter = 'blur(5px)';
        items[i].style.opacity = stt > 2 ? 0 : 0.6;
    }
    stt = 0;
    for (var i = active - 1; i >= 0; i--) {
        stt++;
        items[i].style.transform = `translateX(${-120 * stt}px) scale(${1 - 0.2 * stt}) perspective(16px) rotateY(1deg)`;
        items[i].style.zIndex = -stt;
        items[i].style.filter = 'blur(5px)';
        items[i].style.opacity = stt > 2 ? 0 : 0.6;
    }
}

// Call the loadShow() function for each slider
loadShow(items1, next1, prev1, active1);
loadShow(items2, next2, prev2, active2);
loadShow(items3, next3, prev3, active3);
loadShow(items4, next4, prev4, active4);

// Assign the click event handlers of the next and previous buttons for each slider
next1.onclick = function () {
    active1 = active1 + 1 < items1.length ? active1 + 1 : active1;
    loadShow(items1, next1, prev1, active1);
}
prev1.onclick = function () {
    active1 = active1 - 1 >= 0 ? active1 - 1 : active1;
    loadShow(items1, next1, prev1, active1);
}

next2.onclick = function () {
    active2 = active2 + 1 < items2.length ? active2 + 1 : active2;
    loadShow(items2, next2, prev2, active2);
}
prev2.onclick = function () {
    active2 = active2 - 1 >= 0 ? active2 - 1 : active2;
    loadShow(items2, next2, prev2, active2);
}

next3.onclick = function () {
    active3 = active3 + 1 < items3.length ? active3 + 1 : active3;
    loadShow(items3, next3, prev3, active3);
}
prev3.onclick = function () {
    active3 = active3 - 1 >= 0 ? active3 - 1 : active3;
    loadShow(items3, next3, prev3, active3);
}

next4.onclick = function () {
    active4 = active4 + 1 < items4.length ? active4 + 1 : active4;
    loadShow(items4, next4, prev4, active4);
}
prev4.onclick = function () {
    active4 = active4 - 1 >= 0 ? active4 - 1 : active4;
    loadShow(items4, next4, prev4, active4);
}
