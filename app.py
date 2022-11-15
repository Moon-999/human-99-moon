# -*- coding: utf-8 -*-

from flask import Flask, request
import pandas as pd 
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.sql import text 
import json

## DB 연결 Local
def db_create():
    # 로컬
	# engine = create_engine("postgresql://postgres:1234@localhost:5432/chatbot", echo = False)
		
	# Heroku
    
    engine = create_engine("postgresql://qxqcovcxobgrzr:136d1a4ee21d7d53fefe41723c82cadb3a41edd4203ef9b4759b8ecb1daf68a7@ec2-107-23-76-12.compute-1.amazonaws.com:5432/d7477vdhmjaq31", echo = False)

    engine.connect()
    engine.execute("""
        CREATE TABLE IF NOT EXISTS iris(
            sepal_length FLOAT NOT NULL,
            sepal_width FLOAT NOT NULL,
            pepal_length FLOAT NOT NULL,
            pepal_width FLOAT NOT NULL,
            species VARCHAR(100) NOT NULL
        );"""
    )
    data = pd.read_csv('data/iris.csv')
    print(data)
    data.to_sql(name='iris', con=engine, schema = 'public', if_exists='replace', index=False)

    engine.execute("""
        CREATE TABLE IF NOT EXISTS apt2(
            city varchar(50) NOT NULL,
            gu varchar(50) NOT NULL,
            dong varchar(50) NOT NULL,
            name varchar(50) NOT NULL,
            type int,
            price int not null
        );"""
    )
    data = pd.read_csv('data/apt2.csv')
    print(data)
    data.to_sql(name='apt2', con=engine, schema = 'public', if_exists='replace', index=False)

## 메인 로직!! 
def cals(opt_operator, number01, number02):
    if opt_operator == "addition":
        return number01 + number02
    elif opt_operator == "subtraction": 
        return number01 - number02
    elif opt_operator == "multiplication":
        return number01 * number02
    elif opt_operator == "division":
        return number01 / number02

app = Flask(__name__)

@app.route("/")
def index():
    db_create()
    return "DB Created Done !!!!!!!!!!!!!!!"

## 카카오톡 텍스트형 응답
@app.route('/api/sayHello', methods=['POST'])
def sayHello():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "안녕 hello I'm Ryan"
                    }
                }
            ]
        }
    }

    return responseBody


## 카카오톡 이미지형 응답
@app.route('/api/showHello', methods=['POST'])
def showHello():
    body = request.get_json()
    print(body)
    print(body['userRequest']['utterance'])

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleImage": {
                        "imageUrl": "https://t1.daumcdn.net/friends/prod/category/M001_friends_ryan2.jpg",
                        "altText": "hello I'm Ryan"
                    }
                }
            ]
        }
    }

    return responseBody

## 카카오톡 Calculator 계산기 응답
@app.route('/api/calCulator', methods=['POST'])
def calCulator():
    body = request.get_json()
    print(body)
    params_df = body['action']['params']
    print(type(params_df))

    print('-----')
    opt_operator = params_df['operators']
    print('operator:', opt_operator)
    print('-----')
    number01 = json.loads(params_df['sys_number01'])['amount']
    number02 = json.loads(params_df['sys_number02'])['amount']

    print(opt_operator, type(opt_operator), number01, type(number01))

    answer_text = str(cals(opt_operator, number01, number02))

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer_text
                    }
                }
            ]
        }
    }

    return responseBody

## Query 조회
@app.route('/api/querySQL', methods=['POST'])
def querySQL():
    
    body = request.get_json()
    params_df = body['action']['params']
    print(params_df, print(type(params_df)))
    sepal_length_num = str(json.loads(params_df['sepal_length_num'])['amount'])

    print(sepal_length_num, type(sepal_length_num))
    query_str = f'''
        SELECT sepal_length, species FROM iris where sepal_length >= {sepal_length_num}
    '''

    engine = create_engine("postgresql://qxqcovcxobgrzr:136d1a4ee21d7d53fefe41723c82cadb3a41edd4203ef9b4759b8ecb1daf68a7@ec2-107-23-76-12.compute-1.amazonaws.com:5432/d7477vdhmjaq31", echo = False)

    with engine.connect() as conn:
        query = conn.execute(text(query_str))

    df = pd.DataFrame(query.fetchall())
    print('------------')
    print(df)
    print('------------')
    nrow_num = str(len(df.index))
    answer_text = nrow_num

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer_text + "개 입니다."
                    }
                }
            ]
        }
    }
    return responseBody

