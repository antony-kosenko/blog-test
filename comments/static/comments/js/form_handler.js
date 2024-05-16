 // Form submit
 function onSubmit(token) {
    document.getElementById("newCommentForm").submit();
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
