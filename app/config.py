# app/config.py

ENTITY_TAGS = {
    "full_name": r"\b([A-Z][a-z]+\s[A-Z][a-z]+)\b",
    "email": r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+",
    "phone_number": r"\b\d{10}\b",
    "dob": r"\b\d{2}/\d{2}/\d{4}\b",
    "aadhar_num": r"\b\d{4}\s\d{4}\s\d{4}\b",
    "credit_debit_no": r"\b(?:\d[ -]*?){13,16}\b",
    "cvv_no": r"\b\d{3}\b",
    "expiry_no": r"\b(0[1-9]|1[0-2])\/\d{2,4}\b"
}
