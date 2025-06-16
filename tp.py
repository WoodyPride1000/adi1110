import smbus
from mpu6050 import MPU6050

# MPU6050のI2Cアドレス
MPU6050_ADDR = 0x68

# MPU6050が接続されているI2Cバスの番号
# Raspberry Piでは通常1です。
# 確実に確認するには、コマンドラインで `ls /dev/i2c*` を実行してください。
# `i2c-1` が見つかれば `1` を使用します。
I2C_BUS_NUM = 1 

# MPU6050オブジェクトの初期化
# 最初の引数にバス番号、2番目の引数にデバイスアドレスを指定します。
sensor = MPU6050(I2C_BUS_NUM, MPU6050_ADDR)

# ここからMPU6050を使用するコードを記述
print("MPU6050 initialized successfully!")
# 例: 加速度データの取得
# accel_data = sensor.get_accel_data()
# print(f"Accelerometer data: {accel_data}")
