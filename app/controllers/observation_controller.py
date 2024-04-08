import datetime
from flask import jsonify, make_response, request

def create():
  try:
    # create tables if not exists.
    db.create_all()
    db.session.commit()
    return '==================TABLES CREATED=================='
  
  except Exception as e:
    print(e)
    return '==================TABLES NOT CREATED!!!=================='

def read():
  try:
    return
  except Exception as e:
    return
    

def update():
  try:
    return
  except Exception as e:
    return
    
def delete():
  try:
    return
  except Exception as e:
    return