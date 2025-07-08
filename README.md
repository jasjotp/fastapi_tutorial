# Pydantic/FastAPI User Management System

A robust, type-safe user management system built with Python's Pydantic library, designed for seamless integration with FastAPI to create REST APIs with automatic data validation and interactive documentation.

## Overview

This project showcases a user management system that leverages Pydantic's data validation to ensure data integrity and type safety. 

## Key Features

### **Type-Safe Data Models**
- **Strict Type Validation**: All user data is validated at runtime using Pydantic's robust validation system
- **UUID-based Identification**: Each user gets a unique UUID for secure, scalable identification
- **Enum-based Role Management**: Role-based access control using Python enums for consistency

### **User Data Structure**
- **User Profiles**: Support for first name, last name, optional middle name
- **Gender Classification**: Type-safe gender enumeration
- **Multi-Role Support**: Users can have multiple roles (admin, user, student)
- **Partial Updates**: Dedicated update model for PATCH operations

### **Data Validation & Security**
- **Schema Validation**: Automatic validation of incoming data against defined schemas
- **Optional Field Handling**: Proper handling of optional fields with sensible defaults
- **Immutable Enums**: Gender and role enums prevent invalid values

## FastAPI Integration

This system is specifically designed to work with FastAPI, providing:
- **Automatic API Documentation**: Swagger/OpenAPI docs generated from Pydantic models
- **Request/Response Validation**: Automatic validation of HTTP requests and responses
- **JSON Serialization**: Native JSON conversion for API responses
- **Error Handling**: Standardized error responses with detailed validation messages

### FastAPI Compatibility
```python
from fastapi import FastAPI
from models import User, updateUser

app = FastAPI()

@app.post("/users/", response_model=User)
async def create_user(user: User):
    # Automatic validation and serialization
    return user

@app.patch("/users/{user_id}", response_model=User)
async def update_user(user_id: str, user_update: updateUser):
    # Partial updates with validation
    return updated_user
```

## Architecture

### File Structure
```
├── main.py          # Main application logic
├── models.py        # Pydantic data models and schemas
└── README.md        # This documentation
```

### Core Components

#### 1. **Enum Definitions**
```python
class Gender(str, Enum):
    male = 'male'
    female = 'female'

class Role(str, Enum):
    admin = 'admin'
    user = 'user'
    student = 'student'
```

#### 2. **User Model**
- **Primary Key**: Auto-generated UUID
- **Required Fields**: first_name, last_name, gender, roles
- **Optional Fields**: middle_name (defaults to None)
- **Validation**: Automatic type checking and data validation

#### 3. **Update Model**
- **Partial Updates**: All fields optional for PATCH operations
- **Type Safety**: Maintains validation even for partial updates
- **Clean API Design**: Separate model for update operations

## Technical Implementation

### Pydantic Integration
The system leverages Pydantic's `BaseModel` for:
- **Automatic Validation**: Runtime validation of all data
- **JSON Serialization**: Seamless conversion to/from JSON
- **IDE Support**: Full type hints for better development experience
- **Error Messages**: Clear, detailed validation error messages

### UUID Generation
```python
id: Optional[UUID] = uuid4()
```
- Automatic UUID generation for new users
- Ensures unique identification across distributed systems
- Optional typing allows for external ID assignment

### Role-Based Access Control
```python
roles: List[Role]
```
- Multiple roles per user for flexible permissions
- Enum-based validation prevents invalid role assignments
- Easily extensible for additional roles

## Usage Examples

### Creating a New User
```python
from models import User, Gender, Role

user = User(
    first_name="John",
    last_name="Doe",
    gender=Gender.male,
    roles=[Role.user, Role.student]
)
```

### Updating User Information
```python
from models import updateUser, Role

update_data = updateUser(
    first_name="Jane",
    roles=[Role.admin, Role.user]
)
```

## Future Enhancements

- **Database Integration**: SQLAlchemy models with Pydantic validation
- **Authentication**: JWT token-based authentication system
- **Audit Logging**: Track user creation and modification history
- **Advanced Validation**: Custom validators for email, phone numbers

## Learning Outcomes

This project demonstrates competencies in:
- **Pydantic Framework**: Data validation and serialization
- **Python Type System**: Type hints and validation
- **API Design Patterns**: Maintainable code architecture
- **Data Modeling**: Proper entity relationship design
---
