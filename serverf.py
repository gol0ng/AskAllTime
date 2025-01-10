from flask import Flask, jsonify, request, render_template, redirect
import historydataf
import modeldataf
import llmf
app = Flask(__name__)


@app.route('/')
def index():
    items = historydataf.get_history()
    return render_template('index.html',items = items)

@app.route('/history/<int:hid>')
def history(hid:int):
    items = historydataf.history_detail(hid)
    return render_template('detail.html',detail = items)

@app.route('/settings')
def settings():
    list = modeldataf.get_models_list()
    return render_template('settings.html',list = list)

@app.route('/settings/setdefaultmodel/<id>')
def setdefaultmodel(id: int):
    modeldataf.set_default_model(id)
    # list = modeldataf.get_models_list()
    return redirect('/settings')

@app.route('/settings/addmodel',methods=['POST', 'GET'])
def addmodel():
    if request.method == 'POST':
        model_nickname = request.form['model_nickname']
        model_name = request.form['model_name']
        url = request.form['url']
        APIkey = request.form['APIkey']
        prompt = request.form['prompt']
        if llmf.verify_APIkey(APIkey,url):
            modeldataf.add_model(model_nickname, model_name, url, APIkey, prompt)
            return redirect('/settings')
        else:
            message = 'API信息错误，请重新填写'
            return render_template('addmodel.html', message=message)
    elif request.method == 'GET':
        return render_template('addmodel.html')

@app.route('/settings/deletemodel/<id>')
def deletemodel(id: int):
    modeldataf.delete_model(id)
    return redirect('/settings')

@app.route('/settings/updatemodel/<id>',methods=['POST', 'GET'])
def updatemodel(id):
    if request.method == 'POST':
        model_nickname = request.form['model_nickname']
        model_name = request.form['model_name']
        url = request.form['url']
        APIkey = request.form['APIkey']
        prompt = request.form['prompt']
        item = {'model_nickname': model_nickname, 'model_name':model_name, 'url':url, 'APIkey':APIkey, 'prompt':prompt}
        if llmf.verify_APIkey(APIkey,url):
            modeldataf.update_model(model_nickname, model_name, url, APIkey, prompt,id)
            return redirect('/settings')
        else:
            message = 'API信息错误，请重新填写'
            return render_template('updatemodel.html', message=message)
    elif request.method == 'GET':
        item = modeldataf.get_model(id)
        return render_template('updatemodel.html',item = item)

def run():
    app.run(debug=True,port=1234,use_reloader=False)


