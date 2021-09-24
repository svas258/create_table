from flask import Flask
from flask import request
from flask import render_template
import psycopg2
from app import app
import os

#app = Flask(__name__)


@app.route('/script')
def application():
     return render_template('index.html')

@app.route('/create_table', methods=['POST'])
def create_table():
  if request.method=="POST":
      try:
         table_name = request.form.get('table_name')
         field_name_list = request.form.getlist('fields[]')
         field_list = []
         for field in field_name_list:
                field_list.append(field+ " VARCHAR(50) DEFAULT NULL")
                field_query = " ( " + ", ".join(field_list) + " ); "
                create_table_query = 'CREATE TABLE IF NOT EXISTS '+table_name+'' + field_query
                print(create_table_query)
                conn = psycopg2.connect(database="postgres", user="postgres",password="Test@1234", host="db")
                cursor = conn.cursor()
                cursor.execute(create_table_query)
                conn.commit()
                conn.close()
                return "Table: "+table_name+" created successfully"
      except Exception as e:
             return str(e)


#if __name__ == '__main__':
#    app.run(host='0.0.0.0', debug = True, port = 5005) 
	

