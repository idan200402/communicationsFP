import os
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, '../data')

chrome_file  = os.path.join(DATA, 'chrome_tls.txt')
firefox_file = os.path.join(DATA, 'firefox_tls.txt')

def count_tls_handshakes(filename):
    with open(filename) as f:
        lines = f.readlines()
        time_stamps = []
        for line in lines:
            try :
                time_stamps.append(float(line.split()[0]))
            except:
                continue

    if len(time_stamps) < 0:
        return len(time_stamps), 1

    time_stamps.sort()
    duration = max(time_stamps) - min(time_stamps)
    return len(time_stamps), duration if duration > 0 else 1

chrome_handshakes, chrome_duration = count_tls_handshakes(chrome_file)
firefox_handshakes, firefox_duration = count_tls_handshakes(firefox_file)

chrome_handshakes_per_sec = chrome_handshakes / max(chrome_duration ,1)
firefox_handshakes_per_sec = firefox_handshakes / max(firefox_duration  ,1)

apps = ['Chrome', 'Firefox']
rates = [chrome_handshakes_per_sec, firefox_handshakes_per_sec]

plt.figure(figsize=(6, 4))
plt.bar(apps, rates, color=['blue', 'orange'])
plt.ylabel('TLS Handshakes rates')
plt.title('TLS Handshakes rates for Chrome and Firefox')
plt.xlabel('Apps')
plt.show()


