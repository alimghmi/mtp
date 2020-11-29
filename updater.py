import os
import time

SERVER = ['95.217.129.65', '168.119.153.11']

RECV_PORT = {
            '168.119.153.11': [717, 555, 515, 777, 818],
            '95.217.129.65': [919, 999, 1111, 2222, 1221]
            }

PRECALL = '''
sysctl -w net.ipv4.ip_forward=1;
sysctl net.ipv4.ip_forward;
iptables -P INPUT ACCEPT;
iptables -P FORWARD ACCEPT;
iptables -P OUTPUT ACCEPT;
iptables -t nat -F;
iptables -t mangle -F;
iptables -F;
iptables -X;
echo "1" > /proc/sys/net/ipv4/ip_forward;
'''.replace('\n', '')
CALL = 'iptables -t nat -A PREROUTING -p tcp --dport {} -j DNAT --to-destination {}:443;'
ENDCALL = 'iptables -t nat -A POSTROUTING ! -s 127.0.0.1 -j MASQUERADE'

def main():
    while True:
        os.system(PRECALL)
        #time.sleep(1)
        print('+ PORTFORWARDING RESETED')

        for s in SERVER:
            for p in RECV_PORT[s]:
                sc = CALL.format(p, s)
                print(':: {} || {}:443'.format(p, s))
                os.system(sc)

        os.system(ENDCALL)
        print('+ PORTFORWARDING SETTINGS SAVED')
        time.sleep(60 * 15)


if __name__ == '__main__':
    main()
