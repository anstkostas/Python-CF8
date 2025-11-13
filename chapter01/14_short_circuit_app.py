username = input("Please enter your username: ")

email = input("Please enter your email: ")

valid_user = username or "User"

# temp_email = (email and f"your email is {email}") or "please provide your email"
# print("temp_email: " + temp_email)
print(f"Hello {valid_user}" + ((email and f"your email is {email}") or ", please provide your email"))