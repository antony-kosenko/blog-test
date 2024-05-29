 // Form submit
 function onSubmit(token) {
    document.getElementById("newCommentForm").submit();
}

function validateTextInput(text) {
  let sanitizedInput = text
    .replace(/<(?!a|code|i|strong)((\w+))>/gm,"&lt$1&gt")
    .replace(/<\/(?!a|code|i|strong)((\w+))>/gm,'&lt\/$1&gt');

  return sanitizedInput
}

function checkKeypress(elem, evt) {
  var txtBef = elem.value.slice(0, elem.selectionEnd);
  var txtAft = elem.value.slice(elem.selectionEnd, elem.value.lenth);
  var lastString = txtBef
      .replace(/\s+/g, " ")
      .split(" ");
  lastString = lastString[lastString.length - 1];
  
  if(evt.key == ">"){
      if(lastString.includes("<")){
          var addClose = lastString.replace(/[< >]/g, "");
          elem.value = txtBef+"  </"+addClose+">"+txtAft; 
          elem.selectionEnd = txtBef.length + 1;
      }
  }
}

// Sending form
const form = document.getElementById("newCommentForm");
const formElements = form.elements

async function sendData() {
  try {
    const response = await fetch(`//${window.location.host}/api/v1/comments/`, {
      method: "POST",
      headers: {
              'Accept': "application/json",
              'Content-Type': "application/json;charset=utf-8",
              // "X-CSRFToken": csrftoken
          },
      credentials: 'same-origin',
      body: JSON.stringify(
        {
          "user": {
              "email": formElements["user-email"].value,
              "username": formElements["user-username"].value,
              "homepage": formElements["user-homepage"].value
          },
          "text": validateTextInput(formElements["text"].value),
          "g-recaptcha-response": document.getElementById("g-recaptcha-response").value
          
        }
      )
    });
    if (!response.ok) {
      const text = await response.text();
			console.log(text)
      throw Error(text);
    }
  } catch (e) {
    console.error(e);
}}

// Take over form submission
form.addEventListener("submit", (event) => {
  event.preventDefault();
  sendData();
});


const iterate = (obj) => {
    Object.keys(obj).forEach(key => {

    console.log(`key: ${key}, value: ${obj[key]}`)

    if (typeof obj[key] === 'object' && obj[key] !== null) {
            iterate(obj[key])
        }
    })
}