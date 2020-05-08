
var myButton = document.querySelector('button');
var myHeading = document.querySelector('h1');


function setUserName() {
  var myName = prompt('请输入你的名字。');
  if(!myName) {
    setUserName();
  } else {
    localStorage.setItem('tsname', myName);
    myHeading.innerHTML = 'Mozilla 酷毙了，' + myName;
  }
}

myButton.onclick = function() {
   setUserName();
}

if(!localStorage.getItem('tsname')) {
  setUserName();
} else {
  var storedName = localStorage.getItem('tsname');
  myHeading.textContent = 'hello，' + storedName;
}