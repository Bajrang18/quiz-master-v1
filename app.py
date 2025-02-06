from flask import Flask, render_template

app = Flask(__name__)

import config

import routes

if __name__ == "__main__":
    app.run(debug=True)


# # config.py
# from dotenv import load_dotenv
# import os
# from app import app

# load_dotenv()

# app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')


# # routes.py
# from flask import render_template
# from app import app

# @app.route('/')
# def index():
#     return render_template('index.html')