# -*- coding: utf-8 -*-
"""hackathon.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/12NpyAa_pN7GMdXgcQrhZcuZjO8EGkJgV
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('/yapay_zeka.xlsx')
#Veri tipini kontrol etmek
#print(df.info())
#Veri setinde eksik olup olmadığını kontrol etmek
#print(df.isnull().sum())
#Eksik verileri ortalama ile doldurmak ancak bu yoldan vazgeçtim
# df['DOWNLOAD'].fillna(df['DOWNLOAD'].mean(), inplace=True)
# df['UPLOAD'].fillna(df['UPLOAD'].mean(), inplace=True)
df['TIME_STAMP'] = pd.to_datetime(df['TIME_STAMP'])
# Haftanın günü ve saat kolonlarını eklemek
df['WEEKDAY'] = df['TIME_STAMP'].dt.weekday
df['HOUR'] = df['TIME_STAMP'].dt.hour
df['MINUTE'] = df['TIME_STAMP'].dt.minute
def fill_missing_with_group_mean(df, group_cols, target_col):
    # Gruplara göre ortalamaları hesaplamak
    group_means = df.groupby(group_cols)[target_col].transform('mean')
    # Eksik değerleri grupların geçmişte aynı tarihte olan ortalamaları ile doldurmak
    df[target_col].fillna(group_means, inplace=True)
# 'DOWNLOAD' kolonundaki eksik verileri doldurmak
fill_missing_with_group_mean(df, ['WEEKDAY', 'HOUR', 'MINUTE'], 'DOWNLOAD')
# 'UPLOAD' kolonundaki eksik verileri doldurmak
fill_missing_with_group_mean(df, ['WEEKDAY', 'HOUR', 'MINUTE'], 'UPLOAD')


# Veriyi gün bazında gruplama
daily_data = df.groupby(df['TIME_STAMP'].dt.date).agg({'DOWNLOAD': 'sum', 'UPLOAD': 'sum'}).reset_index()
daily_data.columns = ['DATE', 'DOWNLOAD_SUM', 'UPLOAD_SUM']

# # # İndirme verisi için gün bazında grafik çizme
# plt.figure(figsize=(18, 6))
# plt.plot(daily_data['DATE'], daily_data['DOWNLOAD_SUM'], marker='o', color='b')
# plt.xlabel('Date')
# plt.ylabel('Download Traffic')
# plt.title('Daily Download Traffic')
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.show()

# # Yükleme verisi için gün bazında grafik çizme
# plt.figure(figsize=(18, 6))
# plt.plot(daily_data['DATE'], daily_data['UPLOAD_SUM'], marker='o', color='g')
# plt.xlabel('Date')
# plt.ylabel('Upload Traffic')
# plt.title('Daily Upload Traffic')
# plt.xticks(rotation=45)
# plt.grid(True)
# plt.show()



# #GÜNLÜK GRAFİK OLUŞTURMA
# df['TIME_STAMP'] = pd.to_datetime(df['TIME_STAMP'])
# df['DATE'] = df['TIME_STAMP'].dt.date
# first_day = df['DATE'].min()
# last_day = df['DATE'].max()

# # İlk ve son günü hariç tutarak veri setini filtreledim
# filtered_df = df[(df['DATE'] != first_day) & (df['DATE'] != last_day)]
# daily_data = filtered_df.groupby('DATE').agg({'DOWNLOAD': 'sum', 'UPLOAD': 'sum'}).reset_index()
# #daily_data = df.groupby('DATE').agg({'DOWNLOAD': 'sum', 'UPLOAD': 'sum'}).reset_index()
# # İndirme grafiği
# plt.figure(figsize=(12, 6))
# plt.plot(daily_data['DATE'], daily_data['DOWNLOAD'], label='Download', marker='o', color='b')
# plt.xlabel('Date')
# plt.ylabel('Download Traffic')
# plt.title('Daily Download Traffic Data')
# plt.legend()
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.show()
# # Yükleme grafiği
# plt.figure(figsize=(12, 6))
# plt.plot(daily_data['DATE'], daily_data['UPLOAD'], label='Upload', marker='o', color='g')
# plt.xlabel('Date')
# plt.ylabel('Upload Traffic')
# plt.title('Daily Upload Traffic Data')
# plt.legend()
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.show()
#GÜNLÜK GRAFİK OLUŞTURMA KAPATMA



# #GÜNLÜK GRAFİĞİ İLK VE SON GÜNDEN FİLTRELEMEK
# # İlk ve son günü belirlemek için min ve max kullandım
# df['DATE'] = df['TIME_STAMP'].dt.date
# first_day = df['DATE'].min()
# last_day = df['DATE'].max()

# # İlk ve son günü hariç tutarak veri setini filtreledim
# filtered_df = df[(df['DATE'] != first_day) & (df['DATE'] != last_day)]

# # İndirme grafiği
# plt.figure(figsize=(54, 18))
# plt.plot(filtered_df['TIME_STAMP'], filtered_df['DOWNLOAD'], label='Download', marker='o', color='b')
# plt.xlabel('Timestamp')
# plt.ylabel('Download Traffic')
# plt.title('Download Traffic Data (Excluding First and Last Day)')
# plt.legend()
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.show()
# # Yükleme grafiği
# plt.figure(figsize=(54, 18))
# plt.plot(filtered_df['TIME_STAMP'], filtered_df['UPLOAD'], label='Upload', marker='o', color='g')
# plt.xlabel('Timestamp')
# plt.ylabel('Upload Traffic')
# plt.title('Upload Traffic Data (Excluding First and Last Day)')
# plt.legend()
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.show()

# #GÜNLÜK GRAFİĞİN FİLTRELENMESİNİN KAPANMASI


# #HAFTALIK GRAFİK OLUŞTURMA
# df['WEEK'] = df['TIME_STAMP'].dt.to_period('W')
# # Veriyi haftalık olarak gruplama
# weekly_groups = df.groupby('WEEK')

# # Her hafta için grafik oluşturma
# for week, group in weekly_groups:
#     plt.figure(figsize=(12, 6))
#     plt.plot(group['TIME_STAMP'], group['DOWNLOAD'], label='Download', marker='x',color ='b')
#     plt.xlabel('Timestamp')
#     plt.ylabel('Traffic')
#     plt.title(f'Traffic Data for Week {week}')
#     plt.legend()
#     plt.grid(True)
#     plt.xticks(rotation=45)
#     plt.show()

#     plt.figure(figsize=(12, 6))
#     plt.plot(group['TIME_STAMP'], group['UPLOAD'], label='Upload', marker='o',color ='g')
#     plt.xlabel('Timestamp')
#     plt.ylabel('Traffic')
#     plt.title(f'Traffic Data for Week {week}')
#     plt.legend()
#     plt.grid(True)
#     plt.xticks(rotation=45)
#     plt.show()
# # HAFTALIK GRAFİK OLUŞTURMA KAPATMA


# # 3 saatlik GRAFİK OLUŞTURMA
# def get_3hour_period(hour):
#     return (hour // 3) * 3

# df['HOUR'] = df['TIME_STAMP'].dt.hour
# df['3HOUR_PERIOD'] = df['HOUR'].apply(get_3hour_period)

# # Gün ve 3 saatlik dilim kombinasyonunu ekleyin
# df['DAY_3HOUR'] = df['TIME_STAMP'].dt.date.astype(str) + '-' + df['3HOUR_PERIOD'].astype(str)
# # Veriyi gün ve 3 saatlik dilimlere göre gruplama
# three_hour_groups = df.groupby('DAY_3HOUR')

# # Her 3 saatlik dilim için grafik oluşturma
# for period, group in three_hour_groups:

#     plt.figure(figsize=(18, 9))
#     plt.plot(group['TIME_STAMP'], group['DOWNLOAD'], label='Download', marker='X')
#     plt.xlabel('Timestamp')
#     plt.ylabel('Traffic')
#     plt.title(f'Download Traffic Data for Period {period}')
#     plt.legend()
#     plt.grid(True)
#     plt.xticks(rotation=45)
#     plt.show()

#     plt.figure(figsize=(18, 9))
#     plt.plot(group['TIME_STAMP'], group['UPLOAD'], label='Upload', marker='o')
#     plt.xlabel('Timestamp')
#     plt.ylabel('Traffic')
#     plt.title(f'Upload Traffic Data for Period {period}')
#     plt.legend()
#     plt.grid(True)
#     plt.xticks(rotation=45)
#     plt.show()
# 3 SAATLİK GRAFİK OLUŞTURMA KAPATMA



# ## 1 OCAK TARİHİ İÇİN GRAFİK
# january_first_data = df[df['TIME_STAMP'].dt.date == pd.to_datetime('2024-01-01').date()]
# hourly_data = january_first_data.groupby(january_first_data['TIME_STAMP'].dt.floor('H')).agg({'DOWNLOAD': 'sum', 'UPLOAD': 'sum'}).reset_index()
# # İndirme grafiği
# plt.figure(figsize=(12, 6))
# plt.plot(hourly_data['TIME_STAMP'], hourly_data['DOWNLOAD'], label='Download', marker='o', color='b')
# plt.xlabel('Timestamp')
# plt.ylabel('Download Traffic')
# plt.title('Hourly Download Traffic Data for January 1')
# plt.legend()
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.show()
# # Yükleme grafiği
# plt.figure(figsize=(12, 6))
# plt.plot(hourly_data['TIME_STAMP'], hourly_data['UPLOAD'], label='Upload', marker='o', color='g')
# plt.xlabel('Timestamp')
# plt.ylabel('Upload Traffic')
# plt.title('Hourly Upload Traffic Data for January 1')
# plt.legend()
# plt.grid(True)
# plt.xticks(rotation=45)
# plt.show()
# # 1 OCAK TARİHİ İÇİN GRAFİK KAPATMA



##BONUS GÖREV
## SAATLERİN ÖNCEKİ GÜNLERDEKİ ORTALAMASI ALARAK EN ÇOK TRAFİĞİN OLDUĞU SAATİ HESAPLAMAK
df['TIME_STAMP'] = pd.to_datetime(df['TIME_STAMP'])
df['HOUR'] = df['TIME_STAMP'].dt.hour
# Veriyi saatlik olarak gruplama ve ortalamalarını hesaplama
hourly_avg_data = df.groupby('HOUR').agg({'DOWNLOAD': 'mean', 'UPLOAD': 'mean'}).reset_index()

# Yoğun trafik saatlerini belirleme
# Yoğun trafik saatlerini belirleme
peak_download_hours = hourly_avg_data.sort_values(by='DOWNLOAD', ascending=False).head(24)
peak_upload_hours = hourly_avg_data.sort_values(by='UPLOAD', ascending=False).head(24)

# Yoğun indirme saatlerini görselleştirme
plt.figure(figsize=(12, 6))
plt.bar(peak_download_hours['HOUR'], peak_download_hours['DOWNLOAD'], color='b')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Download Traffic')
plt.title('Peak Download Hours')
plt.grid(True)
plt.show()
# Yoğun yükleme saatlerini görselleştirme
plt.figure(figsize=(12, 6))
plt.bar(peak_upload_hours['HOUR'], peak_upload_hours['UPLOAD'], color='g')
plt.xlabel('Hour of the Day')
plt.ylabel('Average Upload Traffic')
plt.title('Peak Upload Hours')
plt.grid(True)
plt.show()

## ONE CLASS SVM and LOCAL OUTLIER KARŞILAŞTIRMASI
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.neighbors import LocalOutlierFactor
from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt

# Load the Excel file
# Yerel klasörden veriyi yükle
df = pd.read_excel('/yapay_zeka.xlsx' )

# Anomali tespiti için verileri ön işleme
df['TIME_STAMP'] = pd.to_datetime(df['TIME_STAMP'])
df.set_index('TIME_STAMP', inplace=True)

# # Eksik verileri doldurma
hourly_data = df.resample('H').sum()

# Local Outlier Factor (LOF) ile saatlik verilerde anomali tespiti
lof = LocalOutlierFactor(n_neighbors=35, contamination=0.01)
hourly_data['anomaly_lof_download'] = lof.fit_predict(hourly_data[['DOWNLOAD']])
hourly_data['anomaly_lof_upload'] = lof.fit_predict(hourly_data[['UPLOAD']])

# One-Class SVM ile saatlik verilerde anomali tespiti
svm = OneClassSVM(nu=0.05, kernel='rbf', gamma=0.01)
hourly_data['anomaly_svm_download'] = svm.fit_predict(hourly_data[['DOWNLOAD']])
hourly_data['anomaly_svm_upload'] = svm.fit_predict(hourly_data[['UPLOAD']])

# LOF anomali tespiti ile saatlik indirme verilerini görselleştirme
plt.figure(figsize=(14, 7))
plt.plot(hourly_data.index, hourly_data['DOWNLOAD'], label='Download')
anomalies_lof_download = hourly_data[hourly_data['anomaly_lof_download'] == -1]
plt.scatter(anomalies_lof_download.index, anomalies_lof_download['DOWNLOAD'], color='red', label='Anomaly (LOF)', marker='o')
plt.title('Hourly Download Data with LOF Anomalies')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Download Traffic')
plt.show()

# LOF anomali tespiti ile saatlik yükleme verilerini görselleştirme
plt.figure(figsize=(14, 7))
plt.plot(hourly_data.index, hourly_data['UPLOAD'], label='Upload')
anomalies_lof_upload = hourly_data[hourly_data['anomaly_lof_upload'] == -1]
plt.scatter(anomalies_lof_upload.index, anomalies_lof_upload['UPLOAD'], color='red', label='Anomaly (LOF)', marker='o')
plt.title('Hourly Upload Data with LOF Anomalies')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Upload Traffic')
plt.show()

# SVM anomali tespiti ile saatlik indirme verilerini görselleştirme
plt.figure(figsize=(14, 7))
plt.plot(hourly_data.index, hourly_data['DOWNLOAD'], label='Download')
anomalies_svm_download = hourly_data[hourly_data['anomaly_svm_download'] == -1]
plt.scatter(anomalies_svm_download.index, anomalies_svm_download['DOWNLOAD'], color='red', label='Anomaly (SVM)', marker='o')
plt.title('Hourly Download Data with SVM Anomalies')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Download Traffic')
plt.show()

# SVM anomali tespiti ile saatlik yükleme verilerini görselleştirme
plt.figure(figsize=(14, 7))
plt.plot(hourly_data.index, hourly_data['UPLOAD'], label='Upload')
anomalies_svm_upload = hourly_data[hourly_data['anomaly_svm_upload'] == -1]
plt.scatter(anomalies_svm_upload.index, anomalies_svm_upload['UPLOAD'], color='red', label='Anomaly (SVM)', marker='o')
plt.title('Hourly Upload Data with SVM Anomalies')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Upload Traffic')
plt.show()

# Verileri günlük frekansa göre yeniden örnekleme
daily_data = df.resample('D').sum()

# Local Outlier Factor (LOF) ile günlük verilerde anomali tespiti
daily_lof = LocalOutlierFactor(n_neighbors=35, contamination=0.01)
daily_data['anomaly_lof_download'] = daily_lof.fit_predict(daily_data[['DOWNLOAD']])
daily_data['anomaly_lof_upload'] = daily_lof.fit_predict(daily_data[['UPLOAD']])

# One-Class SVM ile günlük verilerde anomali tespiti
daily_svm = OneClassSVM(nu=0.05, kernel='rbf', gamma=0.01)
daily_data['anomaly_svm_download'] = daily_svm.fit_predict(daily_data[['DOWNLOAD']])
daily_data['anomaly_svm_upload'] = daily_svm.fit_predict(daily_data[['UPLOAD']])

# LOF anomali tespiti ile günlük indirme verilerini görselleştirme
plt.figure(figsize=(14, 7))
plt.plot(daily_data.index, daily_data['DOWNLOAD'], label='Download')
anomalies_lof_download_daily = daily_data[daily_data['anomaly_lof_download'] == -1]
plt.scatter(anomalies_lof_download_daily.index, anomalies_lof_download_daily['DOWNLOAD'], color='red', label='Anomaly (LOF)', marker='o')
plt.title('Daily Download Data with LOF Anomalies')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Download Traffic')
plt.show()

# LOF anomali tespiti ile günlük yükleme verilerini görselleştirme
plt.figure(figsize=(14, 7))
plt.plot(daily_data.index, daily_data['UPLOAD'], label='Upload')
anomalies_lof_upload_daily = daily_data[daily_data['anomaly_lof_upload'] == -1]
plt.scatter(anomalies_lof_upload_daily.index, anomalies_lof_upload_daily['UPLOAD'], color='red', label='Anomaly (LOF)', marker='o')
plt.title('Daily Upload Data with LOF Anomalies')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Upload Traffic')
plt.show()

# SVM anomali tespiti ile günlük indirme verilerini görselleştirme
plt.figure(figsize=(14, 7))
plt.plot(daily_data.index, daily_data['DOWNLOAD'], label='Download')
anomalies_svm_download_daily = daily_data[daily_data['anomaly_svm_download'] == -1]
plt.scatter(anomalies_svm_download_daily.index, anomalies_svm_download_daily['DOWNLOAD'], color='red', label='Anomaly (SVM)', marker='o')
plt.title('Daily Download Data with SVM Anomalies')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Download Traffic')
plt.show()

# SVM anomali tespiti ile günlük yükleme verilerini görselleştirme
plt.figure(figsize=(14, 7))
plt.plot(daily_data.index, daily_data['UPLOAD'], label='Upload')
anomalies_svm_upload_daily = daily_data[daily_data['anomaly_svm_upload'] == -1]
plt.scatter(anomalies_svm_upload_daily.index, anomalies_svm_upload_daily['UPLOAD'], color='red', label='Anomaly (SVM)', marker='o')
plt.title('Daily Upload Data with SVM Anomalies')
plt.legend()
plt.xlabel('Time')
plt.ylabel('Upload Traffic')
plt.show()

## TÜM VERİ SETİ İÇİN ISOLATION FOREST ANOMALİ TESPİTİ
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Veriyi yükle ve TIME_STAMP sütununu datetime formatına dönüştür
data = pd.read_excel('/yapay_zeka.xlsx')
data['TIME_STAMP'] = pd.to_datetime(data['TIME_STAMP'])

# Saat ve haftanın günü gibi ek özellikleri çıkar
data['HOUR'] = data['TIME_STAMP'].dt.hour
data['DAY_OF_WEEK'] = data['TIME_STAMP'].dt.dayofweek
data['IS_WEEKEND'] = data['DAY_OF_WEEK'].apply(lambda x: 1 if x >= 5 else 0)
data['IS_HOLIDAY'] = data['TIME_STAMP'].apply(lambda x: 1 if x.month == 1 and x.day == 1 else 0)

# Eksik değerleri geçmiş haftalardaki aynı günlerin aynı zamanlarının ortalamasını alarak doldurma
def fill_missing_values(df, column_name):
    for hour in range(24):
        for day in range(7):
            mask = (df['HOUR'] == hour) & (df['DAY_OF_WEEK'] == day)
            df.loc[mask, column_name] = df.loc[mask, column_name].fillna(df.loc[mask, column_name].mean())
    return df

data = fill_missing_values(data, 'DOWNLOAD')
data = fill_missing_values(data, 'UPLOAD')

# Isolation Forest algoritmasını uygula
iso_forest = IsolationForest(contamination=0.1, random_state=60)
features = ['DOWNLOAD', 'UPLOAD', 'HOUR', 'DAY_OF_WEEK', 'IS_HOLIDAY', 'IS_WEEKEND']
data['ANOMALY'] = iso_forest.fit_predict(data[features])

# Anomaliler -1 olarak işaretlenir, normal noktalar 1 olarak
data['ANOMALY'] = data['ANOMALY'].apply(lambda x: 1 if x == -1 else 0)


# Sonuçları görselleştir
plt.figure(figsize=(28, 12))
plt.plot(data['TIME_STAMP'], data['DOWNLOAD'], label='Download Trafiği', color='blue')
plt.scatter(data[data['ANOMALY'] == 1]['TIME_STAMP'], data[data['ANOMALY'] == 1]['DOWNLOAD'], color='red', label='Anomaliler')
plt.xlabel('Zaman')
plt.ylabel('Download Trafiği')
plt.title('Isolation Forest ile Anomali Tespiti')
plt.legend()
plt.show()

# Anomalileri inceleme
anomalies = data[data['ANOMALY'] == 1]


# Anomali noktalarının dağılımını görselleştir - Upload
plt.figure(figsize=(28, 12))
plt.plot(data['TIME_STAMP'], data['UPLOAD'], label='Upload Trafiği', color='green')
plt.scatter(anomalies['TIME_STAMP'], anomalies['UPLOAD'], color='red', label='Anomaliler')
plt.xlabel('Zaman')
plt.ylabel('Upload Trafiği')
plt.title('Isolation Forest ile Anomali Tespiti - Upload')
plt.legend()
plt.show()

#ISOLATION FOREST SON 2 GÜN ANOMALİ TESPİT ALGORİTMASI
import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

# Veriyi yükle ve TIME_STAMP sütununu datetime formatına dönüştür
data = pd.read_excel('/yapay_zeka.xlsx')
data['TIME_STAMP'] = pd.to_datetime(data['TIME_STAMP'])

# Saat ve haftanın günü gibi ek özellikleri çıkar
data['HOUR'] = data['TIME_STAMP'].dt.hour
data['DAY_OF_WEEK'] = data['TIME_STAMP'].dt.dayofweek
data['IS_WEEKEND'] = data['DAY_OF_WEEK'].apply(lambda x: 1 if x >= 5 else 0)
data['IS_HOLIDAY'] = data['TIME_STAMP'].apply(lambda x: 1 if x.month == 1 and x.day == 1 else 0)

# Eksik değerleri geçmiş haftalardaki aynı günlerin aynı zamanlarının ortalamasını alarak doldurma
def fill_missing_values(df, column_name):
    for hour in range(24):
        for day in range(7):
            mask = (df['HOUR'] == hour) & (df['DAY_OF_WEEK'] == day)
            df.loc[mask, column_name] = df.loc[mask, column_name].fillna(df.loc[mask, column_name].mean())
    return df

data = fill_missing_values(data, 'DOWNLOAD')
data = fill_missing_values(data, 'UPLOAD')

# Son 2 gün için veri seçimi
last_two_days = data[data['TIME_STAMP'] >= (data['TIME_STAMP'].max() - pd.Timedelta(days=2))]

# Isolation Forest algoritmasını uygula
iso_forest = IsolationForest(contamination=0.2, random_state=60)
features = ['DOWNLOAD', 'UPLOAD', 'HOUR', 'DAY_OF_WEEK', 'IS_HOLIDAY', 'IS_WEEKEND']
last_two_days['ANOMALY'] = iso_forest.fit_predict(last_two_days[features])

# Anomaliler -1 olarak işaretlenir, normal noktalar 1 olarak
last_two_days['ANOMALY'] = last_two_days['ANOMALY'].apply(lambda x: 1 if x == -1 else 0)

# Verinin en sonunda anomali olup olmadığını kontrol et
last_row = last_two_days.iloc[-1]


# Sonuçları görselleştir
plt.figure(figsize=(28, 12))
plt.plot(last_two_days['TIME_STAMP'], last_two_days['DOWNLOAD'], label='Download Trafiği', color='blue')
plt.scatter(last_two_days[last_two_days['ANOMALY'] == 1]['TIME_STAMP'], last_two_days[last_two_days['ANOMALY'] == 1]['DOWNLOAD'], color='red', label='Anomaliler')
plt.xlabel('Zaman')
plt.ylabel('Download Trafiği')
plt.title('Isolation Forest ile Anomali Tespiti - Son 2 Gün')
plt.legend()
plt.show()

# Anomalileri inceleme
anomalies = last_two_days[last_two_days['ANOMALY'] == 1]



# Anomali noktalarının dağılımını görselleştir - Upload
plt.figure(figsize=(28, 12))
plt.plot(last_two_days['TIME_STAMP'], last_two_days['UPLOAD'], label='Upload Trafiği', color='green')
plt.scatter(anomalies['TIME_STAMP'], anomalies['UPLOAD'], color='red', label='Anomaliler')
plt.xlabel('Zaman')
plt.ylabel('Upload Trafiği')
plt.title('Isolation Forest ile Anomali Tespiti - Son 2 Gün - Upload')
plt.legend()
plt.show()

import pandas as pd
from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt

# Excel dosyasını yükle
# Veriyi yükle ve TIME_STAMP sütununu datetime formatına dönüştür
df = pd.read_excel('/yapay_zeka.xlsx')
df['TIME_STAMP'] = pd.to_datetime(df['TIME_STAMP'])

# Anomali tespiti için verileri ön işleme
df['TIME_STAMP'] = pd.to_datetime(df['TIME_STAMP'])
df.set_index('TIME_STAMP', inplace=True)

# Verileri saatlik frekansa göre yeniden örnekleme
hourly_data = df.resample('H').sum()

# Saatlik veriler için One-Class SVM
svm = OneClassSVM(nu=0.05, kernel='rbf', gamma=0.01)
hourly_data['anomaly_svm_download'] = svm.fit_predict(hourly_data[['DOWNLOAD']])
hourly_data['anomaly_svm_upload'] = svm.fit_predict(hourly_data[['UPLOAD']])

# SVM anomali tespiti ile saatlik indirme verilerini görselleştirme
plt.figure(figsize=(14, 7))
plt.plot(hourly_data.index, hourly_data['DOWNLOAD'], label='Download')
anomalies_svm_download = hourly_data[hourly_data['anomaly_svm_download'] == -1]
plt.scatter(anomalies_svm_download.index, anomalies_svm_download['DOWNLOAD'], color='red', label='Anomaly (SVM)', marker='o')
plt.title('Saatlik İndirme Verileri ile SVM Anomalileri')
plt.legend()
plt.xlabel('Zaman')
plt.ylabel('İndirme Trafiği')
plt.show()

# SVM anomali tespiti ile saatlik yükleme verilerini görselleştirme
plt.figure(figsize=(14, 7))
plt.plot(hourly_data.index, hourly_data['UPLOAD'], label='Upload')
anomalies_svm_upload = hourly_data[hourly_data['anomaly_svm_upload'] == -1]
plt.scatter(anomalies_svm_upload.index, anomalies_svm_upload['UPLOAD'], color='red', label='Anomaly (SVM)', marker='o')
plt.title('Saatlik Yükleme Verileri ile SVM Anomalileri')
plt.legend()
plt.xlabel('Zaman')
plt.ylabel('Yükleme Trafiği')
plt.show()

# Verileri günlük frekansa göre yeniden örnekleme
daily_data = df.resample('D').sum()

# Günlük veriler için One-Class SVM
daily_svm = OneClassSVM(nu=0.01, kernel='rbf', gamma=0.001)
daily_data['anomaly_svm_download'] = daily_svm.fit_predict(daily_data[['DOWNLOAD']])
daily_data['anomaly_svm_upload'] = daily_svm.fit_predict(daily_data[['UPLOAD']])

# SVM anomali tespiti ile günlük indirme verilerini görselleştirme
plt.figure(figsize=(14, 7))
plt.plot(daily_data.index, daily_data['DOWNLOAD'], label='Download')
anomalies_svm_download_daily = daily_data[daily_data['anomaly_svm_download'] == -1]
plt.scatter(anomalies_svm_download_daily.index, anomalies_svm_download_daily['DOWNLOAD'], color='red', label='Anomaly (SVM)', marker='o')
plt.title('Günlük İndirme Verileri ile SVM Anomalileri')
plt.legend()
plt.xlabel('Zaman')
plt.ylabel('İndirme Trafiği')
plt.show()

# SVM anomali tespiti ile günlük yükleme verilerini görselleştirme
plt.figure(figsize=(14, 7))
plt.plot(daily_data.index, daily_data['UPLOAD'], label='Upload')
anomalies_svm_upload_daily = daily_data[daily_data['anomaly_svm_upload'] == -1]
plt.scatter(anomalies_svm_upload_daily.index, anomalies_svm_upload_daily['UPLOAD'], color='red', label='Anomaly (SVM)', marker='o')
plt.title('Günlük Yükleme Verileri ile SVM Anomalileri')
plt.legend()
plt.xlabel('Zaman')
plt.ylabel('Yükleme Trafiği')
plt.show()

## ONE CLASS SVM SON 2 GÜNÜN ANOMALİ TESPİTİ
import pandas as pd
from sklearn.svm import OneClassSVM
import matplotlib.pyplot as plt

# Veriyi yükle ve TIME_STAMP sütununu datetime formatına dönüştür
data = pd.read_excel('/yapay_zeka.xlsx')
data['TIME_STAMP'] = pd.to_datetime(data['TIME_STAMP'])

# Saat ve haftanın günü gibi ek özellikleri çıkar
data['HOUR'] = data['TIME_STAMP'].dt.hour
data['DAY_OF_WEEK'] = data['TIME_STAMP'].dt.dayofweek
data['IS_WEEKEND'] = data['DAY_OF_WEEK'].apply(lambda x: 1 if x >= 5 else 0)
data['IS_HOLIDAY'] = data['TIME_STAMP'].apply(lambda x: 1 if x.month == 1 and x.day == 1 else 0)

# Eksik değerleri geçmiş haftalardaki aynı günlerin aynı zamanlarının ortalamasını alarak doldurma
def fill_missing_values(df, column_name):
    for hour in range(24):
        for day in range(7):
            mask = (df['HOUR'] == hour) & (df['DAY_OF_WEEK'] == day)
            df.loc[mask, column_name] = df.loc[mask, column_name].fillna(df.loc[mask, column_name].mean())
    return df

data = fill_missing_values(data, 'DOWNLOAD')
data = fill_missing_values(data, 'UPLOAD')

# Son 2 gün için veri seçimi
last_two_days = data[data['TIME_STAMP'] >= (data['TIME_STAMP'].max() - pd.Timedelta(days=2))]

# One-Class SVM algoritmasını uygula
ocsvm = OneClassSVM(kernel='rbf', gamma=0.000001, nu=0.000001)
features = ['DOWNLOAD', 'UPLOAD', 'HOUR', 'DAY_OF_WEEK', 'IS_HOLIDAY', 'IS_WEEKEND']
ocsvm.fit(last_two_days[features])
last_two_days['ANOMALY'] = ocsvm.predict(last_two_days[features])

# Anomaliler -1 olarak işaretlenir, normal noktalar 1 olarak
last_two_days['ANOMALY'] = last_two_days['ANOMALY'].apply(lambda x: 1 if x == -1 else 0)

# Verinin en sonunda anomali olup olmadığını kontrol et
last_row = last_two_days.iloc[-1]


# Sonuçları görselleştir
plt.figure(figsize=(28, 12))
plt.plot(last_two_days['TIME_STAMP'], last_two_days['DOWNLOAD'], label='Download Trafiği', color='blue')
plt.scatter(last_two_days[last_two_days['ANOMALY'] == 1]['TIME_STAMP'], last_two_days[last_two_days['ANOMALY'] == 1]['DOWNLOAD'], color='red', label='Anomaliler')
plt.xlabel('Zaman')
plt.ylabel('Download Trafiği')
plt.title('One-Class SVM ile Anomali Tespiti - Son 2 Gün')
plt.legend()
plt.show()

# Anomalileri inceleme
anomalies = last_two_days[last_two_days['ANOMALY'] == 1]


# Anomali noktalarının dağılımını görselleştir - Upload
plt.figure(figsize=(28, 12))
plt.plot(last_two_days['TIME_STAMP'], last_two_days['UPLOAD'], label='Upload Trafiği', color='green')
plt.scatter(anomalies['TIME_STAMP'], anomalies['UPLOAD'], color='red', label='Anomaliler')
plt.xlabel('Zaman')
plt.ylabel('Upload Trafiği')
plt.title('One-Class SVM ile Anomali Tespiti - Son 2 Gün - Upload')
plt.legend()
plt.show()

#ISOLATION FOREST VE ONE CLASS SVM BİRLİKTE ANOMALİ TESPİTİ YAPMASI

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import OneClassSVM
from sklearn.ensemble import IsolationForest

# Veriyi yükle ve TIME_STAMP sütununu datetime formatına dönüştür
data = pd.read_excel('/yapay_zeka.xlsx')
data['TIME_STAMP'] = pd.to_datetime(data['TIME_STAMP'])

# Eksik değerleri median ile doldur
data['DOWNLOAD'].fillna(data['DOWNLOAD'].median(), inplace=True)
data['UPLOAD'].fillna(data['UPLOAD'].median(), inplace=True)

# Son 1 ay için veri seçimi
last_month = data[data['TIME_STAMP'] >= (data['TIME_STAMP'].max() - pd.Timedelta(days=2))]

# Özellikleri seçme
features = last_month[['DOWNLOAD', 'UPLOAD']]

# One-Class SVM algoritmasını uygula
ocsvm = OneClassSVM(kernel='rbf', gamma=0.001, nu=0.001)
last_month['ocsvm_anomaly'] = ocsvm.fit_predict(features)
last_month['ocsvm_anomaly'] = last_month['ocsvm_anomaly'].apply(lambda x: 1 if x == -1 else 0)

# Isolation Forest algoritmasını uygula
iso_forest = IsolationForest(contamination=0.001, random_state=42)
last_month['iso_forest_anomaly'] = iso_forest.fit_predict(features)
last_month['iso_forest_anomaly'] = last_month['iso_forest_anomaly'].apply(lambda x: 1 if x == -1 else 0)

# Ortak anomalileri ve farklı anomalileri belirleme
last_month['combined_anomaly'] = last_month.apply(lambda row: 1 if row['ocsvm_anomaly'] == 1 or row['iso_forest_anomaly'] == 1 else 0, axis=1)

# Anomalileri zaman serisinde görselleştir (DOWNLOAD)
plt.figure(figsize=(14, 7))
plt.plot(last_month['TIME_STAMP'], last_month['DOWNLOAD'], label='Download Trafiği', color='blue')
plt.scatter(last_month[last_month['combined_anomaly'] == 1]['TIME_STAMP'], last_month[last_month['combined_anomaly'] == 1]['DOWNLOAD'], color='red', label='Anomaliler')
plt.xlabel('Zaman')
plt.ylabel('Download Trafiği')
plt.title('One-Class SVM ve Isolation Forest ile Anomali Tespiti - Zaman Serisi (Download)')
plt.legend()
plt.show()

# Anomalileri zaman serisinde görselleştir (UPLOAD)
plt.figure(figsize=(14, 7))
plt.plot(last_month['TIME_STAMP'], last_month['UPLOAD'], label='Upload Trafiği', color='blue')
plt.scatter(last_month[last_month['combined_anomaly'] == 1]['TIME_STAMP'], last_month[last_month['combined_anomaly'] == 1]['UPLOAD'], color='red', label='Anomaliler')
plt.xlabel('Zaman')
plt.ylabel('Upload Trafiği')
plt.title('One-Class SVM ve Isolation Forest ile Anomali Tespiti - Zaman Serisi (Upload)')
plt.legend()
plt.show()

# Son bir ay için anomalileri inceleme
combined_anomalies = last_month[last_month['combined_anomaly'] == 1]
combined_anomalies_summary = combined_anomalies[['TIME_STAMP', 'DOWNLOAD', 'UPLOAD']]

# 1. Prophet kütüphanesini yükleme
!pip install prophet

# 2. Gerekli kütüphaneleri içe aktarma
import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

# 3. Veri yükleme ve ön işleme
data = pd.read_excel('/yapay_zeka.xlsx')
data['TIME_STAMP'] = pd.to_datetime(data['TIME_STAMP'])

# İndirme verisi için Prophet formatına dönüştürme
download_data = data[['TIME_STAMP', 'DOWNLOAD']].rename(columns={'TIME_STAMP': 'ds', 'DOWNLOAD': 'y'})

# Yükleme verisi için Prophet formatına dönüştürme
upload_data = data[['TIME_STAMP', 'UPLOAD']].rename(columns={'TIME_STAMP': 'ds', 'UPLOAD': 'y'})

# 4. Prophet modeli ile indirme trafiğini tahmin etme
download_model = Prophet()
download_model.fit(download_data)
download_future = download_model.make_future_dataframe(periods=30)
download_forecast = download_model.predict(download_future)

# 5. Prophet modeli ile yükleme trafiğini tahmin etme
upload_model = Prophet()
upload_model.fit(upload_data)
upload_future = upload_model.make_future_dataframe(periods=30)
upload_forecast = upload_model.predict(upload_future)

# 6. İndirme tahminini görselleştirme
fig1 = download_model.plot(download_forecast)
plt.title('Download Trafiği Tahmini')
plt.show()

# İndirme tahmin bileşenlerini görselleştirme
fig2 = download_model.plot_components(download_forecast)
plt.show()

# 7. Yükleme tahminini görselleştirme
fig3 = upload_model.plot(upload_forecast)
plt.title('Upload Trafiği Tahmini')
plt.show()

# Yükleme tahmin bileşenlerini görselleştirme
fig4 = upload_model.plot_components(upload_forecast)
plt.show()

!pip install prophet
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from prophet import Prophet

# Veriyi yükle ve TIME_STAMP sütununu datetime formatına dönüştür
data = pd.read_excel('/yapay_zeka.xlsx')
data['TIME_STAMP'] = pd.to_datetime(data['TIME_STAMP'])

# Prophet'in beklediği formatta veri hazırlığı
df_download = data[['TIME_STAMP', 'DOWNLOAD']].rename(columns={'TIME_STAMP': 'ds', 'DOWNLOAD': 'y'})
df_upload = data[['TIME_STAMP', 'UPLOAD']].rename(columns={'TIME_STAMP': 'ds', 'UPLOAD': 'y'})

# Prophet modelini oluştur ve eğit (Download için)
model_download = Prophet()
model_download.fit(df_download)
future_download = model_download.make_future_dataframe(periods=30, freq='D')  # 30 gün için tahmin
forecast_download = model_download.predict(future_download)

# Prophet modelini oluştur ve eğit (Upload için)
model_upload = Prophet()
model_upload.fit(df_upload)
future_upload = model_upload.make_future_dataframe(periods=30, freq='D')  # 30 gün için tahmin
forecast_upload = model_upload.predict(future_upload)

# Gerçek değerleri ve tahmin edilen değerleri birleştir (Download)
forecast_merged_download = pd.merge(future_download, forecast_download[['ds', 'yhat', 'yhat_lower', 'yhat_upper']], on='ds', how='left')
df_merged_download = pd.merge(df_download, forecast_merged_download, on='ds', how='outer')
df_merged_download['anomaly'] = df_merged_download.apply(lambda row: 1 if row['y'] > row['yhat_upper'] or row['y'] < row['yhat_lower'] else 0, axis=1)

# Gerçek değerleri ve tahmin edilen değerleri birleştir (Upload)
forecast_merged_upload = pd.merge(future_upload, forecast_upload[['ds', 'yhat', 'yhat_lower', 'yhat_upper']], on='ds', how='left')
df_merged_upload = pd.merge(df_upload, forecast_merged_upload, on='ds', how='outer')
df_merged_upload['anomaly'] = df_merged_upload.apply(lambda row: 1 if row['y'] > row['yhat_upper'] or row['y'] < row['yhat_lower'] else 0, axis=1)

# Download grafiği
plt.figure(figsize=(14, 7))
plt.plot(df_merged_download['ds'], df_merged_download['y'], label='Gerçek Değerler', color='blue')
plt.plot(df_merged_download['ds'], df_merged_download['yhat'], label='Tahmin Edilen Değerler', color='red')
plt.fill_between(df_merged_download['ds'], df_merged_download['yhat_lower'], df_merged_download['yhat_upper'], color='pink', alpha=0.3, label='Tahmin Aralığı')
plt.scatter(df_merged_download[df_merged_download['anomaly'] == 1]['ds'], df_merged_download[df_merged_download['anomaly'] == 1]['y'], color='black', label='Anomaliler', marker='o')
plt.xlabel('Zaman')
plt.ylabel('Download Trafiği')
plt.title('Prophet ile Anomali Tespiti - Gelecek 30 Gün (Download)')
plt.legend()
plt.show()

# Upload grafiği
plt.figure(figsize=(14, 7))
plt.plot(df_merged_upload['ds'], df_merged_upload['y'], label='Gerçek Değerler', color='blue')
plt.plot(df_merged_upload['ds'], df_merged_upload['yhat'], label='Tahmin Edilen Değerler', color='red')
plt.fill_between(df_merged_upload['ds'], df_merged_upload['yhat_lower'], df_merged_upload['yhat_upper'], color='pink', alpha=0.3, label='Tahmin Aralığı')
plt.scatter(df_merged_upload[df_merged_upload['anomaly'] == 1]['ds'], df_merged_upload[df_merged_upload['anomaly'] == 1]['y'], color='black', label='Anomaliler', marker='o')
plt.xlabel('Zaman')
plt.ylabel('Upload Trafiği')
plt.title('Prophet ile Anomali Tespiti - Gelecek 30 Gün (Upload)')
plt.legend()
plt.show()

# Anomalileri inceleme (Download)
anomalies_download = df_merged_download[df_merged_download['anomaly'] == 1]
print("Download Anomalileri")
print(anomalies_download[['ds', 'y', 'yhat', 'yhat_lower', 'yhat_upper', 'anomaly']])

# Anomalileri inceleme (Upload)
anomalies_upload = df_merged_upload[df_merged_upload['anomaly'] == 1]
print("Upload Anomalileri")
print(anomalies_upload[['ds', 'y', 'yhat', 'yhat_lower', 'yhat_upper', 'anomaly']])