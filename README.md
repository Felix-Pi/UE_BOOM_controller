# UE_BOOM_controller
> Python script for controlling (turn ON/OFF) ue boom speaker and getting its current battery level

Tested on ue boom version 1

## Prerequisites

```
gatttool
```

### Usefull links: 
* https://www.jaredwolff.com/get-started-with-bluetooth-low-energy/
* https://github.com/pcborenstein/bluezDoc/wiki/hcitool-and-gatttool-example

## Usage
```python
boom = Boom('DEVICE_MAC', 'CLIENT_MAC')
#DEVICE_MAC: speakers MAC address, format: XX:XX:XX:XX:XX:XX
#CLIENT_MAC: MAC address of a device that already has been connected to the speaker, format: XX:XX:XX:XX:XX:XX

boom.on() #turns speaker on

boom.off() #turn speaker off

battery_level = boom.get_battery() #returns speakers battery level
```


## Gatttool usage
<pre><code>
Usage: sudo gatttool [OPTIONS]

Paramater:
  SPEAKER_MAC    speakers mac address, format: <b>XX:XX:XX:XX:XX:XX</b>
  CLIENT_MAC     mac address of a client that has already been connected to speaker,
                 format: <b>XXXXXXXXXXXX</b>
  
Commands:  
  <b>on</b>
    sudo gatttool -i hci0 -b SPEAKER_MAC --char-write-req -a 0x0003 -n CLIENT_MAC<b>01</b>
 
  <b>off</b>
    sudo gatttool -i hci0 -b SPEAKER_MAC --char-write-req -a 0x0003 -n CLIENT_MAC<b>02</b>
    
  <b>battery_level</b>
    sudo gatttool -i hci0 -b SPEAKER_MAC --char-read --uuid 0x2a19
  
</code></pre>


## Credits
* Source of gatttool commands ([reddit](https://www.reddit.com/r/shortcuts/comments/dz9zun/finally_turn_on_ue_boom_bluetooth_speaker/))
