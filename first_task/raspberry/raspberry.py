import serial
import time

# Design Python script for measuring voltage (can use Raspberry or Arduino as measuring device
# and communicate via COM port):
# a. Input range 0..3.3V
# b. NPLC: 1, 5, 10

# Налаштування COM-порту
ser = serial.Serial('COMx', 9600, timeout=1)  # Замініть 'COMx' на відповідний порт


def measure_voltage(nplc):
    # Відправлення команди на вимірювання напруги з вказаною NPLC
    command = f'MEASURE:VOLTAGE:DC? {nplc}\n'
    ser.write(command.encode())

    # Затримка для читання результатів
    time.sleep(1)

    # Отримання та виведення результатів
    result = ser.readline().decode().strip()
    print(f'Measured Voltage (NPLC={nplc}): {result} V')


# Вимірювання з різними значеннями NPLC
measure_voltage(1)
measure_voltage(5)
measure_voltage(10)

# Закриття COM-порту
ser.close()
