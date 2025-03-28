# Flask + MongoDB Backend Template (Python 3.12)

## Installation

### 1. Clone the repository

```sh
git clone https://github.com/Axiom-208/backend.git
cd flask-mongodb-template
```

### 2. Create a virtual environment (Important)

```sh
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```
This will install all necessary dependencies, including MongoDB-related libraries.

## Running the Application

### 1. Start the Flask server with Uvicorn

```sh
uvicorn app:app --host 0.0.0.0 --port 5000 --reload
```

The server will start at `http://127.0.0.1:5000/`

### 2. Example Request

```sh
curl -X GET http://127.0.0.1:5000/
```

#### Response:

```json
{
    "status": 200,
    "success": true,
    "message": "User created",
    "data": {
        "id": 1,
        "name": "John Doe"
    }
}
```

## Folder Structure

```
/
├── app/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py  # Makes the `api` folder a package
│   │   ├── v1/  # API Version 1
│   │   │   ├── __init__.py
│   │   │   ├── router.py  # Main router for v1
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── items.py  # Item-related routes
│   │   │   │   ├── users.py  # User-related routes
│   │   ├── v2/  # API Version 2 (for future expansion)
│   │   │   ├── __init__.py
│   │   │   ├── router.py  # Main router for v2
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── orders.py  # New endpoint for orders (example)
│   │   │   │   ├── products.py  # New endpoint for products (example)
│   │   └── base_router.py  # Registers versions and API entry points
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py  # Application settings (e.g., environment variables)
│   │   ├── dependencies.py  # Centralized dependencies (e.g., database sessions, middleware)
│   ├── db/
│   │   ├── __init__.py
│   │   ├── database.py  # Beanie/MongoDB initialization
│   │   ├── mongodb_utils.py  # Helper functions for MongoDB operations
│   ├── middleware/
│   │   ├── __init__.py
│   │   ├── auth_middleware.py  # Authentication and authorization middleware
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py  # Beanie/Pydantic models for users
│   │   ├── item.py  # Beanie/Pydantic models for items
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── user.py  # Pydantic schemas for request/response validation (users)
│   │   ├── item.py  # Pydantic schemas for request/response validation (items)
│   ├── services/
│   │   ├── __init__.py
│   │   ├── user_service.py  # Business logic for user-related operations
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── helpers.py  # General utility functions (e.g., token generation, logging)
├── logs/  # Stores logs for debugging and monitoring
├── .env  # Environment variables (MongoDB URI, secrets, etc.)
├── .gitignore  # Ignored files (venv, logs, .env, etc.)
├── main.py  # Flask application entry point
├── README.md  # Project documentation
└── requirements.txt  # Dependencies for the project
```

## Environment Variables

The only required configuration for MongoDB is setting the following environment variables in a `.env` file:

```
MONGO_URI=mongodb://localhost:27017/
MONGO_DATABASE_NAME=mydatabase
```

## MongoDB Integration

No additional setup is required beyond setting the environment variables. The system will automatically connect to MongoDB using the provided values.


## Deployment

Use **Uvicorn** for production deployment:

```sh
uvicorn app:app --host 0.0.0.0 --port 5000
```

## 🚀 To-Do List

This section outlines the remaining tasks for the project.

### Backend Development
- [ ] Set up all Pydantic schemas for request validation and response modeling  
- [ ] Create API endpoints for handling various functionalities  
- [ ] Implement authentication middleware  
- [ ] Develop functions to generate authentication tokens  
- [ ] Integrate the database to store video data  

### Feature Implementation
- [ ] Implement video creation functionality  
- [ ] Integrate video creation with an API endpoint  
- [ ] Implement flashcard creation feature  
- [ ] Integrate flashcard creation with an API endpoint  

### Additional Tasks
- [ ] Add logging and test error handling  

