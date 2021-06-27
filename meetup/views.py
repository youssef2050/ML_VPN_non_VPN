import threading
import time

from meetup.ML.RealTimeCapture import RealTimeCapture
from meetup.ML.KNN import KNN
from django.shortcuts import render


def index(request):
    # result= KNN.predict([[411416,2,0,44,0,22,22,22,0,0,0,0,0,106.9477123,4.86125965,411416,0,411416,411416,411416,411416,0,411416,411416,0,0,0,0,0,0,0,0,0,16,0,4.86125965,0,22,22,22,0,0,0,0,0,0,0,0,0,0,0,33,22,0,0,0,0,0,0,0,1,22,0,0,0,0,1,8,0,0,0,0,1.43E+15,0,1.43E+15,1.43E+15]])
    result = RealTimeCapture.getInterface
    return render(request, 'meetups/index.html', {'result': result})


def runTime(request, interface):
    if (interface == 'offline'):
        return render(request, 'meetups/uploadFile.html')
    else:
        data = [
            {'ip_src': '192.168.0.1', 'port_src': '5000', 'ip_dest': '29.168.15.205', 'port_dest': '80',
             'classifier': 'vpn'},
            {'ip_src': '192.168.0.1', 'port_src': '8080', 'ip_dest': '172.16.0.215', 'port_dest': '21',
             'classifier': 'non_vpn'},
            {'ip_src': '192.168.0.1', 'port_src': '5000', 'ip_dest': '29.168.15.205', 'port_dest': '80',
             'classifier': 'vpn'},
            {'ip_src': '192.168.0.1', 'port_src': '5000', 'ip_dest': '29.168.15.205', 'port_dest': '80',
             'classifier': 'vpn'},
            {'ip_src': '192.168.0.1', 'port_src': '5000', 'ip_dest': '29.168.15.205', 'port_dest': '80',
             'classifier': 'non_vpn'},
            {'ip_src': '192.168.0.1', 'port_src': '5000', 'ip_dest': '29.168.15.205', 'port_dest': '80',
             'classifier': 'non_vpn'},
        ]
        runLiveCapture(interface)
    return render(request, 'meetups/result.html', {
        'title': interface,
        'data': data,
        'close': True,
    })


def runLiveCapture(interface):
    local_time = time.time()
    RealTimeCapture.liveCapture(interface, local_time)


def stopCapture(request, interface):
    RealTimeCapture.closeCapture()
    data = [{'ip_src': '192.168.0.1', 'port_src': '5000', 'ip_dest': '29.168.15.205', 'port_dest': '80',
             'classifier': 'vpn'},
            {'ip_src': '192.168.0.1', 'port_src': '5000', 'ip_dest': '29.168.15.205', 'port_dest': '80',
             'classifier': 'non_vpn'},
            {'ip_src': '192.168.0.1', 'port_src': '5000', 'ip_dest': '29.168.15.205', 'port_dest': '80',
             'classifier': 'non_vpn'}, ]
    return render(request, 'meetups/result.html', {
        'title': interface,
        'data': data,
        'close': False,
    })
