from flask_pymongo import PyMongo
from flask import Flask,jsonify,request

app = Flask(__name__)

app.config['MONGO_DBNAME']='shubhamm0333'
app.config['MONGO_URI']= 'mongodb://chill:chill@ds125578.mlab.com:25578/shubhamm0333'


mongo =PyMongo(app)

print("shit")
@app.route('/see',methods=['GET'])
def get_all_data():
    data1=mongo.db.data1
    
    output=[]

    for q in data1.find():
        output.append({"decade": q["decade"], "artist": q["artist"], "song":q["song"], "weeksAtOne":q["weeksAtOne"]})
    return jsonify({"result": output})
@app.route('/see/<decade>',methods=['GET'])  
def get_one(decade):

    data1=mongo.db.data1

    q=data1.find_one({"decade":decade})
    if q:
        output={"decade": q["decade"], "artist": q["artist"], "song":q["song"], "weeksAtOne":q["weeksAtOne"]}
    else:
        output= "No result"

    return jsonify({"result": output})

@app.route('/', methods=['POST'])
def add_some():
    data1=mongo.db.data1

    decade= request.json['decade']
    artist=request.json['artist']
    song=request.json['song']
    weeksAtOne=request.json['weeksAtOne']

    data1_id=data1.insert({'decade':decade,'artist':artist,'song':song,'weeksAtOne':weeksAtOne})
    new_data=data1.find_one({'_id':data1_id})

    output={'decade':new_data['decade'],'artist':new_data['artist'],'song':new_data['song'],'weeksAtOne':new_data['weeksAtOne']}

    return jsonify({"result": output})




if __name__=="__main__":
    print("poo")
    app.run(debug=True)
    
