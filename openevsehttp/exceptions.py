"""Exceptions."""


class AuthenticationError(Exception):
    """Exception for authentication errors."""


class OpenEVSEConnectionError(Exception):
    """Base exception for network/connection failures when talking to the charger."""


class OpenEVSETimeoutError(OpenEVSEConnectionError, TimeoutError):
    """Exception raised when a request to the charger times out.

    Also inherits from the builtin TimeoutError so existing callers that
    catch TimeoutError broadly continue to work unchanged.
    """


class ParseJSONError(Exception):
    """Exception for JSON parsing errors."""


class UnknownError(Exception):
    """Exception for Unknown errors."""


class MissingMethod(Exception):
    """Exception for missing method variable."""


class AlreadyListening(Exception):
    """Exception for already listening websocket."""


class MissingSerial(Exception):
    """Exception for missing serial number."""


class UnsupportedFeature(Exception):
    """Exception for firmware that is too old."""


class InvalidType(Exception):
    """Exception for invalid types."""
