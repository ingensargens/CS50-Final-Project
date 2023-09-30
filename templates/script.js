// Get the switch element
const toggleSwitch = document.getElementById('toggleSwitch');

// Function to toggle dark mode
function toggleDarkMode() {
    if (toggleSwitch.checked) {
        // Enable dark mode
        document.body.classList.add('dark-mode');
    } else {
        // Disable dark mode
        document.body.classList.remove('dark-mode');
    }
}

// Listen for the switch change event
toggleSwitch.addEventListener('change', toggleDarkMode);
