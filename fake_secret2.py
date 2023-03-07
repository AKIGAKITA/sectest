import os

# This script contains a secret that should not be committed to version control
SECRET_KEY = "mysecretkey"

# Use the secret key in your code
def use_secret_key():
    print(f"Using secret key: {SECRET_KEY}")

# Get a secret from an environment variable
def get_secret():
    secret = os.getenv("MY_SECRET")
    if secret is None:
        print("Secret not found")
    else:
        print(f"Secret found: {secret}")

# Main function that uses the secret
def main():
    use_secret_key()
    get_secret()

if __name__ == "__main__":
    main()