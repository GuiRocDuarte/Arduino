import serial
import csv
import time
from datetime import datetime


def lerDados():
    ser = serial.Serial("/dev/ttyUSB0", 9600, timeout=1800) # 30: 1800 | 5: 300

    with open('dados.csv', mode='a', newline='') as arquivo_csv:
        campo_nomes = ["QualidadeAr(PPM)", "Temperatura", "Umidade", "Data", "Hora", "Localizacao"]
        escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campo_nomes)

        # Se o arquivo CSV estiver vazio, escreva o cabeçalho
        if arquivo_csv.tell() == 0:
            escritor_csv.writeheader()
        
        i=0

        while i < 5:
            try:
                ler = ser.readline()
                ler_str = ler.decode('utf8').strip()
                ler_str = ler_str.split(',')
                dados = {
                    "QualidadeAr(PPM)": ler_str[0],
                    "Temperatura": ler_str[1],
                    
                    "Umidade": ler_str[2],
                    "Data": datetime.now().strftime("%Y/%m/%d"),
                    "Hora": datetime.now().strftime("%H:%M:%S"),
                    # Jardins Mangueiral | Tororó | Asa Sul -> MODIFICAR NO APP ARDUINO TAMBÉM
                    "Localizacao": "Jardins Mangueiral"
                }
                print(dados)
                i+=1
                escritor_csv.writerow(dados)
            except Exception as error:
                print("Falhou!", error)
                continue
                
        ser.close()


while True:
    lerDados()
    time.sleep(1798) # 30: 1798 | 5: 298