## Query 조회2
@app.route('/api/querySQL2', methods=['POST'])
def querySQL2():
    
    body = request.get_json()
    print(body, type(body))
    
    location01 = body['action']['params']['sys_location01']
    location02 = body['action']['params']['sys_location02']
    location03 = body['action']['params']['sys_location03']

    query_str = f'''
        SELECT DISTINCT "NAME" FROM apt2 where "CITY" = '{location01}' and "GU" = '{location02}' and "DONG" = '{location03}'
    '''
    print('---------------')
    print(query_str)
    print('---------------')

    engine = create_engine("postgresql://qxqcovcxobgrzr:136d1a4ee21d7d53fefe41723c82cadb3a41edd4203ef9b4759b8ecb1daf68a7@ec2-107-23-76-12.compute-1.amazonaws.com:5432/d7477vdhmjaq31", echo = False)

    with engine.connect() as conn:
        query = conn.execute(text(query_str))

    df = pd.DataFrame(query.fetchall())
    print('-----------')
    print(df)
    print('----------')
    results = df['NAME'].tolist()
    answer_text = '/ '.join(results)  

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer_text
                    }
                }
            ]
        }
    }
    return responseBody


## Query 조회3
@app.route('/api/querySQL3', methods=['POST'])
def querySQL3():
    
    body = request.get_json()
    print(body, type(body))
    
    location04 = body['action']['params']['sys_location04']

    query_str = f'''
        SELECT "TYPE" FROM apt2 where "NAME" = '{location04}'
    '''
    print('---------------')
    print(query_str)
    print('---------------')

    engine = create_engine("postgresql://qxqcovcxobgrzr:136d1a4ee21d7d53fefe41723c82cadb3a41edd4203ef9b4759b8ecb1daf68a7@ec2-107-23-76-12.compute-1.amazonaws.com:5432/d7477vdhmjaq31", echo = False)

    with engine.connect() as conn:
        query = conn.execute(text(query_str))

    df = pd.DataFrame(query.fetchall())
    print('-----------')
    print(df)
    print('----------')
    results = df['TYPE'].tolist()
    answer_text = '/'.join(str(s) for s in results)

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer_text
                    }
                }
            ]
        }
    }
    return responseBody

## Query 조회4
@app.route('/api/querySQL4', methods=['POST'])
def querySQL4():
    
    body = request.get_json()
    print(body, type(body))
    
    location05 = body['action']['params']['sys_location05']
    sys_number = body['action']['params']['sys_number']
    print('---------------')
    print(sys_number, type(sys_number))
    print('---------------')
    # params_df = body['action']['params']
    # print(params_df, print(type(params_df)))
    # sys_number = str(json.loads(params_df['sys_number'])['amount'])

    query_str = f'''
        SELECT "PRICE" FROM apt2 where "NAME" = '{location05}' AND "TYPE" = {sys_number}
    '''
    print('---------------')
    print(query_str)
    print('---------------')

    engine = create_engine("postgresql://qxqcovcxobgrzr:136d1a4ee21d7d53fefe41723c82cadb3a41edd4203ef9b4759b8ecb1daf68a7@ec2-107-23-76-12.compute-1.amazonaws.com:5432/d7477vdhmjaq31", echo = False)

    with engine.connect() as conn:
        query = conn.execute(text(query_str))
    print('-----------')
    print(query)
    print('-------------')
    df = pd.DataFrame(query.fetchall())
    print('-----------')
    print(df)
    print('----------')
    results = df['PRICE'].tolist()
    answer_text = '/'.join(str(s) for s in results)

    responseBody = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": answer_text
                    }
                }
            ]
        }
    }
    return responseBody


if __name__ == "__main__":
    db_create()
    app.run()








