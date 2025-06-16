import smbus
from mpu6050 import MPU6050
import time

# MPU6050のI2Cアドレス
MPU6050_ADDR = 0x68

# MPU6050が接続されているI2Cバスの番号
I2C_BUS_NUM = 1

# MPU6050オブジェクトの初期化
# このライブラリは、内部的にDMPを使用するため、
# MPU6050オブジェクトの初期化後にDMPの初期化を行う必要があります。
sensor = MPU6050(I2C_BUS_NUM, MPU6050_ADDR)

# ここでDMPを初期化します。
# このライブラリはDMPを利用することを前提としているようです。
sensor.dmp_initialize()

print("MPU6050 initialized successfully! Ready for data acquisition.")

try:
    while True:
        # 加速度データの取得
        # get_acceleration() は V (XYZVector) オブジェクトを返します
        accel_data = sensor.get_acceleration()
        # 加速度の値はrawデータなので、適切なスケールファクターでG単位に変換する必要がある場合があります。
        # MPU6050_ACCEL_FS_2 が設定されている場合、2Gレンジなので 16384.0 で割ると G になります。
        accel_x_g = accel_data.x / 16384.0
        accel_y_g = accel_data.y / 16384.0
        accel_z_g = accel_data.z / 16384.0
        print(f"Accelerometer: X={accel_x_g:.2f} G, Y={accel_y_g:.2f} G, Z={accel_z_g:.2f} G")

        # 角速度データの取得
        # get_rotation() も V (XYZVector) オブジェクトを返します
        # MPU6050_GYRO_FS_250 が設定されている場合、250deg/sレンジなので 131.0 で割ると deg/s になります。
        # あなたのライブラリの__init__では MPU6050_GYRO_FS_250 が使われていますが、
        # dmp_initialize() では MPU6050_GYRO_FS_2000 に設定されています。
        # どちらが適用されているかによって、適切なスケールファクターは変わります。
        # dmp_initializeが後なので、2000 deg/sレンジと仮定して 16.4 で割ります。
        gyro_data = sensor.get_rotation()
        gyro_x_dps = gyro_data.x / 16.4
        gyro_y_dps = gyro_data.y / 16.4
        gyro_z_dps = gyro_data.z / 16.4
        print(f"Gyroscope: X={gyro_x_dps:.2f} °/s, Y={gyro_y_dps:.2f} °/s, Z={gyro_z_dps:.2f} °/s")

        # このライブラリでは、温度データを直接取得する公開メソッドがありません。
        # もし必要であれば、MPU6050のレジスタマップを直接読み込む必要がありますが、
        # 通常は加速度や角速度が主な目的です。
        # print("Temperature data not directly available via public methods in this library version.")

        print("-" * 30)
        time.sleep(0.1) # データ取得間隔を短くしてみました (DMPのサンプルレートにもよります)

except KeyboardInterrupt:
    print("\nProgram terminated by user.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
