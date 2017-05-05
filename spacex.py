from flask import Flask, render_template, json
import csv
app = Flask(__name__)

TITLE = "Chirping Falcon"

@app.route("/", methods=['GET'])
def hello(name="Cori"):
  return render_template("index.html", title=TITLE, name=name)

@app.route("/api/sentiment", methods=['GET'])
def get_sentiment():
  print(json.dumps({'happy':0.75, 'sad':0.50, 'mad':0.25}))
  return json.dumps({'happy':0.75, 'sad':0.50, 'mad':0.25})

@app.route("/api/data", methods=['GET'])
def fill_data():
  with open('/tmp/data.csv') as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    data = []
    for row in reversed(list(reader)):
      data.append({'date':row[0],'happy':row[1], 'sad':row[2], 'mad':row[3]})
      count+=1
      if count == 9:
        return json.dumps({'data':data})

@app.errorhandler(404)
def page_not_found(error):
  return render_template("error.html", title=TITLE), 404

if __name__ == "__main__":
    app.run()