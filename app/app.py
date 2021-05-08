from typing import List, Dict
import mysql.connector
import simplejson as json
from flask import Flask, Response, request, redirect, jsonify

app = Flask(__name__)


connection = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="123",
    database="dev"
)
cursor = connection.cursor(dictionary=True)



@app.route('/')
def index():

    return "Robert Deniro Movies API"


