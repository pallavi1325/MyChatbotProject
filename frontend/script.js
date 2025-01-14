// Function to handle sending messages
function sendMessage() {
    const userInput = document.getElementById("user-input").value;

    if (userInput.trim() === "") {
        alert("Please enter a question!");
        return;
    }

    // Display the user's message in the chat
    displayMessage(userInput, "user-message");

    // Send the user's input to the backend server (API)
    fetch("http://localhost:3000/chatbot/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ question: userInput }),
    })
        .then((response) => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then((data) => {
            // Display the chatbot's response
            displayMessage(data.answer, "bot-message");
        })
        .catch((error) => {
            console.error("Error:", error);
        });

    // Clear the input field
    document.getElementById("user-input").value = "";
}

// Function to display messages in the chat box
function displayMessage(message, type) {
    const chatBox = document.getElementById("chat-box");
    const messageDiv = document.createElement("div");
    messageDiv.classList.add("chat-message", type);
    messageDiv.innerHTML = `<p>${message}</p>`;
    chatBox.appendChild(messageDiv);

    // Scroll to the bottom of the chat box
    chatBox.scrollTop = chatBox.scrollHeight;
}
