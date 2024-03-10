from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    try:
        # Using eval, but be aware of the security implications
        result = eval(expression)
    except Exception as e:
        result = "Error: " + str(e)
    #return render_template('index.html', result=result)
    return render_template('index.html', expression=result)

if __name__ == '__main__':
    app.run(debug=True)
