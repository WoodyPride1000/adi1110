import smbus
from mpu6050 import MPU6050
import time # データ取得間隔のために追加

# MPU6050のI2Cアドレス
MPU6050_ADDR = 0x68

# MPU6050が接続されているI2Cバスの番号
# Raspberry Piでは通常1です。
I2C_BUS_NUM = 1

# MPU6050オブジェクトの初期化
sensor = MPU6050(I2C_BUS_NUM, MPU6050_ADDR)

print("MPU6050 initialized successfully!")

try:
    while True:
        # 温度データの取得
        temp = sensor.get_temp()
        print(f"Temperature: {temp:.2f} °C")

        # 加速度データの取得
        accel_data = sensor.get_accel_data()
        print(f"Accelerometer: X={accel_data['x']:.2f}, Y={accel_data['y']:.2f}, Z={accel_data['z']:.2f} G")

        # 角速度データの取得
        gyro_data = sensor.get_gyro_data()
        print(f"Gyroscope: X={gyro_data['x']:.2f}, Y={gyro_data['y']:.2f}, Z={gyro_data['z']:.2f} °/s")

        print("-" * 30)
        time.sleep(1) # 1秒待機してから次のデータを取得

except KeyboardInterrupt:
    print("\nProgram terminated by user.")
except Exception as e:
    print(f"An error occurred: {e}")
