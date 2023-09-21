
from flask import Flask, render_template, request
from requests import get
import joblib



app = Flask(__name__)
model = joblib.load("best_model_0.82_percentage")


@app.route("/output", methods = ["POST"])
def finalPage():
    i1 = request.form.get("aa")
    i2 = request.form.get('bb')
    i3 = request.form.get('cc')
    i4 = request.form.get('dd')
    i5 = request.form.get('ee')
    i6 = request.form.get('ff')
    i7 = request.form.get('gg')
    i8 = request.form.get('hh')
    i9 = request.form.get('ii')
    i10 = request.form.get('jj')

    testInput = [[int(i1),int(i2),int(i3),int(i4),int(i5),int(i6),int(i7),int(i8),int(i9),int(i10)]]


    #testInput = [[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]]

    userInputResult = model.predict(testInput)[0]   # Outcome is at index 0
    
    resultMsg = ""
    resultMsgInfo = ""
    if userInputResult == 0:
        resultMsg = "NORMAL, No possibility of attack."
        resultMsgInfo = "You are safe!"

    elif userInputResult == 1:
        resultMsg = "Higher Possibility of BLACKHOLE attack."
        resultMsgInfo = "Information : BLACKHOLE attacks occur when a router deletes all messages it is supposed to forward."
        
    elif userInputResult == 2:
        resultMsg = "Higher Possibility of TCP-SYN attack."
        resultMsgInfo = "Information : A SYN flood (half-open attack) is a type of denial-of-service (DDoS) attack which aims to make a server unavailable to legitimate traffic by consuming all available server resources. By repeatedly sending initial connection request (SYN) packets, the attacker is able to overwhelm all available ports on a targeted server machine, causing the targeted device to respond to legitimate traffic sluggishly or not at all"
        
    elif userInputResult == 3:
        resultMsg = "Higher Possibility of PORTSCAN attack."
        resultMsgInfo = "Information : A port scan is an attack that sends client requests to a range of server port addresses on a host, with the goal of finding an active port and exploiting a known vulnerability of that service. The results will uncover network or server status."
        
    elif userInputResult == 4:
        resultMsg = "Higher Possibility of DIVERSION attack."
        resultMsgInfo = "Information : Diversion/Social engineering is an attack vector that relies heavily on human interaction and often involves manipulating people into breaking normal security procedures and best practices to gain unauthorized access to systems, networks or physical locations or for financial gain. Spoofing, Phishing falls into this category."
    else :
        resultMsg = "Try Again"
        resultMsgInfo = "Choose different values."

            

    return render_template("output.html",op = resultMsg, op2 = resultMsgInfo)


@app.route("/")
def home():

    return render_template("input.html")


if __name__ == "__main__":
    app.run(debug=True)