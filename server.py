from flask import Flask, render_template, send_from_directory, request, redirect, url_for
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(f'{page_name}.html')

def write_to_file(data):
   with open('database.txt', 'a+') as database:
       email = data['email']
       subject = data['subject']
       name = data['name']
       message = data['message']
       file = database.write(f'\n{email}, {subject}, {name}, {message}')

def write_to_csv(data):
    with open('database.csv', 'a', newline='') as database2:
        email = data['email']
        subject = data['subject']
        name = data['name']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, )
        csv_writer.writerow([email, subject, name, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return render_template('thankyou.html', name=data['name'])
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. try again.'


