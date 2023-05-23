## Integrate HTML with Flask
## HTTP verb GET and POST 

## Jinja templates
'''
{%...%} conditions, for loops

Sample Code: 
Case 1: Whenever there is an integer value passed here
{% if result>=50 %} 
<h1>Your result is passed</h1>
{% else %}
<h1>Your result is failed</h1>
{% endif %}

Case 2: Whenever there is a dictionary item as an input, Iterating dictionary and printing values in the form of table 
<table border=2>
    {% for key, value in result.items() %}
    <tr>
        <th>{{ key }}</th>
        <th>{{ value }}</th>
    </tr>
    {% endfor %}
</table>

{{  }} expressions to print output
{#...#} this is for comments
'''

from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

# Result checker html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science + maths + c + datascience)/4
    
    return redirect(url_for('success',score=total_score))

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if float(score) >=50:
        res = 'PASS'
    else:
        res = 'FAIL'
    exp = {'score':score, 'res':res}
    return render_template('result.html',result=exp)




if __name__=="__main__":
    app.run(debug=True)