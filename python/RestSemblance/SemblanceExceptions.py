class Error(Exception):
   """Base class for other exceptions"""
   pass

class UnrecognizedURLTestCase(Error):
   """Raised when a mocked API call function uses an unknown endpoint"""
   pass