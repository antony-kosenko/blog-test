 // Form submit
 function onSubmit(token) {
    document.getElementById("newCommentForm").submit();
}

// Sending form
const form = document.getElementById("newCommentForm");
const formElements = form.elements
// let csrftoken = getCookie('csrftoken');

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
        "text": formElements["text"].value,
        "g-recaptcha-response": document.getElementById("g-recaptcha-response").value
        
      }
    )
  });
  } catch (e) {
    console.error(e);
}
}

// Take over form submission
form.addEventListener("submit", (event) => {
event.preventDefault();
sendData();
});


// Getting Cookies

// function getCookie(name) {
// var cookieValue = null;
// if (document.cookie && document.cookie !== '') {
//   var cookies = document.cookie.split(';');
//   for (var i = 0; i < cookies.length; i++) {
//       var cookie = cookies[i].trim();
//       if (cookie.substring(0, name.length + 1) === (name + '=')) {
//           cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//           break;
//       }
//   }
// }
// return cookieValue;
// }