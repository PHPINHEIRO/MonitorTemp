# MonitorTemp

Um simples sistema de supervisao de temperatura feito em python usando Tkinter + pySerial + arduino + LM35


Dependencia:
 - pip install pyserial
 
Como usar:
 - Baixa os arquivos
 - Grave o sketch/sensorTemp/sensorTemp.ino em seu Arduino
 - Verifique qual porta o Arduino esta conectada e coloque em "arduino = Serial("Arduino_porta",9600)" no arquivo "TempMonitor.py"
 - Execute o arquivo app.py
