from flask import Flask, request, jsonify
from app.masking import mask_pii
from app.model import classify_email
from app.utils import clean_text

app = Flask(__name__)

@app.route("/classify", methods=["POST"])
def classify_email_route():
    data = request.get_json()

    if not data or "email_body" not in data:
        return jsonify({"error": "Missing 'email_body' in request"}), 400

    email = data["email_body"]
    email = clean_text(email)
    masked_email, entities = mask_pii(email)
    category = classify_email(masked_email)

    response = {
        "input_email_body": email,
        "list_of_masked_entities": entities,
        "masked_email": masked_email,
        "category_of_the_email": category
    }

    return jsonify(response), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
