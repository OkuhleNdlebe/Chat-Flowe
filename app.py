from flask import Flask, request
app = Flask(__name__)

@app.route('/messaging-webhook', methods=['GET'])
def messaging_webhook():
    # Parse the query params
    mode = request.args.get("hub.mode")
    token = request.args.get("hub.verify_token")
    challenge = request.args.get("hub.challenge")

    # Check if a token and mode is in the query string of the request
    if mode and token:
        # Check the mode and token sent is correct
        if mode == "subscribe" and token == "hello":
            # Respond with the challenge token from the request
            print("WEBHOOK_VERIFIED")
            return challenge, 200
        else:
            # Respond with '403 Forbidden' if verify tokens do not match
            return 'Forbidden', 403
    else:
        return 'Bad Request', 400

if __name__ == "__main__":
    app.run(debug=True, port=80)