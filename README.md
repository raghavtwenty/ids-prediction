# INTRUSION DETECTION PREDICTION 
INTRUSION DETECTION SYSTEM - Predicting the type of cyber attack based on network packets using Machine Learning models
<br><br>

### _EXPERIENCE HERE ..._
https://huggingface.co/spaces/raghavtwenty/cyber-attack-prediction
<br><br>

### - PROBLEM

A firewall alone doesn’t provide adequate protection against modern cyber threats. Malware and other malicious content are often delivered using legitimate types of traffic, such as email, or web traffic. In order to solve this problem we need to step in further and examine the network traffic, this is where the Intrusion Detection System plays a major role.
<br><br>

### - WHAT IS IDS?

An Intrusion Detection System (IDS) is a network security technology originally built for detecting vulnerability exploits against a target application or computer. The IDS is a listen-only device. The IDS monitors traffic and reports results to an administrator.
<br><br>

### - WORKING OF IDS

![260608446-d533139a-5928-46ac-b1a5-71f9b59333e8](https://github.com/raghavtwenty/ids-prediction/assets/126254197/e794a9ea-6e68-4c6d-9584-9774165f30e7)

Typical intrusion detection systems look for known attack, Signature-based IDS monitors inbound network traffic, looking for specific patterns and sequences that match known attack signatures or abnormal deviations from set norms. These anomalous patterns in the network traffic are then sent up in the stack for further investigation at the protocol and application layers of the OSI (Open Systems Interconnection) model.<br>
An IDS is placed out of the real-time communication band (a path between the information sender and receiver) within your network infrastructure to work as a detection system. It instead leverages a SPAN or TAP port for network monitoring and analyzes a copy of inline network packets (fetched through port mirroring) to make sure the streaming traffic is not malicious or spoofed in any way. The IDS efficiently detects infected elements with the potential to impact your overall network performance, such as malformed information packets, DNS poisonings, port scans and more.<br>
IDS is either installed on your network or a client system (host-based IDS)
<br><br>

### - OBJECTIVE

To predict the type of cyber attack that could have possibly occurred in a network. Having the past network logs from a server using machine learning models, We have to choose the best suitable model for the prediction, For the new input classify the type of cyber attack that has higher chance.
<br><br>

### - USERS

1. Security operations center (SOC) analysts.
2. Incident responders.
3. Cyber Security analysts.
4. A person with adequate knowledge on networking can experiment this.
<br><br>

### - OVERVIEW OF INITIAL DATASET

![260610474-e652e75a-a1bd-41b8-b6dc-84300ecc1848](https://github.com/raghavtwenty/ids-prediction/assets/126254197/c7df3cbc-1420-49b6-baae-cb8be37352e6)

This dataset contains 5000 records of features extracted from Network Port Statistics to protect modern-day computer networks from cyber attacks and are thereby classified into 5 classes. <br>

Switch ID - The switch through which the network flow passed. <br>
Port Number - The switch port through which the flow passed. <br>
Received Packets - Number of packets received by the port. <br>
Received Bytes - Number of bytes received by the port. <br>
Sent Bytes - Number of bytes sent by the port. <br>
Sent Packets - Number of packets sent by the port. <br>
Port alive Duration (S) - The time port has been alive in seconds. <br>
Packets Rx Dropped - Number of packets dropped by the receiver. <br>
Packets Tx Dropped - Number of packets dropped by the sender. <br>
Packets Rx Errors - Number of transmit errors. <br>
Delta Received Packets - Number of packets received by the port. <br>
Delta Received Bytes - Number of bytes received by the port. <br>
Delta Sent Bytes - Number of bytes sent by the port. <br>
Delta Sent Packets - Number of packets sent by the port. <br>
Delta Port alive Duration (S) - The time port has been alive in seconds. <br>
Delta Packets Rx Dropped - Number of packets dropped by the receiver. <br>
Delta Packets Tx Dropped - Number of packets dropped by the sender. <br>
Delta Packets Rx Errors - Number of receive errors. <br>
Delta Packets Tx Errors - Number of transmit errors. <br>
Connection Point - Network connection point expressed as a pair of the network element identifier and port number. <br>
Total Load/Rate - Obtain the current observed total load/rate (in bytes/s) on a link. <br>
Total Load/Latest - Obtain the latest total load bytes counter viewed on that link. <br>
Load/Rate - Obtain the current observed unknown-sized load/rate (in bytes/s) on a link. <br>
Unknown Load/Latest - Obtain the latest unknown-sized load bytes counter viewed on that link. <br>
Latest bytes counter - Latest bytes counted in the switch port. <br>
Checkis_valit - Indicates whether this load was built on valid values. <br>
vpn_keyTable ID - Returns the Table ID values. <br>
Active Flow Entries - Returns the number of active flow entries in this table. <br>
Packets Looked Up - Returns the number of packets looked up in the table. <br>
Packets Matched - Returns the number of packets that successfully matched in the table. <br>
Max Size - Returns the maximum size of this table. <br>
_TARGET_ --- Label - Label types for intrusions - Normal:0, Blackhole:1, TCP-SYN:2, PortScan:3, Diversion:4, Overflow:5 <br>
<br><br>

### - PREPROCESSING (Visualization)

Heatmap before scaling the columns. <br>
![260611431-327931d5-aa5c-40a3-9f2d-084afedc9311](https://github.com/raghavtwenty/ids-prediction/assets/126254197/4ff93764-97f6-4f46-ba5a-6187fcb1261f)

Heatmap after scaling the columns. <br>
![260611484-da6a5a5d-bc77-41d7-92f4-20a898793fed](https://github.com/raghavtwenty/ids-prediction/assets/126254197/13b22023-18fb-4a40-9a5e-35876c82fee2)

Heatmap after removing the least correlated columns. <br>
![260611464-eff5ef03-a6d0-43be-b4db-a3d0a301eee0](https://github.com/raghavtwenty/ids-prediction/assets/126254197/b26e3907-5488-4b43-8e8e-be18e6ca366a)

<br><br>

### - RESULT
![260609385-1c925325-d96d-433c-ac42-dd7548fbb553](https://github.com/raghavtwenty/ids-prediction/assets/126254197/38a00efd-4e88-43ad-bb54-2cc3e3fe9805)

![260609624-6dffd482-3648-4e0d-ae80-c1c685608613](https://github.com/raghavtwenty/ids-prediction/assets/126254197/eb85b877-a47d-4278-8188-a2e0d1dd7088)

After preprocessing the dataset, K-Nearest Neighbors algorithm and the Naive Bayes algorithm had been used for classifying the test dataset. After multiple trials The KNN model classified the test dataset and resulted in an average of 76 % accuracy while the Naive bayes algorithm resulted in an average of 82% accuracy. Since the Naive Bayes algorithm performed better than the KNN algorithm, It is chosen for the deployment process.
<br><br>

### - SAMPLE TEST CASES & OUTPUT
![260609648-045bd9db-b852-459c-8df7-9a261d8d249e](https://github.com/raghavtwenty/ids-prediction/assets/126254197/68164d22-65d7-4d6f-8d41-e6c37c5ad0b4)

![260609672-0bfdc1b2-3ff7-488f-8d9d-51018cc5e5d6](https://github.com/raghavtwenty/ids-prediction/assets/126254197/6f24656f-e491-48c2-9b51-acb4e1407fef)

<br><br>

### - FUTURE SCOPE
Companies realize the limitations of a standard IDS. Some are reacting to build bigger and better products for their customers. New IDS solutions may come with a lower administrative burden. They may rely on machine learning to lower the risk of false positives, so staff have less to examine every day and vendors may update them simultaneously, so the system always has access to up-to-date information in real time.
<br><br>

_END OF README_


