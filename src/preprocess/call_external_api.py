# import http.client
# import json


# API_BASE_URL = '10.181.131.244'
# POS_TAG_PORT = '5500'
# NER_PORT = '10009'

# def get_pos_tag(text):
#     conn = http.client.HTTPConnection(API_BASE_URL, POS_TAG_PORT)
#     payload = json.dumps({'text': text})
#     headers = {
#         "content-type": "application/json",
#         "x-api-key": ""
#         }

#     conn.request('POST', '/', payload, headers)
#     res = conn.getresponse()
#     data = json.loads(res.read().decode('utf-8'))

#     return data

# def get_ner(text):
#     conn = http.client.HTTPConnection(API_BASE_URL, NER_PORT)
#     payload = json.dumps({'text': text})
#     headers = {
#         "content-type": "application/json",
#         "x-api-key": ""
#         }

#     conn.request('POST', '/', payload, headers)
#     res = conn.getresponse()
#     data = json.loads(res.read().decode('utf-8'))

#     return data

import json
import requests
 
url_ner = "https://api.prosa.ai/v2/text/ner"
url_pos = "https://api.prosa.ai/v2/text/basic-nlp"
api_key_ner=""
api_key_pos=""
 


def get_pos_tag(text):
    data = {
        "version": "v2",
        "text": text,
    }
    headers = {
        "Content-Type": "application/json",
         "x-api-key": api_key_pos
    }
    response = requests.post(url_pos, headers=headers, json=data)
    jsondata=response.json()
    pos_tags = []
    for sentence in jsondata['sentences']['sentences']:
        tokens = sentence.get('tokens', [])
        sentence_tags = [[token.get('token', ''), token.get('pos_tag', '')] for token in tokens]
        pos_tags.append(sentence_tags)

    # Create the final dictionary in the desired format
    result = {'postags': pos_tags}
#    return numpy.array(result)
    return result

def get_ner(text):
    data = {
        "version": "v2",
        "text": text,
    }
    headers = {
        "Content-Type": "application/json",
         "x-api-key": api_key_ner
    }
    response = requests.post(url_ner, headers=headers, json=data)
    jsondata=response.json()
    return jsondata
