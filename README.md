# UE_BOOM_controller
Python script for controlling (turn ON/OFF) ue boom speaker and getting its current battery level. (Tested on ue boom version 1)

### Prerequisites

```
gatttool
```

usefull links: 
* https://www.jaredwolff.com/get-started-with-bluetooth-low-energy/
* https://github.com/pcborenstein/bluezDoc/wiki/hcitool-and-gatttool-example

##How to use
```python
boom = Boom('DEVICE_MAC', 'CLIENT_MAC')
#DEVICE_MAC: speakers MAC address, format: XX:XX:XX:XX:XX:XX
#CLIENT_MAC: MAC address of a device that already has been connected to the speaker, format: XX:XX:XX:XX:XX:XX

boom.on() #turns speaker on

boom.off() #turn speaker off

battery_level = boom.get_battery() #returns speakers battery level
```


## Usage of gatttool 
`XX:XX:XX:XX:XX:XX` speakers MAC address
### ON
``sudo gatttool -i hci0 -b XX:XX:XX:XX:XX:XX --char-write-req -a 0x0003 -n XXXXXXXXXXXX01``

`0x0003` service handle

`XXXXXXXXXXXX` clients MAC address (without :) followed by **01**

### OFF
``sudo gatttool -i hci0 -b XX:XX:XX:XX:XX:XX --char-write-req -a 0x0003 -n XXXXXXXXXXXX01``

`0x0003` service handle

`XXXXXXXXXXXX` clients MAC address (without :) followed by **02**

### battery level
``sudo gatttool -i hci0 -b XX:XX:XX:XX:XX:XX --char-read --uuid 0x2a19``

`XX:XX:XX:XX:XX:XX` speakers MAC address

`0x2a19` service handle


## Sources
Source of gatttool commands: https://www.reddit.com/r/shortcuts/comments/dz9zun/finally_turn_on_ue_boom_bluetooth_speaker/