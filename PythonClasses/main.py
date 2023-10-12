# ========================= Flask ===================


from flask import Flask, render_template,request,session,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json

with open('config.json','r') as c:
    params = json.load(c) ["params"]

local_server = True

app = Flask(__name__)
app.secret_key = 'super secret key'
if(local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = params['prod_uri']
    
    
db = SQLAlchemy(app)



@app.route("/")
def home():
    posts = Posts.query.filter_by().all()[0:params['no_of_post']]
    return render_template("index.html",params=params,posts=posts)









# @app.route("/sirhamza")
# def sirHamza():
#     return "<h1>My Name is Sir Hamza Ahmed</h1>"


class Contact(db.Model):
    #   ===== id , name , email, phone_num, msg , date 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False , nullable = False)
    email = db.Column(db.String(120), unique=False, nullable = False)
    phone_num = db.Column(db.String(120), unique=True, nullable = False)
    msg = db.Column(db.String(120), unique=False, nullable = False)
    date = db.Column(db.String(120), unique=False , nullable = False)

class Posts(db.Model):
    #   ===== id , title , slug, text date 
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=False , nullable = False)
    subtitle = db.Column(db.String(120), unique=False , nullable = False)
    slug = db.Column(db.String(120), unique=False, nullable = False)
    text = db.Column(db.String(120), unique=True, nullable = False)
    img_file = db.Column(db.String(120), unique=True, nullable = False)
    date = db.Column(db.String(120), unique=False , nullable = False)







@app.route("/about")
def about():
    return render_template("about.html",params=params)



@app.route("/login")
def login():
    return render_template("login.html",params=params)


# ============ creating Dashboard ===================

@app.route("/dashboard" , methods = ['GET','POST'])
def dashboard():
    
    if('user' in session and session['user'] == params['admin_user'] ):
        posts = Posts.query.all()
        return render_template("dashboard.html",params = params,posts=posts)
    
    
    if request.method == 'POST':
        username = request.form.get("uemail")
        userpassword = request.form.get("upass")
        if(username==params['admin_user'] and userpassword == params['admin_pass']):
            # set the session variable
            session['user'] = username
            posts = Posts.query.all()
            return render_template("dashboard.html",params = params,posts=posts)
            
    
    return render_template("login.html",params = params)
    
    
    
    
# ===================== Logout ======================

@app.route("/logout")
def logout():
    session.pop('user')
    return redirect('/dashboard')

 
    
# ================ Delete ===========
@app.route("/delete/<string:id>",  methods = ['GET','POST'])
def delete(id):
    if ('user' in session and session ['user'] == params['admin_user']):
        post = Posts.query.filter_by(id=id).first()
        db.session.delete(post)
        db.session.commit()
        
        
    return redirect('/dashboard')
    



# =============== Edit =================

@app.route("/edit/<string:id>",  methods = ['GET','POST'])
def edit(id):
    if ('user' in session and session ['user'] == params['admin_user']):
        if request.method=='POST':
            box_title = request.form.get('title')
            subtitle = request.form.get('subtitle')

            slug = request.form.get('slug')
            text = request.form.get('text')
            date=datetime.now()
            
            if id == "0":
                post= Posts(title=box_title,slug=slug,content=content,subtitle=subtitle,date=date)
                db.session.add(post)
                db.session.commit()
                
            else:
                post=Posts.query.filter_by(id=id).first()
                post.title=box_title
                post.slug=slug
                post.text=text
                post.subtitle=subtitle
                post.date=date
                db.session.commit()
                return redirect('/edit/'+id)
        post=Posts.query.filter_by(id=id).first()                
        return render_template('edit.html',params=params,post=post)
    










# @app.route("/edit/<string:id>",methods=["GET","POST"])
# def edit(id):
#     if('user' in session and session['user'] == params['admin_user']):
#         if request.method=="POST":
#             box_title = request.form.get('title')
#             subtitle = request.form.get('subtitle')
#             slug =  request.form.get('slug')
#             text = request.form.get('text')
#             date = datetime.now()
            
            
#             if id == "0":
#                 post = Posts(title=box_title,subtitle=subtitle,slug=slug,text=text,date=date) 
#                 db.session.add(post)
#                 db.session.commit()
                
#             else:
#                 post = Posts.query.filter_by(id=id).first()
#                 post.title = box_title
#                 post.subtitle = subtitle
#                 post.slug = slug
#                 post.text = text
#                 post.date = date
#                 db.session.commit()
#                 return redirect('/edit/'+id)
#         post = Posts.query.filter_by(id = id).first()
#         return render_template('edit.html',params=params,post=post) 
        





@app.route("/post/<string:post_slug>",methods=["GET"])
def post_route(post_slug):
    post1 = Posts.query.filter_by(slug = post_slug).first()
    return render_template("post.html",slug=post_slug,post1 = post1,params=params)






@app.route("/contact", methods=['GET','POST'])
def contact():
    #   ===== id , name , email, phone_num, msg , date 
    
    if(request.method == "POST"):
        name = request.form.get("name")
        email = request.form.get("email")
        phone=request.form.get("phone")
        message = request.form.get("message")
        entry=Contact(name = name , email = email, phone_num = phone, msg = message, date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        
        
        
    
    
    return render_template("contact.html",params=params)




@app.route("/post")
def post():
    return render_template("post.html",params=params)







app.run(debug=True)