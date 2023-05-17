from flask import Flask, render_template, jsonify

app=Flask(__name__)

JOBS=[
  {
    'id':1,
    'role':"Data Analyst",
    'location':"Banglore, India",
    'salary':"Rs. 12,00,000"
  },
  {
    'id':2,
    'role':"Data Scientist",
    'location':"Chennai, India"
   },
  {
    'id':3,
    'role':"Frontend Developer",
    'location':"Pune, India",
    'salary':"Rs. 8,00,000"
   },
  {
    'id':4,
    'role':"Backend Developer",
    'location':"Kolkata, India",
    'salary':"Rs. 15,00,000"
   }
]

@app.route('/')
def home():
  return render_template('index.html', jobs=JOBS)

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


app.run(debug=True)
