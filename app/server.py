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


@app.route('/application_form', methods = ['POST', 'GET'])
def apply():
   if request.method == 'POST':
      apply = dict()
      apply['Name'] = request.form.get('Name')
      apply['StudentNumber'] = request.form.get('StudentNumber')
      apply['Major'] = request.form.get('Major')
      apply['Location'] = request.form.get('Location')
      apply['Date'] = request.form.get('Date')
      apply['Comment'] = request.form.get('Comment')
      return render_template("application_form.html",apply = apply)

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
   uName = request.form.get('Name')
   uStudentNumber = request.form.get('StudentNumber')
   uMajor = request.form.get('Major')
   uLocation = request.form.get('Location')
   uDate = request.form.get('Date')
   uComment = request.form.get('Comment')
   
   return render_template("submit.html",uName = uName, uStudentNumber = uStudentNumber, uMajor = uMajor, uLocation = uLocation, uDate = uDate, uComment = uComment)

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=80)
