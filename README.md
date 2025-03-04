NetWork Traffic Analysis and Classification using Machine Learning
===============================================================
This project deals with capturing and classifying network traffic from various applications with Wireshark and with machine
learning. The main goal is to determine the application types from their network flow patterns and
examine possible security threats where an attacker seeks to determining the particular app or website being used.

Key Objectives:
Capture and analyze network traffic during web browsing, video streaming, audio streaming, and video conferencing
activities.
Extract relevant features from packet captures that include IP/TCP/TLS header fields, packet sizes, inter-arrival times,
flow sizes flow volumes etc.

Use machine learning models (Random Forest) to classify network flows for enabling application type identification.

Investigate the capability of an attacker to determine with accuracy the exact application that can be used from the
traffic pattern on the internet.

Pre-requisites:
Python 3.12 or higher. 
the following libraries: pandas, numpy, scikit-learn, matplotlib, seaborn and gdown.
`pip install pandas numpy scikit-learn matplotlib seaborn gdown`

How to run The Project:
1. Clone the repository or download the zip file.
2. Open it in of your favorite IDE or text editor.
3. install manually:  sudo apt update && sudo apt install python3-tk
4. Run the `main.py` file.
5. 1-8 is about displaying the plots ,  9 is about closing the program and 10 is about downloading the dataset and 
    training the model.


Results and Conclusion:
1. The model was able to classify the network traffic with an accuracy of 96% using Random Forest Classifier.
2. There are district patterns in the network traffic that can be used to identify the application type.

Future Work:
1. Collect more data about real time communication applications like Zoom, Skype, and Microsoft Teams.
2. Investigate more deeply about countermeasures to prevent attackers from determining the application type.

Authors:
1. Rei Shaul ,  Ron Avraham , Lior Fikhman , Idan Shumski from the Department of Computer Science in Ariel University 
    as part of the course "Communication Networks"

License:
This project is for Educational purposes only , anyone can use it and modify it as long as they give credit.



