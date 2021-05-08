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


@app.route('/all')
def all():

    cursor.execute('SELECT * FROM movies')
    result = cursor.fetchall()
    
    return jsonify(result)

@app.route('/movie/<int:id>')
def movie(id):
    cursor.execute('SELECT * FROM movies WHERE id = ' + str(id))
    result = cursor.fetchall()
    
    if not result:
        return jsonify({"Error":"Movie Not Found"})

    return jsonify(result[0])


def create():
    data = request.json
    Title = data["Title"]
    ReleaseYear = data["ReleaseYear"]
    Score = data["Score"]


    query =f"INSERT INTO dev.movies(Title, ReleaseYear, Score) VALUE (\'{Title}\', {ReleaseYear}, {Score})"

    cursor.execute(query)
    connection.commit()
    # result = cursor.fetchall()

    return jsonify(query)
