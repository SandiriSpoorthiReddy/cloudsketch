document.addEventListener('mousemove', function(e) {
    const mouseX = e.clientX;
    const mouseY = e.clientY;

    // Get the width and height of the window
    const width = window.innerWidth;
    const height = window.innerHeight;

    // Calculate a lighter shade of gray based on the mouse position
    const gray = Math.round((mouseY / height) * 255); // Change intensity based on vertical position
    const lightGray = Math.round(gray * 0.6); // Make it lighter by reducing the intensity

    // Define baby blue color
    const babyBlue = `rgb(137, 207, 240)`; // Baby blue color

    // Define gray color
    const gradientGray = `rgb(${lightGray}, ${lightGray}, ${lightGray})`; // Lighter gray based on mouse position

    // Set the background to a gradient
    document.body.style.background = `linear-gradient(135deg, ${lightGray}, ${gradientGray})`; // Gradient from baby blue to gray
});

// Add hover interaction to input fields
const inputs = document.querySelectorAll('.input-field input');
inputs.forEach(input => {
    input.addEventListener('mouseenter', () => {
        input.style.borderColor = '#007bff'; // Change border color on hover to a blue shade
    });

    input.addEventListener('mouseleave', () => {
        input.style.borderColor = '#ccc'; // Reset border color
    });
});
