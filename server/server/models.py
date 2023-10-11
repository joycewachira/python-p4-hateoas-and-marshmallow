# Importing the necessary module from flask_sqlalchemy
from flask_sqlalchemy import SQLAlchemy

# Creating an instance of SQLAlchemy
db = SQLAlchemy()

# Defining the Newsletter class/model
class Newsletter(db.Model):
    # Specifying the name of the table
    __tablename__ = 'newsletters'
    
    # Defining the columns for the table newsletters
    id = db.Column(db.Integer, primary_key=True)  # a primary key column, which is an integer
    title = db.Column(db.String)  # a string column for the title of the newsletter
    body = db.Column(db.String)  # a string column for the body of the newsletter
    
    # a datetime column for the published_at timestamp, which has a default value of the current time
    published_at = db.Column(db.DateTime, server_default=db.func.now())
    
    # a datetime column for the edited_at timestamp, which will be updated to the current time whenever the newsletter is edited
    edited_at = db.Column(db.DateTime, onupdate=db.func.now())
    
    # A string representation of the model
    def __repr__(self):
        return f'<Newsletter {self.title}, published at {self.published_at}.>'
