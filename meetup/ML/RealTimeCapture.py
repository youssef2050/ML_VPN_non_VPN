import threading
import time

import pyshark as pyshark
import psutil


class RealTimeCapture:
    @staticmethod
    def getInterface():
        address = psutil.net_if_addrs()
        address.__setitem__('offline', 'Youssef Ezz-Eldeen Developer ML use python, Android and desktop use java')
        return address.keys()

    @staticmethod
    def liveCapture(interface, outputFilePath, time=120, packet_count=5000):
        global capture
        capture = pyshark.LiveCapture(interface=interface, output_file='uploads/files/' + str(outputFilePath) + '.pcap')
        t = threading.Thread(target=capture.sniff, kwargs={'timeout': time, 'packet_count': packet_count}, daemon=True)
        t.start()
        t.join()
        # GetFeatures.convertToCSV('uploads/files/' + str(outputFilePath) + '.pcap')

    @staticmethod
    def closeCapture():
        if capture is not None:
            capture.close()
        else:
            pass
