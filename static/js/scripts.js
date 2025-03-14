document.addEventListener("DOMContentLoaded", function () {
    let messages = document.querySelectorAll(".flash-message");
    messages.forEach((msg) => {
        setTimeout(() => {
            msg.style.display = "none";
        }, 3000);
    });
});
