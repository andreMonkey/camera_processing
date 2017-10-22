#!/bin/bash

## execute command for websocket subscription
#sh ./unsubscribe.sh ble987BF3738084 PULSE

# discover bluetooth devices
sh ./discover.sh

# register oximeter 
sh ./registerDevice.sh 98:7B:F3:73:80:84 Oximeter

# Give it time to register
sleep 2

# execute command for websocket subscription
sh ./subscribe.sh ble987BF3738084 PULSE

