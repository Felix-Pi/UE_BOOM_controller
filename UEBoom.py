import os


class Boom:
    def __init__(self, speacer_mac, client_mac):
        self.speacer_mac = speacer_mac
        self.client_mac = client_mac.replace(':', '')

    def on(self):
        command = 'sudo gatttool -i hci0 -b {} --char-write-req -a 0x0003 -n {}01'.format(self.speacer_mac,
                                                                                          self.client_mac)
        os.system(command)

    def off(self):
        command = 'sudo gatttool -i hci0 -b {} --char-write-req -a 0x0003 -n {}02'.format(self.speacer_mac,
                                                                                          self.client_mac)

        os.system(command)

    def get_battery(self):
        command = 'sudo gatttool -i hci0 -b {} --char-read --uuid 0x2a19 | grep -oP \'(?<=value: )(.*?)(?=$)\''.format(
            self.speacer_mac)

        return os.popen(command).read()
