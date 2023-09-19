
# Experience Here : 
# https://huggingface.co/spaces/raghavtwenty/cyber-attack-prediction

"""
Filename : _1_gr_gradio_ids.py
Title : Intrusion Detection Prediction - Predicting - Gradio application
Author : raghav | GitHub : @raghavtwenty 
Date Created : June 10, 2023 | Last Updated : June 18, 2023 
Language : Python | Version : 3.11.3, 64-bit
"""

# Importing the required libraries
import gradio as gr
import joblib


# File location
model = joblib.load("best_model_0.82_percentage")


# Naive Bayes
def naive_bayes_gaussian(x1,x2,x3,x4,x5,x6,x7,x8,x9,x10):

    testInput = [[x1,x2,x3,x4,x5,x6,x7,x8,x9,x10]]

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

    return resultMsg, resultMsgInfo

# Main
# Set interface
grShow = gr.Interface(
    naive_bayes_gaussian, 
    inputs = [gr.components.Slider(1,4,label = "Port Number - The switch port through which the flow passed"),
                gr.components.Slider(0,352772,label = "Received Packets - Number of packets received by the port"),
                gr.components.Slider(0,2.715916e+08,label = "Received Bytes - Number of bytes received by the port"),
                gr.components.Slider(0,2.392430e+08,label = "Sent Bytes - Number of bytes sent by the port"),
                gr.components.Slider(0,421598,label = "Sent Packets - Number of packets sent by the port"),
                gr.components.Slider(0,3317,label = "Port alive Duration (S) - The time port has been alive in seconds"),
                gr.components.Slider(0,5,label = "Delta Port alive Duration (S) - The time port has been alive in seconds"),
                gr.components.Slider(1,5,label = "Connection Point - Network connection point expressed as a pair of the network element identifier and port number."),
                gr.components.Slider(0,1.012574e+06,label = "Packets Looked Up - Returns the number of packets looked up in the table."),
                gr.components.Slider(0,1.012574e+06,label = "Packets Matched - Returns the number of packets that successfully matched in the table.")],
    outputs = ["text","text"],
    examples=[[4,349950,14844034,76099589,158473,2540,4,4,663067,662932],
                    [1,2990,67970025,63263334,4240,1906,5,1,13782,13662],
                    [1,1241,25263813,25832,188,236,4,1,3216,3106], 
                    [3,744,12647232,31974078,126060,241,4,3,127492,127392],
                    [2,4571,113552526,94919832,6236,2757,5,3,24500,24272]],
    description = "Cyber Attack - Intrusion Detection Prediction --- Designed & Developed by Raghav --- GitHub : @raghavtwenty --- Examples are at the bottom of this page. --- Created on : June 10, 2023 | LastUpdated : June 18, 2023",
    allow_flagging=None,
    theme='finlaymacklon/boxy_violet')



# Render webpage
grShow.launch()
