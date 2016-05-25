import json

class Decoder:
    """
    Extracts data from nodewatcher JSON dumps
    """
    def __init__(self, filename):
        self.file = open(filename,'r')
        self.json = json.load(self.file)

    def getNodeModel(self):
        return self.json["core.general"]["hardware"]["model"]

    def getNodeChannel(self, interface="wlan0"):
        return self.json["core.wireless"]["interfaces"][interface]["channel"]

    def getNodeSNR(self, interface="wlan0"):
        return self.json["core.wireless"]["interfaces"][interface]["signal"]-self.json["core.wireless"]["interfaces"][interface]["noise"]

    def getNodeBSSID(self, interface="wlan0"):
        return self.json["core.wireless"]["interfaces"][interface][bssid]

    def getNodeNeighbors(self, radio="phy1"):
        """
        returns a dictionary of all access points in the vicinity along with the signal strength of each access point.
        :param: radio used to survey surroundings
        :return: a dictionary of neighbors
        """
        return self.json["core.wireless"]["radios"][radio]["survey"]