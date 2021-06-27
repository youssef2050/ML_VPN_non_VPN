import os
import sklearn
from sklearn.utils import shuffle
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np
from sklearn import linear_model, preprocessing
class KNN:
    @staticmethod
    def KNNModel():
        data = pd.read_csv('meetup/ML/output.csv')
        le = preprocessing.LabelEncoder()
        FlowDuration = le.fit_transform(list(data["FlowDuration"]))
        TotalFwdPacket = le.fit_transform(list(data["TotalFwdPacket"]))
        TotalBwdpackets = le.fit_transform(list(data["TotalBwdpackets"]))
        TotalLengthofFwdPacket = le.fit_transform(list(data["TotalLengthofFwdPacket"]))
        TotalLengthofBwdPacket = le.fit_transform(list(data["TotalLengthofBwdPacket"]))
        FwdPacketLengthMax = le.fit_transform(list(data["FwdPacketLengthMax"]))
        FwdPacketLengthMin = le.fit_transform(list(data["FwdPacketLengthMin"]))
        FwdPacketLengthMean = le.fit_transform(list(data["FwdPacketLengthMean"]))
        FwdPacketLengthStd = le.fit_transform(list(data["FwdPacketLengthStd"]))
        BwdPacketLengthMax = le.fit_transform(list(data["BwdPacketLengthMax"]))
        BwdPacketLengthMin = le.fit_transform(list(data["BwdPacketLengthMin"]))
        BwdPacketLengthMean = le.fit_transform(list(data["BwdPacketLengthMean"]))
        BwdPacketLengthStd = le.fit_transform(list(data["BwdPacketLengthStd"]))
        FlowBytes_s = le.fit_transform(list(data["FlowBytes_s"]))
        FlowPackets_s = le.fit_transform(list(data["FlowPackets_s"]))
        FlowIATMean = le.fit_transform(list(data["FlowIATMean"]))
        FlowIATStd = le.fit_transform(list(data["FlowIATStd"]))
        FlowIATMax = le.fit_transform(list(data["FlowIATMax"]))
        FlowIATMin = le.fit_transform(list(data["FlowIATMin"]))
        FwdIATTotal = le.fit_transform(list(data["FwdIATTotal"]))
        FwdIATMean = le.fit_transform(list(data["FwdIATMean"]))
        FwdIATStd = le.fit_transform(list(data["FwdIATStd"]))
        FwdIATMax = le.fit_transform(list(data["FwdIATMax"]))
        FwdIATMin = le.fit_transform(list(data["FwdIATMin"]))
        BwdIATTotal = le.fit_transform(list(data["BwdIATTotal"]))
        BwdIATMean = le.fit_transform(list(data["BwdIATMean"]))
        BwdIATStd = le.fit_transform(list(data["BwdIATStd"]))
        BwdIATMax = le.fit_transform(list(data["BwdIATMax"]))
        BwdIATMin = le.fit_transform(list(data["BwdIATMin"]))
        FwdPSHFlags = le.fit_transform(list(data["FwdPSHFlags"]))
        BwdPSHFlags = le.fit_transform(list(data["BwdPSHFlags"]))
        FwdURGFlags = le.fit_transform(list(data["FwdURGFlags"]))
        BwdURGFlags = le.fit_transform(list(data["BwdURGFlags"]))
        FwdHeaderLength = le.fit_transform(list(data["FwdHeaderLength"]))
        BwdHeaderLength = le.fit_transform(list(data["BwdHeaderLength"]))
        FwdPackets_s = le.fit_transform(list(data["FwdPackets_s"]))
        BwdPackets_s = le.fit_transform(list(data["BwdPackets_s"]))
        PacketLengthMin = le.fit_transform(list(data["PacketLengthMin"]))
        PacketLengthMax = le.fit_transform(list(data["PacketLengthMax"]))
        PacketLengthMean = le.fit_transform(list(data["PacketLengthMean"]))
        PacketLengthStd = le.fit_transform(list(data["PacketLengthStd"]))
        PacketLengthVariance = le.fit_transform(list(data["PacketLengthVariance"]))
        FINFlagCount = le.fit_transform(list(data["FINFlagCount"]))
        SYNFlagCount = le.fit_transform(list(data["SYNFlagCount"]))
        RSTFlagCount = le.fit_transform(list(data["RSTFlagCount"]))
        PSHFlagCount = le.fit_transform(list(data["PSHFlagCount"]))
        ACKFlagCount = le.fit_transform(list(data["ACKFlagCount"]))
        URGFlagCount = le.fit_transform(list(data["URGFlagCount"]))
        CWRFlagCount = le.fit_transform(list(data["CWRFlagCount"]))
        ECEFlagCount = le.fit_transform(list(data["ECEFlagCount"]))
        Down_UpRatio = le.fit_transform(list(data["Down_UpRatio"]))
        AveragePacketSize = le.fit_transform(list(data["AveragePacketSize"]))
        FwdSegmentSizeAvg = le.fit_transform(list(data["FwdSegmentSizeAvg"]))
        BwdSegmentSizeAvg = le.fit_transform(list(data["BwdSegmentSizeAvg"]))
        FwdBytes_BulkAvg = le.fit_transform(list(data["FwdBytes_BulkAvg"]))
        FwdPacket_BulkAvg = le.fit_transform(list(data["FwdPacket_BulkAvg"]))
        FwdBulkRateAvg = le.fit_transform(list(data["FwdBulkRateAvg"]))
        BwdBytes_BulkAvg = le.fit_transform(list(data["BwdBytes_BulkAvg"]))
        BwdPacket_BulkAvg = le.fit_transform(list(data["BwdPacket_BulkAvg"]))
        BwdBulkRateAvg = le.fit_transform(list(data["BwdBulkRateAvg"]))
        SubflowFwdPackets = le.fit_transform(list(data["SubflowFwdPackets"]))
        SubflowFwdBytes = le.fit_transform(list(data["SubflowFwdBytes"]))
        SubflowBwdPackets = le.fit_transform(list(data["SubflowBwdPackets"]))
        SubflowBwdBytes = le.fit_transform(list(data["SubflowBwdBytes"]))
        FWDInitWinBytes = le.fit_transform(list(data["FWDInitWinBytes"]))
        BwdInitWinBytes = le.fit_transform(list(data["BwdInitWinBytes"]))
        FwdActDataPkts = le.fit_transform(list(data["FwdActDataPkts"]))
        FwdSegSizeMin = le.fit_transform(list(data["FwdSegSizeMin"]))
        ActiveMean = le.fit_transform(list(data["ActiveMean"]))
        ActiveStd = le.fit_transform(list(data["ActiveStd"]))
        ActiveMax = le.fit_transform(list(data["ActiveMax"]))
        ActiveMin = le.fit_transform(list(data["ActiveMin"]))
        IdleMean = le.fit_transform(list(data["IdleMean"]))
        IdleStd = le.fit_transform(list(data["IdleStd"]))
        IdleMax = le.fit_transform(list(data["IdleMax"]))
        IdleMin = le.fit_transform(list(data["IdleMin"]))
        Label = le.fit_transform(list(data["Label"]))
        predict = "Label"  # optional
        X = list(zip(FlowDuration,
                     TotalFwdPacket,
                     TotalBwdpackets,
                     TotalLengthofFwdPacket,
                     TotalLengthofBwdPacket,
                     FwdPacketLengthMax,
                     FwdPacketLengthMin,
                     FwdPacketLengthMean,
                     FwdPacketLengthStd,
                     BwdPacketLengthMax,
                     BwdPacketLengthMin,
                     BwdPacketLengthMean,
                     BwdPacketLengthStd,
                     FlowBytes_s,
                     FlowPackets_s,
                     FlowIATMean,
                     FlowIATStd,
                     FlowIATMax,
                     FlowIATMin,
                     FwdIATTotal,
                     FwdIATMean,
                     FwdIATStd,
                     FwdIATMax,
                     FwdIATMin,
                     BwdIATTotal,
                     BwdIATMean,
                     BwdIATStd,
                     BwdIATMax,
                     BwdIATMin,
                     FwdPSHFlags,
                     BwdPSHFlags,
                     FwdURGFlags,
                     BwdURGFlags,
                     FwdHeaderLength,
                     BwdHeaderLength,
                     FwdPackets_s,
                     BwdPackets_s,
                     PacketLengthMin,
                     PacketLengthMax,
                     PacketLengthMean,
                     PacketLengthStd,
                     PacketLengthVariance,
                     FINFlagCount,
                     SYNFlagCount,
                     RSTFlagCount,
                     PSHFlagCount,
                     ACKFlagCount,
                     URGFlagCount,
                     CWRFlagCount,
                     ECEFlagCount,
                     Down_UpRatio,
                     AveragePacketSize,
                     FwdSegmentSizeAvg,
                     BwdSegmentSizeAvg,
                     FwdBytes_BulkAvg,
                     FwdPacket_BulkAvg,
                     FwdBulkRateAvg,
                     BwdBytes_BulkAvg,
                     BwdPacket_BulkAvg,
                     BwdBulkRateAvg,
                     SubflowFwdPackets,
                     SubflowFwdBytes,
                     SubflowBwdPackets,
                     SubflowBwdBytes,
                     FWDInitWinBytes,
                     BwdInitWinBytes,
                     FwdActDataPkts,
                     FwdSegSizeMin,
                     ActiveMean,
                     ActiveStd,
                     ActiveMax,
                     ActiveMin,
                     IdleMean,
                     IdleStd,
                     IdleMax,
                     IdleMin))
        y = list(Label)
        x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)
        model = KNeighborsClassifier(n_neighbors=5)
        model.fit(x_train, y_train)
        return model

    @staticmethod
    def predict(listFeatures):
        model = KNN.KNNModel()
        names = ["non-vpn", "vpn"]
        predicted = model.predict(listFeatures)
        return names[predicted[0]]