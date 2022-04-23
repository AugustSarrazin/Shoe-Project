from flask import render_template,redirect,session,request
from flask_app import app
from flask_app.models.user import User
from flask_app.models.shoe import Shoe

@app.route('/')
def index():
    return render_template('index.html', shoes=Shoe.get_all_shoes_with_sneaker_head)

@app.route('/new/shoe')
def new_event():
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['user_id']
    }
    return render_template('create_shoe.html',user=User.get_by_id(data))

@app.route('/create/shoe', methods=['POST'])
def create_event ():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Shoe.validate_shoe(request.form):
        return redirect('/new/event')
    
    data = {
        'name': request.form['name'],
        'brand': request.form['brand'],
        'model': request.form['model'],
        'size': request.form['size'],
        'price': request.form['price'],
        'description':request.form['description'],
        'user_id': request.form['user_id']
    }
    Shoe.save(data)
    return redirect ('/dashboard')

@app.route('/edit/shoe/<int:id>')
def edit_event(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("edit_event.html",edit=Shoe.get_one(data),user=User.get_by_id(user_data))



@app.route('/update/shoe',methods=['POST'])
def update_shoe():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Shoe.validate_shoe(request.form):
        return redirect('/dashboard')
    data = {
            'name': request.form['name'],
            'brand': request.form['brand'],
            'model': request.form['model'],
            'size': request.form['size'],
            'price': request.form['price'],
            'user_id': request.form['user_id']
    }
    Shoe.update(data)
    return redirect('/dashboard')

@app.route('/shoe/<int:id>')
def show_shoe(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    user_data = {
        "id":session['user_id']
    }
    return render_template("show_shoe.html",event=Shoe.get_one(data),user=User.get_by_id(user_data))


@app.route('/destroy/event/<int:id>')
def destroy_event(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Shoe.destroy(data)
    return redirect('/dashboard')
