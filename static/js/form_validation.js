document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("registerForm");

    form.addEventListener("submit", function (event) {
        let isValid = true;

        // Validate Email
        const username = document.getElementById("username");
        const usernameError = document.getElementById("usernameError");
        if (!username.value.includes("@")) {
            usernameError.textContent = "Enter a valid email address.";
            isValid = false;
        } else {
            usernameError.textContent = "";
        }

        // Validate Password
        const password = document.getElementById("password");
        const passwordError = document.getElementById("passwordError");
        if (password.value.length < 6) {
            passwordError.textContent = "Password must be at least 6 characters.";
            isValid = false;
        } else {
            passwordError.textContent = "";
        }

        // Validate Full Name
        const fullName = document.getElementById("full_name");
        const fullNameError = document.getElementById("fullNameError");
        if (fullName.value.trim() === "") {
            fullNameError.textContent = "Full Name is required.";
            isValid = false;
        } else {
            fullNameError.textContent = "";
        }

        // Validate DOB
        const dob = document.getElementById("dob");
        const dobError = document.getElementById("dobError");
        if (!dob.value) {
            dobError.textContent = "Date of Birth is required.";
            isValid = false;
        } else {
            dobError.textContent = "";
        }

        // Prevent form submission if validation fails
        if (!isValid) {
            event.preventDefault();
        }
    });
});
