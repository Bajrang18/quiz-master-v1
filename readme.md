# Quiz Master V1  

## 📖 Project Overview  
Quiz Master V1 is a **Flask-based quiz management system** that allows **admins** to create quizzes, add questions, and manage users, while **students** can take quizzes and view their scores.  

## 🏗️ Project Structure  

/quiz_master /templates # HTML templates /admin # Admin panel pages /user # User dashboard & quiz pages /controllers # Flask blueprints (routes) /static # CSS, JavaScript, images /css # Stylesheets /js # JavaScript files /images # Image assets /models # Database models app.py # Main Flask application config.py # Configuration settings requirements.txt # Project dependencies README.md # Project documentation


## 🚀 Features  
### **🔹 Admin Panel**
- Manage **Subjects, Chapters, Quizzes, and Questions**
- View & Delete **Users**
- Quiz **CRUD Operations**
- Secure **Admin Login**  

### **🔹 User Dashboard**
- Take **Quizzes**
- View **Quiz Scores**
- Secure **User Authentication**  

### **🔹 Additional Features**
- **Form Validation** (Frontend & Backend)
- **Quiz Timer** (Auto-submit when time runs out)
- **Chart.js Integration** (Visualize quiz scores)

---

## 🛠️ Installation & Setup  

### **1️⃣ Install Dependencies**  
Make sure you have **Python 3+** installed, then run:  
```bash
pip install -r requirements.txt

📌 Usage Guide
1️⃣ Admin Panel
Login as Admin (http://127.0.0.1:5000/login)
Create Subjects → Add Chapters → Add Quizzes → Add Questions
Manage Users & View Scores

📌 Technologies Used
✅ Backend: Flask, Flask-SQLAlchemy, Flask-Login, Flask-WTF
✅ Database: SQLite
✅ Frontend: HTML, CSS, Bootstrap
✅ JavaScript: Chart.js, Quiz Timer

👨‍💻 Author
Developed by Bajrang Kumar