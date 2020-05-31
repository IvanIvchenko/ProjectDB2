from flask import Flask

app = Flask(__name__)
app.secret_key = 'hello_world'
app.config.from_object(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://bdanikhbpqxuzr:c141409d09f88fad7a9225f8dcbd9fbc1740cb90c649a38856ba99e2f24900ef@ec2-54-86-170-8.compute-1.amazonaws.com:5432/db80h2uk7jbvk5'

from blogger import models
from blogger import views

