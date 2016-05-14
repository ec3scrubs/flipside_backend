#!flask/bin/python
from flask import Flask, jsonify
import requests
import crawl
import parse

###############################
## Get crawler data
###############################
crawl.main()

# list of lists
# each item: [body, title, date]
full_text = parse.main()
# print full_text[0]

###############################
## HPE Sentiment requests
###############################
# Init
f = open('hpe_api_key', 'r')
api_key = f.read()

# Go through the corpus
def parse(text):
  pass

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
sentiment_request("the quick brown fox jumps over the lazy dog!")  

###############################
## Flask app
###############################
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)