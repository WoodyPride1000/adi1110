import smbus
from mpu6050 import MPU6050
import time

# MPU6050のI2Cアドレス
MPU6050_ADDR = 0x68

# MPU6050が接続されているI2Cバスの番号
I2C_BUS_NUM = 1

# MPU6050オブジェクトの初期化
sensor = MPU6050(I2C_BUS_NUM, MPU6050_ADDR)

# ここでDMPを初期化します。
sensor.dmp_initialize()

print("MPU6050 initialized successfully! Ready for data acquisition.")

try:
    while True:
        # 加速度データの取得 (修正箇所)
        accel_data = sensor.get_acceleration() # <-- ここを修正
        # MPU6050_ACCEL_FS_2 (+/-2G) 用のスケールファクター (raw値をG単位に変換)
        accel_x_g = accel_data.x / 16384.0
        accel_y_g = accel_data.y / 16384.0
        accel_z_g = accel_data.z / 16384.0
        print(f"Accelerometer: X={accel_x_g:.2f} G, Y={accel_y_g:.2f} G, Z={accel_z_g:.2f} G")

        # 角速度データの取得 (修正箇所)
        gyro_data = sensor.get_rotation() # <-- ここを修正
        # dmp_initialize() で MPU6050_GYRO_FS_2000 に設定されるため、+/-2000deg/s 用のスケールファクター (raw値をdeg/s単位に変換)
        gyro_x_dps = gyro_data.x / 16.4
        gyro_y_dps = gyro_data.y / 16.4
        gyro_z_dps = gyro_data.z / 16.4
        print(f"Gyroscope: X={gyro_x_dps:.2f} °/s, Y={gyro_y_dps:.2f} °/s, Z={gyro_z_dps:.2f} °/s")

        # このライブラリでは、温度データを直接取得する公開メソッドがありません。
        # print("Temperature data not directly available via public methods in this library version.")

        print("-" * 30)
        time.sleep(0.1) # データ取得間隔を短くしてみました (DMPのサンプルレートにもよります)

except KeyboardInterrupt:
    print("\nProgram terminated by user.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
