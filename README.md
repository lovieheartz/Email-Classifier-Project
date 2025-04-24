# Email Classifier with PII Masking (Flask API)

This project is a complete solution to:
- Detect and mask Personally Identifiable Information (PII)
- Classify emails into categories like `Request`, `Incident`, or `Problem`
- Expose the system as a **Flask API**
- Follow clean architecture with modular code and PEP8 compliance

---

## Features

- **PII Masking**: Uses regular expressions to detect:
  - Full Name
  - Email
  - Phone Number
  - Date of Birth
  - Aadhar Number
  - Credit/Debit Card Number
  - CVV
  - Expiry Date

- **Email Classification**: Uses a trained `RandomForestClassifier` on TF-IDF features to predict email type.

- **REST API**: Accepts a raw email via POST request and returns:
  - Original input
  - List of detected entities
  - Masked email
  - Email category


# Email Classifier with PII Masking

This project:
- Detects and masks PII from emails
- Classifies email into types: Request, Incident, Problem
- Exposes a Flask API

## Run the Project locally

```bash
pip install -r requirements.txt
python train_model.py
python app.py
-Then test the api using POST method on the Running URL

On hugging face:
-https://lovieheartz-email-classifier-api.hf.space/classify
