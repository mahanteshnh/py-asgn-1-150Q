import os


def get_user_environment():
    environment = os.environ
    return environment


# Example usage
user_environment = get_user_environment()
for key, value in user_environment.items():
    print(key, "=", value)

