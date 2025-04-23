# app/exception.py


class AppException(Exception):
    """
    Custom application exception with optional status code.
    """
    def __init__(self, message="Application error", status_code=400):
        super().__init__(message)
        self.status_code = status_code
