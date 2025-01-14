const express = require('express');
const router = express.Router();
const fs = require('fs');

// Route to handle chatbot questions
router.post('/ask', (req, res) => {
    const userQuestion = req.body.question;

    if (!userQuestion) {
        return res.status(400).json({ error: 'Question is required' });
    }

    // Load the data.json file
    fs.readFile('data.json', 'utf8', (err, data) => {
        if (err) {
            return res.status(500).json({ error: 'Failed to read data file' });
        }

        try {
            const questionsAndAnswers = JSON.parse(data);
            let foundAnswer = null;

            // Check if the question matches any stored questions
            for (const entry of questionsAndAnswers) {
                if (entry.question.toLowerCase() === userQuestion.toLowerCase()) {
                    foundAnswer = entry.answer;
                    break;
                }
            }

            if (foundAnswer) {
                return res.json({ answer: foundAnswer });
            } else {
                return res.json({
                    answer: 'I am sorry, I cannot answer that question at the moment. Please check the documentation for more details.'
                });
            }
        } catch (e) {
            return res.status(500).json({ error: 'Failed to parse data file' });
        }
    });
});

module.exports = router;
