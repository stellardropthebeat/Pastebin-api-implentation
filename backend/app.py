import sys
import json

import flask
from flask import Flask, request, jsonify
from datetime import datetime
from sqlalchemy import Column, Text, DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import declarative_base
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)
app.config["DEBUG"] = True

# Define the MariaDB engine using MariaDB Connector/Python
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:hardpass@127.0.0.1:3307/test")

Base = declarative_base()


class Paste(Base):
    __tablename__ = 'pastebin'
    id = Column(Integer, primary_key=True)
    title = Column(String(length=100))
    content = Column(Text)
    createdAt = Column(DateTime)


Base.metadata.create_all(engine)

# Create a session
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()


def addPaste(title, content, createdAt):
    newPaste = Paste(title=title, content=content, createdAt=createdAt)
    session.add(newPaste)
    session.commit()
    return newPaste.id


def selectById(Id):
    return session.query(Paste).get(Id)


def selectRecents():
    recents = session.query(Paste).order_by(Paste.id.desc()).limit(100)
    toReturn = []
    for p in recents:
        toReturn.append(({"title": p.title, "content": p.content, "createdAt": str(p.createdAt)}))
    return toReturn


@app.route('/')
def index():
    return "Hello World"


@app.route('/api/paste', methods=['POST'])
def paste():
    try:
        title = request.json["title"]
        content = request.json["content"]
        dt = datetime.now()
        toReturn = jsonify({"id": addPaste(title, content, dt)})
    except:
        toReturn = None
    if toReturn is None:
        return jsonify({"error": "No title or content"}), 400
    else:
        return toReturn, 200


@app.route('/api/<Id>', methods=["GET"])
def getId(Id):
    paste = selectById(Id)
    if paste is None:
        return '', 404
    else:
        return jsonify(
            {"title": paste.title, "content": paste.content, "createdAt": str(paste.createdAt)}
        ), 200


@app.route('/api/recents', methods=["POST"])
def getRecents():
    return json.dumps(selectRecents())


app.run()
