from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')

# Create or get the database
db = client['mydatabase']  # Replace 'mydatabase' with your database name

# Create or get the collection (users)
users_collection = db['users']

# Example: Inserting a new user
new_user = {
    'username': 'example_user',
    'password': 'example_password',
    'email': 'example@example.com'
}

# Insert the new user into the collection
result = users_collection.insert_one(new_user)

# Check if the insertion was successful
if result.inserted_id:
    print("New user inserted successfully.")
else:
    print("Failed to insert new user.")
