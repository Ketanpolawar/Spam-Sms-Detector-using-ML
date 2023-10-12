from asyncio import run
from flask import Flask,jsonify
import pickle
from flask import render_template,request
app=Flask(__name__,template_folder='template')
c=pickle.load(open('mod2.pkl','rb'))
@app.route('/')
def home():
    return render_template('cod.html')
@app.route('/predict',methods=['POST'])
def perdict():
    cno=int(request.form.get('ccnum'))
    at=float(request.form.get('amt'))
    zp=int(request.form.get('zip'))
    lat=float(request.form.get('lat'))
    long=float(request.form.get('lon'))
    cp=float(request.form.get('cp'))
    un=int(request.form.get('unix'))
    mla=float(request.form.get('mla'))
    mlo=float(request.form.get('mlo'))

    result=c.predict([[cno,at,zp,lat,long,cp,un,mla,mlo]])
    final=str(result)
    t=int(final[1])

    if t==1:
        return "**Transaction is fraud**"
    else:
        return "**Transaction is safe**"

    
    

if __name__=='__main__':
    app.run(debug=True)




    
