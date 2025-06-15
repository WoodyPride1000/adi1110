ステップバイステップ：MACアドレスでIPアドレスを固定

1. .network ファイルの作成（例: /etc/systemd/network/10-adin.network）
[Match]
MACAddress=ca:2f:b7:10:23:63

[Network]
Address=192.168.1.10/24
Gateway=192.168.1.1
DNS=8.8.8.8
MACAddress で対象のインターフェースを識別。
Address は IP アドレス（CIDR 形式）。
Gateway, DNS は任意（ルーティング必要なら設定）。
2. .link ファイル（オプション）
これは インターフェース名の固定やMAC変更などに使います。以下は例：

# /etc/systemd/network/10-adin.link
[Match]
MACAddress=ca:2f:b7:10:23:63

[Link]
Name=adin0
MACAddress=02:00:00:00:00:01
Name= でインターフェース名を固定（例: adin0）。
MACAddress=（下段）はソフト的にMACアドレスを変更する場合。
3. 有効化と反映
sudo systemctl enable systemd-networkd
sudo systemctl restart systemd-networkd
4. 状態確認
networkctl status
ip addr show
🔎 備考

.network → IPアドレス、ルーティング、DNSなど ネットワーク設定
.link → インターフェース名や MAC変更など リンク設定
✅ まとめ：IPアドレスを設定したい場合は .network ファイルが必要

[Match]
MACAddress=ca:2f:b7:10:23:63

[Network]
Address=192.168.100.10/24
Gateway=192.168.100.1
DNS=8.8.8.8
