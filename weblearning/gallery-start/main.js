const displayedImage = document.querySelector('.displayed-img');
const thumbBar = document.querySelector('.thumb-bar');

const btn = document.querySelector('button');
const overlay = document.querySelector('.overlay');


/* Looping through images */
for (var i=0; i<5; ++i){
    const newImage = document.createElement('img');
    newImage.setAttribute('src', 'images/pic' + (i + 1) + '.jpg');
    thumbBar.appendChild(newImage);
}


thumbBar.onclick = function (e) {
    displayedImage.setAttribute('src', e.target.getAttribute('src'))
}


/* Wiring up the Darken/Lighten button */
btn.onclick = function () {
    if (btn.getAttribute('class') === 'dark') {
        btn.setAttribute('class', 'light');
        overlay.style.backgroundColor = 'rgba(0, 0, 0, 0.5)';
    } else {
        btn.setAttribute('class', 'dark');
        overlay.style.backgroundColor = 'rgba(0, 0, 0, 0)'
    }
}
