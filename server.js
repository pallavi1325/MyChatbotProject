const express = require("express");
const cors = require("cors");

const app = express();
const PORT = 3000;

// Middleware
app.use(express.json());
app.use(cors());

// Import routes
const chatbotRoutes = require("./routes/chatbot");
app.use("/chatbot", chatbotRoutes);

// Default route
app.get("/", (req, res) => {
    res.send("Chatbot server is running...");
});

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
