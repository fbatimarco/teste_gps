import requests
import time
import json


def getSerial():
    cpuserial = ''
    try:
        with open ('/proc/cpuinfo', 'r') as f:
        # f = open('/proc/cpuinfo', 'r')
            for line in f:
                if line[0:6] == 'Serial':
                    cpuserial = line[10:26]
            f.close()
    except:
        cpuserial = 'Error'
    return cpuserial


latitude = -22
longitude = -42

aumento = 0.03

url = "https://api-operacao.dev.buspay.com.br/Geolocalizacao"

while True:
    print(str(latitude))
    
    string_geo = str(latitude) + "," + str(longitude)
    serial = str(getSerial())
    #serial = '1000000004714cb0'

    payload = {'caixaMagicaId': serial, 'operadoraId': 4, 'linhaId':51, 'geolocalizacao': string_geo, 'sentidoViagem': 1}
    print(payload)
    headers = {'Content-Type': 'application/json'}

    r = requests.put(url, data=json.dumps(payload), headers=headers)
    print(r)

    latitude = latitude + aumento
    longitude = longitude + aumento
    time.sleep(5)

