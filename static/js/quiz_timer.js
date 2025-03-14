document.addEventListener("DOMContentLoaded", function () {
    let timeLimit = "{{ quiz.time_duration }}".split(":");  // Get time from Flask (HH:MM)
    let timeRemaining = parseInt(timeLimit[0]) * 60 + parseInt(timeLimit[1]);  // Convert to seconds

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
    const timerInterval = setInterval(updateTimer, 1000);
});
