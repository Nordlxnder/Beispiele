#!/bin/bash

sudo ip addr add 192.168.100.100/24 dev enp56s0f4u1u2
sudo ip link set enp56s0f4u1u2 up
sudo systemctl start dnsmasq

echo "Forward aktivieren!"

echo 'echo 1 > /proc/sys/net/ipv4/ip_forward'
sudo -s
sudo iptables -t nat -A POSTROUTING -o enp27s0 -j MASQUERADE
