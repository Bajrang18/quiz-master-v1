document.addEventListener("DOMContentLoaded", function () {
    if (typeof quizDuration === "undefined" || quizDuration === "None") {
        console.error("Error: Quiz time duration is not available!");
        return;
    }

    let timeParts = quizDuration.split(":");  // Extract HH:MM
    let timeRemaining = parseInt(timeParts[0]) * 60 + parseInt(timeParts[1]);  // Convert to seconds

    const timerDisplay = document.getElementById("timer");
    const quizForm = document.getElementById("quizForm");

    function updateTimer() {
        let minutes = Math.floor(timeRemaining / 60);
        let seconds = timeRemaining % 60;
        timerDisplay.textContent = `${minutes}:${seconds < 10 ? "0" : ""}${seconds}`;

        if (timeRemaining <= 0) {
            clearInterval(timerInterval);
            alert("Time's up! Your quiz will be submitted automatically.");
            quizForm.submit();
        } else {
            timeRemaining--;
        }
    }

    updateTimer();
    let timerInterval = setInterval(updateTimer, 1000);
});
