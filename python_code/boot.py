# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)

import webrepl
import network

ap_if = network.WLAN(network.AP_IF)
ap_if.active(True)  #hotspot

#Set Hotspot name and password
ap_if.config(essid='ESP328266',password=b"12345678",channel=1,authmode=network.AUTH_WPA_WPA2_PSK)

webrepl.start()