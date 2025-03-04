import pandas as pd
import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import gdown as gd

FILE_ID = "1F7s170qiJIAhP1AzJIcY-eFmTMehYnoa"
OUTPUT = "dataset.csv"


def download_dataset():
    if os.path.exists(OUTPUT):
        return
    url = f"https://drive.google.com/uc?id={FILE_ID}"
    gd.download(url, OUTPUT, quiet=False)


def load_dataset():
    download_dataset()
    return pd.read_csv(OUTPUT)


df = load_dataset()
df_filtered = df.dropna()
df_filtered = df_filtered[["BYTES", "PKT_TIMES", "TYPE"]]
df_filtered = df_filtered[df_filtered["TYPE"].isin(['P', 'M', 'W', 'L'])]
label_to_int = {'L': 0, 'P': 1, 'M': 2, 'W': 3}
df_filtered['TYPE'] = df_filtered['TYPE'].map(label_to_int)


def packet_times_to_number(packet_times):
    if isinstance(packet_times, str):
        packet_times = packet_times.strip('[]').split()
        return np.array([float(x) for x in packet_times])
    return np.array([])


df_filtered['PKT_TIMES'] = df_filtered['PKT_TIMES'].apply(packet_times_to_number)


def packet_times_stats(packet_times):
    if len(packet_times) == 0:
        return 0, 0, 0
    return np.mean(packet_times), np.std(packet_times), len(packet_times)


packets_stats = df_filtered['PKT_TIMES'].apply(packet_times_stats)
df_filtered['PKT_MEAN'] = packets_stats.apply(lambda x: x[0])
df_filtered['PKT_STD'] = packets_stats.apply(lambda x: x[1])
df_filtered['PKT_COUNT'] = packets_stats.apply(lambda x: x[2])
df_filtered = df_filtered.drop(columns=['PKT_TIMES'])

X = df_filtered[['BYTES', 'PKT_MEAN', 'PKT_STD', 'PKT_COUNT']]
Y = df_filtered['TYPE']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=68)

random_forest = RandomForestClassifier(n_estimators=100, random_state=68)
random_forest.fit(X_train, Y_train)
Y_pred = random_forest.predict(X_test)
print("Random Forest Classifier accuracy: ", accuracy_score(Y_test, Y_pred))
