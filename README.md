
# MongoDB Connection Test

This repository contains code for testing the connection to a MongoDB database using Python with Flask framework. The code includes a simple Flask web application with login, registration, and profile functionalities, as well as MongoDB connection setup.

## MongoDB Setup

To run the code, you need to have MongoDB installed on your system. You can download and install MongoDB from the [official website](https://www.mongodb.com/try/download/community).

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/your_username/mongodb-connection-test.git
    ```

2. Navigate to the project directory:

    ```bash
    cd mongodb-connection-test
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Ensure MongoDB is running on your local machine.

2. Run the Flask application:

    ```bash
    python app.py
    ```

3. Open your web browser and go to [http://localhost:5000](http://localhost:5000) to access the application.

## MongoDB Connection

In the `app.py` file, the MongoDB connection is established using the `MongoClient` class from the `pymongo` package. The following line of code initializes the MongoDB client with the default host (`localhost`) and port (`27017`):

```python
client = MongoClient('mongodb://localhost:27017/')
```

Here, `'mongodb://localhost:27017/'` indicates that the MongoDB server is running locally on the default port `27017`.

## About MongoDB

MongoDB is a popular NoSQL database program that uses JSON-like documents with optional schemas. It is known for its flexibility, scalability, and performance. MongoDB is widely used in modern web applications for storing and managing data.

## Contributors
Sekandari Hamidreza

