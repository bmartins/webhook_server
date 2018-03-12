from bottle import route, run, request, Bottle

app = application = Bottle()

@app.route("/<url:re:.*>" , method=['POST'])
def index(url):
    body = request.body.read()

    query = ''
    for k in request.query:
        if query  != '':
            query +=  '&'
        query  += k + '=' + request.query[k]

    if query != '':
        query = '?' + query
    print "########################################################"
    print "url: /" + url + query
    print body
    print "########################################################"
    return {"ok": 1}


#app.run(host='0.0.0.0', port=8001)

