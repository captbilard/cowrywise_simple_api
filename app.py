import datetime
import uuid

from flask import Flask, jsonify
from collections import OrderedDict


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


uuid_dict = {}

@app.route('/', methods=['GET'])
def index():
    timestamp = str(datetime.datetime.now())
    ids = uuid.uuid4().hex
    uuid_dict[timestamp] = ids
    data = reverse_dict(uuid_dict)
    return jsonify(data)


def reverse_dict(dict):
    ordered_dict = OrderedDict(sorted(dict.items(), key = lambda x:datetime.datetime.strptime(x[0], '%Y-%m-%d %H:%M:%S.%f'), reverse=True))
    return ordered_dict

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)