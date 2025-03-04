import os
import numpy as np
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, '../counts')

youtube_tcp_file = os.path.join(DATA, 'youtube_tcp_count.txt')
youtube_udp_file = os.path.join(DATA, 'youtube_udp_count.txt')
firefox_tcp_file = os.path.join(DATA, 'firefox_tcp_count.txt')
firefox_udp_file = os.path.join(DATA, 'firefox_udp_count.txt')
zoom_tcp_file = os.path.join(DATA, 'zoom_tcp_count.txt')
zoom_udp_file = os.path.join(DATA, 'zoom_udp_count.txt')
zoom_tls_file = os.path.join(DATA, 'zoom_tls_count.txt')
youtube_tls_file = os.path.join(DATA, 'youtube_tls_count.txt')
firefox_tls_file = os.path.join(DATA, 'firefox_tls_count.txt')


def count_packets(filename):
    with open(filename, 'r') as f:
        try:
            lines = f.readlines()
            return int(lines[0])
        except:
            return 0


youtube_tcp_count = count_packets(youtube_tcp_file)
youtube_udp_count = count_packets(youtube_udp_file)
firefox_tcp_count = count_packets(firefox_tcp_file)
firefox_udp_count = count_packets(firefox_udp_file)
zoom_tcp_count = count_packets(zoom_tcp_file)
zoom_udp_count = count_packets(zoom_udp_file)
youtube_tls_count = count_packets(youtube_tls_file)
firefox_tls_count = count_packets(firefox_tls_file)
zomm_tls_count = count_packets(zoom_tls_file)
youtube_total = youtube_tcp_count + youtube_udp_count + youtube_tls_count
firefox_total = firefox_tcp_count + firefox_udp_count + firefox_tls_count
zoom_total = zoom_tcp_count + zoom_udp_count+ zomm_tls_count

apps = ['Youtube', 'Zoom', 'Firefox']

youtube_tcp_prc = youtube_tcp_count / youtube_total * 100 if youtube_total > 0 else 0
youtube_udp_prc = youtube_udp_count / youtube_total * 100 if youtube_total > 0 else 0
youtube_tls_prc = youtube_tls_count / youtube_total * 100 if youtube_total > 0 else 0
zoom_tcp_prc = zoom_tcp_count / zoom_total * 100 if zoom_total > 0 else 0
zoom_udp_prc = zoom_udp_count / zoom_total * 100 if zoom_total > 0 else 0
zoom_tls_prc = zomm_tls_count / zoom_total * 100 if zoom_total > 0 else 0
firefox_tcp_prc = firefox_tcp_count / firefox_total * 100 if firefox_total > 0 else 0
firefox_udp_prc = firefox_udp_count / firefox_total * 100 if firefox_total > 0 else 0
firefox_tls_prc = firefox_tls_count / firefox_total * 100 if firefox_total > 0 else 0

plt.figure(figsize=(10, 10))

tcp_values = [youtube_tcp_prc, zoom_tcp_prc, firefox_tcp_prc]
udp_values = [youtube_udp_prc, zoom_udp_prc, firefox_udp_prc]
tls_values = [youtube_tls_prc, zoom_tls_prc  ,firefox_tls_prc]
bar_width = 1.5
plt.bar(apps, tcp_values, color='blue', label='TCP', width=bar_width)
plt.bar(apps, udp_values, color='orange', label='UDP', width=bar_width, bottom=tcp_values)
plt.bar(apps, tls_values, color='green', label='TLS', width=bar_width, bottom=np.array(tcp_values) + np.array(udp_values))
plt.ylabel('Percentage of packets')
plt.title('Distribution of TCP  ,  UDP and TLS packets in Youtube, Zoom and Firefox')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.1)
plt.show()
