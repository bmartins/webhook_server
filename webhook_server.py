from bottle import route, run, request, Bottle

app = application = Bottle()

@app.route('/' , method=['POST'])
def index():
    body = request.body.read()
    print "########################################################"
    print body
    print "########################################################"
    return {"ok": 1}


#run(host='0.0.0.0', port=8001)

