import json
import threading
import time

from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse

from meetup.ML.CICFlowMeterFeatures.GetFeatures import convertToCSV
from meetup.ML.RealTimeCapture import RealTimeCapture
from meetup.ML.BGTs import BGTs
from django.shortcuts import render

from meetup.models import Files, ResultML


def index(request):
    # result= BGTs.predict([[658,1,1,33,345,33,33,33,0,345,345,345,0,574468.09,3039.51,658,0,658,658,0,0,0,0,0,0,0,0,0,0,0,0,0,0,8,8,1519.76,1519.76,33,345,137,180.13,32448,0,0,0,0,0,0,0,0,1,205.5,33,345,0,0,0,0,0,0,0,16,0,172,0,0,0,8,0,0,0,0,1.43E+15,0,1.43E+15,1.43E+15]])
    result = RealTimeCapture.getInterface
    return render(request, 'meetups/index.html', {'result': result})


def runTime(request, interface):
    if interface == 'offline':
        return render(request, 'meetups/uploadFile.html')
    else:
        convertToCSV('uploads/files/csv/test.csv')
        data = Files.objects.all()
        return render(request, 'meetups/result.html', {
            'title': interface,
            'data': data,
            'close': True,
        })


def runLiveCapture(request):
    local_time = time.time()
    RealTimeCapture.liveCapture(request.GET.get('interface'), local_time)
    file = Files(name=local_time, file='files/' + str(local_time) + '.pcap')
    file.save()
    return JsonResponse(['is run capture'])


def stopCapture(request, interface):
    RealTimeCapture.closeCapture()
    date = ResultML.objects.all()
    return render(request, 'meetups/result.html', {
        'title': interface,
        'close': False,
        'data': date
    })


def getData(request):
    res = ResultML.objects.all()
    data = serialize("json", res, fields=('ip_src', 'port_src', 'ip_des', 'port_des', 'classification'))
    return HttpResponse(data, content_type="application/json")
