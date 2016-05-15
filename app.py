#!flask/bin/python
from flask import Flask, jsonify, request
from flask.ext.cors import CORS
import requests
import search

###############################
## Flask app
###############################
app = Flask(__name__)
CORS(app)

sentiments = [
  {
    'id': 1,
    'date': u'19-05-2015',
    'description': u'ate food',
    'sentiment': u'positive',
    'score': u'0.5' 
  },
  {
    'id': 2,
    'date': u'20-05-2015',
    'description': u'failed all the exams rofl',
    'sentiment': u'negative',
    'score': u'-0.9' 
  },

]

@app.route('/sentiment/api/', methods=['GET'])
def get_sentiments():
  return jsonify({'sentiments': sentiments})

@app.route('/sentiment/api/query', methods=['POST'])
def get_query():  
  json_dict = request.get_json()
  print json_dict
  return "hello"



if __name__ == '__main__':
    app.run(debug=True)

###############################
## Search queries
###############################
# Edit this to come from HTTP request later
def search_query(query):
  query = "chicken rice"
  results = search.main("dictionary.txt", "postings.txt", query)

  # Find the most stars and least stars
  sorted_reviews = sorted([(k, v) for (k, v) in results.items()], key=lambda x: x[1], reverse=True)
  best_review = sorted_reviews[0]
  worst_review = sorted_reviews[-1]

  print best_review, worst_review
  # Filter out if the difference between them is only 1 star
  if best_review[1] - worst_review[1] == 1.0:
    return "The best and worst reviews are similar to each other."
    # todo: set this up as a POST response

###############################
## HPE Sentiment requests
###############################
# Init
f = open('hpe_api_key', 'r')
api_key = f.read()

# Go through the corpus
# def parse(text):
#   pass

# Send request to HPE sentiment analysis
def sentiment_request(line):
  request_line = ""
  for word in line.split():
    request_line += word + '+' 

  # [:-1] is a quick hack to remove the '+' at the end rofl
  r = requests.get('https://api.havenondemand.com/1/api/sync/analyzesentiment/v1?text=' + request_line[:-1] + '&apikey=' + api_key)
  
  # Debug
  print request_line[:-1]
  print r.text

# Debug
# sentiment_request("the quick brown fox jumps over the lazy dog!")  

