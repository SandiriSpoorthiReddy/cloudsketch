document.getElementById('runButton').addEventListener('click', function() {
    // Display a loading message
    showAlert('Running hand detection, please wait...', 'info');

    // Redirect to the run hand detection route
    setTimeout(() => {
        window.location.href = '/run_hand_detection'; // Ensure this route is set up in Flask
    }, 1000); // Delay redirection to allow alert to display
});

function showAlert(message, type) {
    const alertDiv = document.getElementById('alert');
    alertDiv.innerText = message;

    // Set the alert class based on type
    if (type === 'success') {
        alertDiv.style.backgroundColor = 'rgba(76, 175, 80, 0.9)'; // Green
        alertDiv.style.color = '#fff'; // White text
    } else if (type === 'error') {
        alertDiv.style.backgroundColor = 'rgba(248, 215, 218, 0.9)'; // Red
        alertDiv.style.color = '#721c24'; // Darker text
    } else {
        alertDiv.style.backgroundColor = 'rgba(255, 193, 7, 0.9)'; // Yellow for info
        alertDiv.style.color = '#000'; // Black text
    }

    alertDiv.style.display = 'block'; // Show the alert
    setTimeout(() => {
        alertDiv.style.display = 'none'; // Hide after 3 seconds
    }, 3000); // Adjust duration as necessary
}
