import serial
import time


def read_voltage(port='COM3', baud_rate=9600, nplc=None):
    # Ініціалізуємо ser як None перед спробою відкрити з'єднання
    ser = None
    try:
        # Відкриваємо з'єднання через COM-порт
        ser = serial.Serial(port, baud_rate, timeout=1)

        # Чекаємо, поки Arduino скине
        time.sleep(2)

        # Очищаємо буфер введення
        ser.flushInput()

        # Безкінечний цикл для постійного вимірювання напруги
        while True:
            # Відсилаємо значення NPLC до Arduino
            ser.write(str(nplc).encode())

            # Зчитуємо значення напруги з Arduino
            voltage = ser.readline().decode().strip()

            # Друкуємо виміряну напругу
            print(f"Напруга: {voltage} V")

            # Регулюємо затримку між вимірюваннями за необхідності
            time.sleep(1)

    except serial.SerialException as e:
        # Обробляємо помилки серійного зв'язку
        print(f"Помилка: {e}")

    finally:
        # Перевірка, чи з'єднання існує перед його закриттям
        if ser is not None:
            ser.close()
        else:
            print("З'єднання не було встановлено.")


# Точка входу в скрипт
if __name__ == "__main__":
    # Викликаємо функцію read_voltage зі значеннями за замовчуванням
    read_voltage(nplc=1)
    read_voltage(nplc=5)
    read_voltage(nplc=10)
