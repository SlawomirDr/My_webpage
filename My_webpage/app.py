from flask import Flask

app = Flask(__name__)


from flask import render_template

@app.route('/mypage/me', methods=['GET'])
def mypage():
    return render_template("me.html")
    

from flask import request, redirect    

@app.route('/mypage/contact', methods=['GET', 'POST'])
def mypage_contact():
   if request.method == 'GET':
       print("We received GET")
       return render_template("contact.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect('/mypage/me')