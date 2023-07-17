from flask import Flask, render_template, request, redirect, url_for,SQLAlchemy
app = Flask(__name__, template_folder='templates')
import re
#app.config['database_url'] = 'sqlite:///my_table.db'
#db = SQLAlchemy(app)
def check_password(password):
    def case(password):
        lower_case = False
        upper_case = False
        for char in password:
            lower_case = lower_case or char.islower()
        for char in password:
            upper_case = upper_case or char.isupper()
        return lower_case and upper_case
    def end_digit():
         if(password[-1].isdigit()):
             return True
         else:
             return False
    length_password = len(password) in range(8, 100)
    if case and end_digit and length_password:
        return True
    else:
        return False
#new_password = Password(password=password)
#db.session.add(password)
#db.session.commit()
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        message = 'requirements passed!' if check_password(password) else 'requirements not satisfied!'
        status = 'success' if check_password(password) else 'attempt failed!'

    return render_template('index.html')
#multi-routes
@app.route('/report')
def report():
    message = request.args.get('message')
    status = request.args.get('status', 'info')
    return render_template('report.html', message=message, status=status)
#main 
if __name__ == '__main__':
    app.run(debug=True)