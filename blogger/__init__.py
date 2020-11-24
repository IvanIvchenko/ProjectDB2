from flask import Flask

app = Flask(__name__)
app.secret_key = 'hello_world'
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://iyjbjjgvjpgeey:df0e9b0ec6e57cd7fb651c6516b35e15d85969a147d06e1bb1a00439d2649849@ec2-34-224-229-81.compute-1.amazonaws.com:5432/d1437q7nntmqbs'

from blogger import models
from blogger import views

