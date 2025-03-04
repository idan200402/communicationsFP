import os
import subprocess

PLOTS = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'src')
SCRIPTS = {
    "1": "inter_arrival_soundcloud_youtube_packets.py",
    "2": "packet_sizes_soundcloud_youtube.py",
    "3": "protocol_distribution_youtube_zoom_google.py",
    "4": "tls_handshakes_chrome_firefox.py",
    "5": "ttl_youtube_zoom.py",
    "6": "window_size_youtube_soundcloud.py",
    "7": "zoom_udp_packet_rate.py"
}


def run_code(name):
    file_path = os.path.join(PLOTS, name)
    if os.path.exists(file_path):
        subprocess.run(['python3', file_path])
    else:
        print(f"File {name} does not exist")


def display_menu():
    while True:
        print("\nChoose a graph to display:")
        print("1 - Inter-arrival Times (SoundCloud & YouTube)")
        print("2 - Packet Sizes (SoundCloud & YouTube)")
        print("3 - Protocol Distribution (YouTube, Zoom, Google)")
        print("4 - TLS Handshakes (Chrome & Firefox)")
        print("5 - TTL Distribution (YouTube & Zoom)")
        print("6 - Window Size Analysis (YouTube & SoundCloud)")
        print("7 - UDP Packet Rate (Zoom)")
        print(
            "8 - Run All (not recommended , but if you do it: you have you close each graph manually to see the next one)")
        print("9 - Exit Program")
        print("10 - download dataset and run ML.py")
        choice = input("Enter your choice: ")

        if choice == "9":
            print("Exiting program...")
            break
        elif choice == "8":
            for script in SCRIPTS.values():
                run_code(script)
        elif choice == "10":
            run_code("ML.py")
        elif choice in SCRIPTS:
            run_code(SCRIPTS[choice])
        else:
            print("Invalid choice. Please try again.")
            continue


if __name__ == "__main__":
    display_menu()
