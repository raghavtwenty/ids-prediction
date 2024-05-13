"""
Filename: ids_ml_gradio.py
Title: XG Boost - Python Gradio file for Web App
Author: Raghava | GitHub: @raghavtwenty
Date Created: June 10, 2023 | Last Updated: May 13, 2024
Language: Python | Version: 3.10.14, 64-bit
"""

# Importing required libraries
import xgboost as xgb
import numpy as np
from joblib import load
import gradio as gr
from _2_scale_transform import transform_new_input


# Model location
model = xgb.Booster()
model.load_model("m3_xg_boost.model")


# User input prediction
def user_input_predict(x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13):

    # Preprocessing input
    user_input = [[x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13]]

    user_input = np.array(user_input)
    user_input = transform_new_input(user_input)
    user_input = xgb.DMatrix(user_input)

    # Prediction
    user_input_result = model.predict(user_input)
    user_input_result = np.argmax(user_input_result)

    result_msg = ""
    result_msg_info = ""

    if user_input_result == 0:
        result_msg = "NORMAL, No possibility of attack."
        result_msg_info = "You are safe!"

    elif user_input_result == 1:
        result_msg = "Higher Possibility of BLACKHOLE attack."
        result_msg_info = "Information : BLACKHOLE attacks occur when a router deletes all messages it is supposed to forward."

    elif user_input_result == 2:
        result_msg = "Higher Possibility of TCP-SYN attack."
        result_msg_info = "Information : A SYN flood (half-open attack) is a type of denial-of-service (DDoS) attack which aims to make a server unavailable to legitimate traffic by consuming all available server resources. By repeatedly sending initial connection request (SYN) packets, the attacker is able to overwhelm all available ports on a targeted server machine, causing the targeted device to respond to legitimate traffic sluggishly or not at all"

    elif user_input_result == 3:
        result_msg = "Higher Possibility of PORTSCAN attack."
        result_msg_info = "Information : A port scan is an attack that sends client requests to a range of server port addresses on a host, with the goal of finding an active port and exploiting a known vulnerability of that service. The results will uncover network or server status."

    elif user_input_result == 4:
        result_msg = "Higher Possibility of DIVERSION attack."
        result_msg_info = "Information : Diversion/Social engineering is an attack vector that relies heavily on human interaction and often involves manipulating people into breaking normal security procedures and best practices to gain unauthorized access to systems, networks or physical locations or for financial gain. Spoofing, Phishing falls into this category."
    else:
        result_msg = "Try Again"
        result_msg_info = "Choose different values."

    return result_msg, result_msg_info


# Main
# Set interface
grShow = gr.Interface(
    user_input_predict,
    inputs=[
        gr.components.Slider(
            1, 4, label="Port Number - The switch port through which the flow passed"
        ),
        gr.components.Slider(
            0, 352772, label="Received Packets - Number of packets received by the port"
        ),
        gr.components.Slider(
            0,
            2.715916e08,
            label="Received Bytes - Number of bytes received by the port",
        ),
        gr.components.Slider(
            0, 2.392430e08, label="Sent Bytes - Number of bytes sent by the port."
        ),
        gr.components.Slider(
            0, 421598, label="Sent Packets - Number of packets sent by the port."
        ),
        gr.components.Slider(
            0,
            3317,
            label="Port alive Duration (S) - The time port has been alive in seconds.",
        ),
        gr.components.Slider(
            0,
            6500000,
            label="Delta Received Bytes - Number of bytes received by the port.",
        ),
        gr.components.Slider(
            0,
            6500000,
            label="Delta Sent Bytes - Number of bytes sent by the port.",
        ),
        gr.components.Slider(
            0,
            5,
            label="Delta Port alive Duration (S) - The time port has been alive in seconds.",
        ),
        gr.components.Slider(
            1,
            5,
            label="Connection Point - Network connection point expressed as a pair of the network element identifier and port number.",
        ),
        gr.components.Slider(
            0,
            1800000,
            label="Total Load/Rate - Obtain the current observed total load/rate (in bytes/s) on a link.",
        ),
        gr.components.Slider(
            0,
            610,
            label="Active Flow Entries - Returns the number of active flow entries in this table.",
        ),
        gr.components.Slider(
            0,
            1020000,
            label="Packets Matched - Returns the number of packets that successfully matched in the table.",
        ),
    ],
    outputs=["text", "text"],
    examples=[
        [4, 350188, 14877116, 101354648, 159524, 2910, 278, 280, 5, 4, 0, 6, 667324],
        [2, 2326, 12856942, 31777516, 2998, 2497, 560, 560, 5, 2, 0, 4, 7259],
        [4, 150, 19774, 6475473, 3054, 166, 556, 6068, 5, 4, 502, 6, 7418],
        [2, 209, 20671, 6316631, 274, 96, 3527, 2757949, 5, 2, 183877, 8, 90494],
        [2, 1733, 37865130, 38063670, 3187, 2152, 0, 556, 5, 3, 0, 4, 14864],
    ],
    description="Cyber Attack - Intrusion Detection Prediction using Machine Learning Models (XG Boost) <br> Designed & Developed by Raghava <br> GitHub: @raghavtwenty <br> Date Created: June 10, 2023 | Last Updated: May 13, 2024 <br> Examples are at the bottom of this page.",
    theme="finlaymacklon/boxy_violet",
    title="Cyber Attack IDS",
    allow_flagging="never",
)


# Render webpage
grShow.launch()
