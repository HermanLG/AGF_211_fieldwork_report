import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import xarray as xr


def Bohemanneset_UNIS_weather_station():
    """

    :return:
    """


# Download the data from thredds MET with xr.open_dataset(
# "https://thredds.met.no/thredds/dodsC/met.no/observations/unis/lighthouse_AWS_Bohemanneset_10min") as f:
# f.to_netcdf("C:/Users/Herma/PycharmProjects/AGF_211_fieldwork_report/src/data_python/salinity/bohemannneset_UNIS_station.nc")

df = xr.open_dataset("bohemannneset_UNIS_station.nc")
# print(df.temperature.values)
a = df.time.values

for i in range(len(a)):
    if a[i] == np.datetime64('2023-03-01T10:00:00.000000000'):
        index_of_03_01 = i

temp_03_01to04_16 = df.temperature.values[index_of_03_01:]


plt.plot(df.time[60200:], df.temperature.values[60200:])
plt.title("Temperature observation in Bohemanneset from 2023-03-01 to 2023-04-16")
plt.xlabel("Date [yyyy-mm-dd]")
plt.ylabel("Temperature [$C^{\circ}$]")
plt.grid()
plt.show()


def frost_api():
    client_id = "6839b8bc-e2f0-4651-be5f-c9847ce87b9b"
    client_secret = "93ffd4b1-5085-4f3a-9aae-12423f0e5727"

    source_slh = "SN99840"  # Svalbard LH
    source_ifr = "SN99790"  # Isfjord radio
    source_pyr = "SN99880"  # Pyramiden weather station

    old_ref_time = 'R29/1981-10-01/1982-04-01/P1Y'
    ref_time = "2023-03-01/2023-04-16"

    freeze_temp = -1.8  # celsius

    HTTP_link = 'https://frost.met.no/observations/v0.jsonld'
    parameters = {
        'sources': source_slh,
        'elements': "mean(air_temperature P1D)",
        'referencetime': ref_time,
        "timeresolutions": "P1D",
        "timeoffsets": "default"}

    # HTTP get request
    request = requests.get(HTTP_link, parameters, auth=(client_id, ''))

    if request.status_code == 200:
        data = request.json()['data']
        print('Data retrieved from frost.met.no!')
    else:
        print('Error! Returned status code %s' % request.status_code)
        print('Message: %s' % request.json()['error']['message'])
        print('Reason: %s' % request.json()['error']['reason'])

    df = pd.DataFrame()

    # JSON to df
    for i in range(len(data)):
        row = pd.DataFrame(data[i]['observations'])
        row['referenceTime'] = data[i]['referenceTime']
        row['sourceId'] = data[i]['sourceId']
        df = pd.concat([df, row])

    print(df)
    """
    columns = ['sourceId', 'referenceTime', 'elementId', 'value', 'unit', 'timeOffset']
    df2 = df[columns].copy()

    df2['referenceTime'] = pd.to_datetime(df2['referenceTime'])
    """

    # print(df.keys())
    # print(df["value"], df["referenceTime"])
    mean_temp = np.array(df["value"])
    date = np.array(df["referenceTime"])

    # print(date)
    # print(mean_temp)

    # 5285
    # 1470

    degree_days = np.array(freeze_temp - mean_temp)

    print(sum(degree_days) / (2010 - 1981))
    print(sum(degree_days) / len(degree_days))

    # plt.plot(freeze_temp - mean_temp)
    # plt.show()
