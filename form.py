from bottle import route, run, template, request
import sidh, sith


@route('/', method=['GET', 'POST'])
def input():
    if request.method == 'POST':
        if request.forms.get("zpet"):
            return web_page()
        lA = int(request.forms.get('lA'))
        lB = int(request.forms.get('lB'))
        eA = int(request.forms.get('eA'))
        eB = int(request.forms.get('eB'))
        if request.forms.get('SIDH'):
            result =  result_sidh(lA,lB,eA,eB)
            return result_page(result)
        if request.forms.get('SITH'):
            result =  result_sith(lA,lB,eA,eB)
            return result_page(result,False)

    return web_page()
        #to_print = "<br>"+str(result)+" </br>"
    return to_print

def result_page(result, SIDH = True):
    button ='<form action="/" method="post">\
            <input value="Zpět" name="zpet" type=\"submit\" /></br>\
    </form>'
    if SIDH:
        sidh = result
        sith = "<h2>...ZzzZzz...</h2>"
        button_d = button
        button_t = ""
    else:
        sidh = "<h2>...ZzzZzz...</h2>"
        sith = result
        button_t = button
        button_d = ""

    return f'<!DOCTYPE html> \
    <html> \
    <head> \
    <meta name="viewport" content="width=device-width, initial-scale=1">\
    <style>'+'\
    body {\
      font-family: Arial;\
      color: white;\
    }\
    .split {\
      height: 100%;\
      width: 50%;\
      position: fixed;\
      z-index: 1;\
      top: 0;\
      overflow-x: hidden;\
      padding-top: 10px;\
    }\
    .left {\
      left: 0;\
      background-color: #616161;\
    }\
    .right {\
      right: 0;\
      background-color: white;\
      color:#616161;\
    }\
    .centered {\
      position: absolute;\
      top: 50%;\
      left: 50%;\
      transform: translate(-50%, -50%);\
      text-align: center;\
    }\
    </style>\
    </head>\
    <body>\
    <div class="split left">\
      <div class="centered">\
        <h1>SITH</h1>\
        '+sith+'\
        <br>'+button_t+'</br>\
      </div>\
    </div>\
    <div class="split right">\
      <div class="centered">\
        <h1>SIDH</h1>\
        '+sidh+'\
        <br>'+button_d+'</br>\
    </div></div>\
    </body>\
    </html>'

def web_page():
    return f'<!DOCTYPE html> \
    <html> \
    <head> \
    <meta name="viewport" content="width=device-width, initial-scale=1">\
    <style>'+'\
    body {\
      font-family: Arial;\
      color: white;\
    }\
    .split {\
      height: 100%;\
      width: 50%;\
      position: fixed;\
      z-index: 1;\
      top: 0;\
      overflow-x: hidden;\
      padding-top: 20px;\
    }\
    .left {\
      left: 0;\
      background-color: #616161;\
    }\
    .right {\
      right: 0;\
      background-color: white;\
      color:#616161;\
    }\
    .centered {\
      position: absolute;\
      top: 50%;\
      left: 50%;\
      transform: translate(-50%, -50%);\
      text-align: center;\
    }\
    .centered img {\
      width: 150px;\
      border-radius: 50%;\
    }\
    .container {\
    width: 200px;\
    clear: both;\
    }\
    .container input {\
    width: 100%;\
    clear: both;\
    }\
    </style>\
    </head>\
    <body>\
    <div class="split left">\
      <div class="centered">\
        <h1>SITH</h1>\
        <form action="/" method="post">\
                <br>\
                <div class="container">\
                prvočíslo: <input name=\"lA\" type=\"text\" /> \
                exponent: <input name=\"eA\" type=\"text\" /></br><br>\
                prvočíslo: <input name=\"lB\" type=\"text\" /> \
                exponent: <input name=\"eB\" type=\"text\" /></br>\
                <br></div>\
                <input value="SITH" name="SITH" type=\"submit\" /></br>\
        </form>\
      </div>\
    </div>\
    <div class="split right">\
      <div class="centered">\
        <h1>SIDH</h1>\
        <form action="/" method="post">\
                <br>\
                <div class="container">\
                prvočíslo: <input name=\"lA\" type=\"text\" /> \
                exponent: <input name=\"eA\" type=\"text\" /></br><br>\
                prvočíslo: <input name=\"lB\" type=\"text\" /> \
                exponent: <input name=\"eB\" type=\"text\" /></br>\
                <br></div>\
                <input value="SIDH" name="SIDH" type=\"submit\" /></br>\
        </form>\
    </div></div>\
    </body>\
    </html>'

