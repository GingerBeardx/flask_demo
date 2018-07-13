from flask import Flask, render_template, redirect, session, flash, request
app = Flask(__name__)
app.secret_key = 'somesupersecretkey'

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/new')
def new():
  return render_template('new.html')

@app.route('/edit/<email>')
def edit(email):
  return render_template('edit.html')

@app.route('/show/<email>')
def show(email):
  return render_template('show.html')

@app.route('/create', methods=['POST'])
def create():
  print "*" * 80
  print request.form
  errors = False

  if len(request.form['name']) < 3:
    flash('name must be at least 3 characters long')
    errors = True
  if len(request.form['email']) == 0:
    flash('email must not be blank')
    errors = True

  if errors == True:
    return redirect('/new')

  if not 'users' in session:
    session['users'] = []

  new_list = session['users']
  new_list.append({
    'name': request.form['name'],
    'email': request.form['email']
  })
  session['users'] = new_list
  return redirect('/')

@app.route('/update', methods=['POST'])
def update():
  return redirect('/')

@app.route('/delete/<email>', methods=['POST'])
def destroy():
  return redirect('/')

app.run(debug=True)

# an app with a form to create a user -- new.html
# validate the form input
# display a list of users -- index.html
# display a specific user -- show.html (edit/delete buttons)
# layout.html -- templating
# edit/delete user -- edit.html