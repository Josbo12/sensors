
#!/usr/bin/env python
# -*- coding: utf8 -*-
import RPi.GPIO as GPIO
import time, sys


class FlowControl(object):
    """Controling FlowControl"""
    def __init__(self):
        super(FlowControl, self).__init__()
        self.previousTime = 0
        self.count = 0
        self.litres = 0
        self.litres_decimal = 0
        self.service = 0
        self.total = 0

    def _get_user(self):
        print "llegeixo nfc"

    def update(self, channel):
        tim = time.time()
        delta = tim - self.previousTime
        if delta < 0.5:
            self.count = self.count+1
            self.litres =(self.count/450.0)
            service = '%.3f' % self.litres
            self.service += service
            self.total += service
            print "service =", service
            print "self.service =", self.service
            print "self.total =", self.total
        else:
            self.service = 0
            self.user = self._get_user()

        self.previousTime = tim

if __name__ == "__main__":
    f1= FlowControl()

    FLOW_SENSOR = 23
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(FLOW_SENSOR, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
    GPIO.add_event_detect(FLOW_SENSOR, GPIO.RISING, callback=f1.update)


    while True:
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print '\ncaught keyboard interrupt!, bye'
            GPIO.cleanup()
            sys.exit()
