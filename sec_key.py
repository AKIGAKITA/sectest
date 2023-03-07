# This test file contains a sample API key
# Do not use this key in production code!
API_KEY = 'sk_test_1234567890'

def test_api_key():
    # This test checks if the API key is valid
    assert API_KEY.startswith('sk_'), "Invalid API key"
