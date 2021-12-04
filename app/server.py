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

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = dict()
      result['Name'] = request.form.get('Name')
      result['StudentNumber'] = request.form.get('StudentNumber')
      result['Major'] = request.form.get('Major')
      result['Location'] = request.form.get('Location')
      result['Date'] = request.form.get('Date')
      result['Comment'] = request.form.get('Comment')
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=80)
