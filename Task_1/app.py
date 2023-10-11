from asyncio import run
from flask import Flask,jsonify
import pickle
from flask import render_template,request
app=Flask(__name__,template_folder='template')
c=pickle.load(open('model.pkl','rb'))
@app.route('/')
def home():
    return render_template('cod.html')
@app.route('/predict',methods=['POST'])
def perdict():
    cno=int(request.form.get('ccnum'))
    at=int(request.form.get('amt'))
    un=int(request.form.get('zip'))
    result=c.predict([[cno,at,un]])
    final=str(result)
    t=final[1]

    if t==1:
        return "**Transaction is fraud**"
    else:
        return "**Transaction is safe**"

    
    

if __name__=='__main__':
    app.run(debug=True)




    
