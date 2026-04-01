# Sample routes from original repo.
# Placed here so they can be used as examples and references


"""

@app.route('/log-in-user', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        session['username'] = name   # store in session
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/display-user-stats')
def user_stats():
    key = {"Name": session['username']}  # retrieve from session
    response = table.get_item(Key=key)
    ...




@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        # Extract form data
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        genre = request.form['genre']

        # Process the data (e.g., add it to a database)
        # For now, let's just print it to the console
        print("Name:", first_name, last_name, ":", "Favorite Genre:", genre)

        flash('User added successfully! Huzzah!', 'success')  # 'success' is a category; makes a green banner at the top
        # Redirect to home page or another page upon successful submission
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('add_user.html')

@app.route('/delete-user',methods=['GET', 'POST'])
def delete_user():
    if request.method == 'POST':
        # Extract form data
        name = request.form['name']

        # Process the data (e.g., add it to a database)
        # For now, let's just print it to the console
        print("Name to delete:", name)

        flash('User deleted successfully! Hoorah!', 'warning')
        # Redirect to home page or another page upon successful submission
        return redirect(url_for('home'))
    else:
        # Render the form page if the request method is GET
        return render_template('delete_user.html')


@app.route('/display-users')
def display_users():
    # hard code a value to the users_list;
    # note that this could have been a result from an SQL query :)
    users_list = (('John','Doe','Comedy'),('Jane', 'Doe','Drama'))
    return render_template('display_users.html', users = users_list)

"""