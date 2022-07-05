const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;


fetch("http://127.0.0.1:8000/postScore/", {
method: "POST",
headers: {'Content-Type': 'application/json'},
headers: {'X-CSRFToken': csrftoken},
body: JSON.stringify(data)
}).then(res => {
console.log("Request complete! response:", res);
});