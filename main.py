from flask import Flask, request

app = Flask(__name__)

import mysql.connector  # We connected database and py with this

database = mysql.connector.connect(
    host="localhost",
    user="bindu",  # we need this know
    password="Blah123"  # we need this know // these credentials
)

cursor = database.cursor()  # In databases we need cursors to manipulate data


def insert_person(name, age, bio, country, blog_count):
    sql = "INSERT INTO my_stupid_sql.persons " \
          "(name, age, bio, country, blog_count)" \
          "VALUES (%s, %s, %s, %s, %s)"
    val = (name, age, bio, country, blog_count)
    cursor.execute(sql, val)
    print(cursor.rowcount, " person record inserted.")
    database.commit()


# This is for inserting a person's info in table

def insert_blog(title, description, content, created_by, claps, image_url):
    # Inserts the given values to a blog

    sql = "INSERT INTO my_stupid_sql.blogs " \
          "(title, description, content, created_by, claps, image_url)" \
          "VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (title, description, content, created_by, claps, image_url)
    cursor.execute(sql, val)
    print(cursor.rowcount, "Blog are saved!")
    database.commit()  # for Commiting the current transaction


@app.route('/')
def default():
    return 'Working'


@app.route('/add-person', methods=['POST'])
def add_person_route():
    name = request.form['name']
    # request that is obj
    age = request.form['age']
    bio = request.form['bio']
    country = request.form['country']
    blog_count = request.form['blog_count']
    insert_person(name, age, bio, country, blog_count)
    # person = {'Bindu': 1, 'Pavan': 2, 'blala': 3}
    return ''


@app.route('/add-blog', methods=['POST'])
def add_blog_route():
    title = request.form['title']  # request that is obj
    description = request.form['description']
    content = request.form['content']
    created_by = request.form['created_by']
    claps = request.form['claps']
    image_url = request.form['image_url']
    insert_blog(title, description, content, created_by, claps, image_url)
    return '_'


if __name__ == '__main__':
    app.run(port=8080)
