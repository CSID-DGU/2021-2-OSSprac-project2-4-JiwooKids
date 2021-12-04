from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
   return render_template('main.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
   error=None
   if request.method == 'POST':
      if request.form['username'] != 'ossp' or request.form['password'] != 'ossp1234':
         error= '회원정보 입력이 잘못되었습니다. 다시 시도하세요.'
      else:
         return render_template("application_form.html")
   return render_template('login.html',error = error)

@app.route('/application_form')
def application_form():
   return render_template('application_form.html')

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=80)
