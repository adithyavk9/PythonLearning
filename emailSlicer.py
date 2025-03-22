#email slicer
email = input("enter your email id: ").strip()
username = email[ : email.index("@") : 1]
domain = email[email.index("@") + 1 : : 1]
print(f"Your user name is {username} and your domain is {domain}")