def result_sidh(lA,lB,eA,eB):
    E,field,ma,na,mb,nb,Gen1A,Gen2A,Gen1B,Gen2B,pB,pA,key = sidh.main(lA,lB,eA,eB)
    return "<h3>Veřejné parametry</h3> <b>Eliptická křivka</b>: "+str(E)+"\
    <br><b>Těleso:</b> "+str(field[0])+", <b>polynom:</b> "+str(field[1])+"</br>\
    <h2>Alfréd</h2> \
    <b>Torze</b>: "+str(lA)+"^"+str(eA)+"<br>\
    <b>Veřejné generátory:</b> "+str(Gen1A)+", "+str(Gen2A)+" <br>\
    <br><b>Veřejný klíč:</b> "+str(pA[0])+"<br><b>Obraz Blaženiných generátorů: </b>"+str(pA[1])+", "+str(pA[2])+"</br> \
    <br><b>Soukromý klíč:</b> "+str(ma)+", "+str(na)+'</br>\
    <p style="color:red"><b>Sdílený klíč:</b> '+str(key)+"</p>\
    <h2>Blažena</h2>\
    <b>Torze</b>: "+str(lB)+"^"+str(eB)+"<br>\
    <b>Veřejné generátory:</b> "+str(Gen1B)+", "+str(Gen2B)+" <br>\
    <br><b>Veřejný klíč:</b> "+str(pB[0])+"<br><b>Obraz Alfrédových generátorů: </b>"+str(pB[1])+", "+str(pB[2])+"</br> \
    <br><b>Soukromý klíč:</b> "+str(mb)+", "+str(nb)+'</br>\
    <p style="color:red"><b>Sdílený klíč:</b> '+str(key)+"</p>"

def result_sith(lA,lB,eA,eB):
    E0,field,E1,ma,na,mb,nb,Gen1A,Gen2A,Gen1B,Gen2B,pB,pA,key= sith.main(lA,lB,eA,eB)
    return "<h3>Veřejné parametry</h3> \
    <br><b>Těleso:</b> "+str(field[0])+", <b>polynom:</b> "+str(field[1])+"</br>\
    <h2>Alfréd</h2> \
    <b>SITH křivka</b>: "+str(E1[0])+"<br>\
    <b>Torze</b>: "+str(lA)+"^"+str(eA)+"<br>\
    <b>Veřejné generátory:</b> "+str(Gen1A)+", "+str(Gen2A)+"<br> \
    <b>Veřejné generátory pro Blaženu:</b> "+str(Gen1B)+", "+str(Gen2B)+" \
    <br><b>Veřejný klíč:</b> "+str(pA[0])+"<br><b>Obraz Blaženiných generátorů: </b>"+str(pA[1])+", "+str(pA[2])+"</br> \
    <br><b>Soukromý klíč:</b> "+str(ma)+", "+str(na)+'</br>\
    <p style="color:red"><b>Sdílený klíč:</b> '+str(key)+"</p>\
    <h2>Blažena</h2>\
    <b>Torze</b>: "+str(lB)+"^"+str(eB)+"<br>\
    <br><b>Veřejný klíč:</b> "+str(pB[0])+"<br><b>Obraz Alfrédových generátorů: </b>"+str(pB[1])+", "+str(pB[2])+"</br> \
    <br><b>Soukromý klíč:</b> "+str(mb)+", "+str(nb)+'</br>\
    <p style="color:red"><b>Sdílený klíč:</b> '+str(key)+"</p>"



run(host='localhost', port=8081, reloader = True)
