# app/api.py

from flask import Blueprint, request, jsonify
from app.masking import mask_pii, demask_text
from app.model import classify_email
from app.utils import clean_text
from app.constants import DEFAULT_RESPONSE
from app.logger import get_logger
from app.exception import AppException

api = Blueprint("api", __name__)
logger = get_logger()


@api.route("/classify", methods=["POST"])
def classify_email_route():
    """
    Classifies and masks the email sent in JSON body.
    """
    try:
        data = request.get_json()
        email = data.get("email_body", "").strip()

        if not email:
            raise AppException("Missing email_body in request.")

        email = clean_text(email)
        masked_email, entities = mask_pii(email)
        category = classify_email(masked_email)

        return jsonify({
            "input_email_body": email,
            "list_of_masked_entities": entities,
            "masked_email": masked_email,
            "category_of_the_email": category
        })

    except AppException as ae:
        return jsonify({"error": str(ae)}), ae.status_code
    except Exception as e:
        logger.error(f"Internal server error: {str(e)}")
        return jsonify({"error": "Internal Server Error"}), 500
