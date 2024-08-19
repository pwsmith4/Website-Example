# Simple React + Django Website

This project is a simple website that demonstrates the integration of a React.js frontend with a Django backend. It showcases the use of React components and Django API endpoints.

## Project Structure

The project consists of two main parts:

1. Frontend: A React.js application
2. Backend: A Django application serving API endpoints

### Frontend

The frontend is built with React.js and demonstrates the use of components. It includes a simple web page that interacts with the backend API.

### Backend

The Django backend provides at least two API endpoints for the frontend to consume.

## Setup and Installation

### Prerequisites

- Node.js and npm
- Python 3.x
- pip

### Frontend Setup

1. Navigate to the frontend directory:
   cd frontend

2. Install dependencies:
   npm install

3. Start the development server:
   npm start

The frontend will be available at http://localhost:3000.

### Backend Setup

1. Navigate to the backend directory:
   cd backend

2. Create a virtual environment:
   python -m venv venv

3. Activate the virtual environment:
   - On Windows: venv\Scripts\activate
   - On macOS and Linux: source venv/bin/activate

4. Install dependencies:
   pip install -r requirements.txt

5. Run migrations:
   python manage.py migrate

6. Start the Django development server:
   python manage.py runserver

The backend will be available at http://localhost:8000.

