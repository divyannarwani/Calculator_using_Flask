from flask import Flask, request, render_template, jsonify


app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template('index.html')

@app.route("/math", methods=["POST"])
def math_ops():
    if (request.method == 'POST'):
        ops = request.form['operation']

        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])

        if ops == 'add':
            r = num1+num2
            result = f"The sum of {num1} and {num2} is {r}"
        
        if ops == 'subtract':
            r = num1-num2
            result = f"The difference of {num1} and {num2} is {r}"

        if ops == 'multiply':
            r = num*num2
            result = f"The product of {num1} and {num2} is {r}"

        if ops == 'divide':
            r = num1/num2
            result = f"The divide of {num1} and {num2} is {r}"

        return render_template("results.html", result = result)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
    