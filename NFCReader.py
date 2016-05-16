#!/usr/bin/env python


import RPi.GPIO as GPIO
import spi
import signal
import time
import MFRC522

class NFCReader(object):

    def __init__(self):
        self.uid = None
        MIFAREReader = MFRC522.MFRC522()

    def is_card_present(self):
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        print "TagType", TagType
        return self.uid

    def read_uid(self):
        (status,uid) = MIFAREReader.MFRC522_Anticoll()
        print "uid", uid
        return self.uid
