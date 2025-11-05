// main.js

// Utility functions
function showMessage(message, type = 'info') {
    const messageDiv = document.getElementById('message');
    if (messageDiv) {
        messageDiv.textContent = message;
        messageDiv.className = `message ${type}`;
        setTimeout(() => {
            messageDiv.className = 'message';
            messageDiv.textContent = '';
        }, 5000);
    }
}

// Auto-refresh stats on index page
if (window.location.pathname === '/') {
    setInterval(() => {
        fetch('/api/stats')
            .then(response => response.json())
            .then(data => {
                // Update stats if needed
                console.log('Stats updated:', data);
            })
            .catch(error => console.error('Error updating stats:', error));
    }, 30000); // Update every 30 seconds
}

// Handle form submissions
document.addEventListener('DOMContentLoaded', () => {
    // Add any initialization code here
    console.log('Face Recognition System loaded');
});

