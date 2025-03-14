# Quiz Master V1

## Overview
Quiz Master V1 is a **multi-user exam preparation web application** built using Flask. It allows users to take quizzes on various subjects and provides an admin dashboard to manage users, quizzes, and scores.

## Features
- **User Authentication:** Register, login, and logout.
- **Admin Role:** Manage subjects, chapters, quizzes, and questions.
- **User Role:** Attempt quizzes and view results.
- **Quiz Management:** Timed quizzes with multiple-choice questions.
- **Scoreboard:** Displays top-performing users.
- **Admin Reports:** View user performance and quiz statistics.

## Technologies Used
- **Backend:** Flask, Flask-SQLAlchemy, Flask-Login
- **Frontend:** Jinja2, HTML, CSS, Bootstrap
- **Database:** SQLite

## Installation
### 1. Clone the Repository
```sh
git clone https://github.com/yourusername/quiz-master-v1.git
cd quiz-master-v1
```
### 2. Set Up a Virtual Environment
```sh
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate    # Windows
```
### 3. Install Dependencies
```sh
pip install -r requirements.txt
```
### 4. Initialize the Database
```sh
python
```
Inside Python, run:
```python
from app import app, db
with app.app_context():
    db.create_all()
```
### 5. Run the Application
```sh
python app.py
```
Visit **http://127.0.0.1:5000/** in your browser.

## Project Structure
```
/quiz_master
│── /static              # CSS, images, JavaScript
│── /templates           # HTML templates
│── /models              # Database models
│── /controllers         # Business logic
│── app.py               # Main Flask application
│── forms.py             # Form validation with Flask-WTF
│── config.py            # Configuration settings
│── database.db          # SQLite database
│── requirements.txt     # Dependencies list
│── README.md            # Project documentation
```

## Usage
### Admin Role
- **Login as Admin** (predefined account)
  - Email: `admin@quizmaster.com`
  - Password: `admin123`
- Manage subjects, chapters, quizzes, and questions.
- View user performance and quiz statistics.

### User Role
- **Register/Login** as a new user.
- Choose a quiz and attempt it.
- View past scores and leaderboard rankings.

## Future Enhancements
- API support for mobile integration.
- More interactive quiz features.
- Advanced analytics for admin reports.

## License
This project is licensed under the MIT License.

---
🎯 **Project Completed!** 🚀 Happy Coding! 😊

