function login() {

    var user = document.getElementById("username").value;
    var pass = document.getElementById("password").value;

    if (user === "kumar" && pass === "kumar123") {

        alert("Login Successful!");

        // Save login status
        localStorage.setItem("loggedIn", "true");

        window.location.href = "dashboard.html";

    } else {

        alert("Invalid Username or Password");

    }
}