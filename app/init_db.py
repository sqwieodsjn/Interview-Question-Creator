from app.database import (
    create_users_table,
    create_reviews_table
)

create_users_table()
create_reviews_table()

print(
    "Database initialized successfully!"
)