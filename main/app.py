from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load static data (data.json)
with open('D:/MyChatbotProject/data.json', 'r') as static_file:
    static_data = json.load(static_file)

# Load scraped data (scraped_data.json)
with open('D:/MyChatbotProject/scraped_data.json', 'r') as scraped_file:
    scraped_data = json.load(scraped_file)

@app.route('/')
def home():
    return "Welcome to the Chatbot API!"

@app.route('/static-data', methods=['GET'])
def get_static_data():
    return jsonify(static_data)

@app.route('/scraped-data', methods=['GET'])
def get_scraped_data():
    return jsonify(scraped_data)

if __name__ == '__main__':
    app.run(debug=True)
