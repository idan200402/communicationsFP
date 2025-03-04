import os
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, '../data')
zoom_file = os.path.join(DATA, 'zoom_udp_times.txt')


def extract_times(filename):
    times = []
    with open(filename, 'r') as f:
        for line in f:
            try:
                time = float(line.split()[0])
                if time > 0:
                    times.append(time)
            except:
                continue
        if len(times) < 2:
            return [], []

        bin = 1  # 1 second bin
        start = min(times)
        end = max(times)
        bins_edges = np.arange(start, end, bin)
        packets_rates, ___ = np.histogram(times, bins=bins_edges)
        return bins_edges[:-1], packets_rates

time_stamps, packets_rates = extract_times(zoom_file)

plt.figure(figsize=(10, 6))
plt.plot(time_stamps, packets_rates, color='blue')
plt.xlabel('Time in seconds')
plt.ylabel('UDP packet rate per second')
plt.title('Zoom UDP packet rate')
plt.grid(True)
plt.show()