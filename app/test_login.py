from auth import verify_user

result = verify_user(
    "devu@gmail.com",
    "wrongpassword"
)
print(result)