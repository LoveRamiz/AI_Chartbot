from flask import Flask, render_template, request, jsonify
import ollama

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')

    try:
        # Send the user's input to tinyllama model
        response = ollama.chat(
            model="tinyllama",
            messages=[{"role": "user", "content": user_input}]
        )

        # Extract the AI's reply
        if 'message' in response and 'content' in response['message']:
            ai_reply = response['message']['content']
            
            # Custom reply for specific question
            if "who made you" in user_input.lower():
                ai_reply = "I was created by Love Ramiz, a BCA student specializing in AI & Machine Learning."

            return jsonify({'reply': ai_reply})
        else:
            return jsonify({'reply': "Sorry, I couldn't understand the model response."})

    except Exception as e:
        return jsonify({'reply': f"Error: {str(e)}"})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)