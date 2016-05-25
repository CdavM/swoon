import json

class Decoder:
    """
    Extracts data from nodewatcher JSON dumps
    """
    def __init__(self, filename):
        self.filename = filename
        self.file = open(filename,'r')
        self.json = json.load(self.file)

    def getNodeModel(self):
        try:
            return self.json["core.general"]["hardware"]["model"]
        except NameError:
            return "Model not found on this device."

    def getNodeChannel(self, frequency_band="2"):
        """

        :param frequency_band: either "2" or "5", corresponding to 2.4GHz and 5GHz.
        :return: channel currently assigned to the node at the specified frequency band.
        """
        try:
            for interface in self.json["core.wireless"]["interfaces"]:
                if str(self.json["core.wireless"]["interfaces"][interface]["frequency"])[:1] == frequency_band:
                    return self.json["core.wireless"]["interfaces"][interface]["channel"]
        except NameError:
            print("Error parsing JSON file for " + str(self.filename))

    def getNodeSNR(self, frequency_band="2"):
        """
        Returns the SNR for this node (difference between signal and noise in dB).
        :param frequency_band: either "2" or "5", corresponding to 2.4GHz and 5GHz.
        :return: SNR for this node at the specified frequency band
        """
        try:
            for interface in self.json["core.wireless"]["interfaces"]:
                if str(self.json["core.wireless"]["interfaces"][interface]["frequency"])[:1] == frequency_band:
                    return self.json["core.wireless"]["interfaces"][interface]["signal"]-self.json["core.wireless"]["interfaces"][interface]["noise"]
        except NameError:
            print("Error parsing JSON file for " + str(self.filename))

    def getNodeBSSID(self, frequency_band="2"):
        """

        :param frequency_band: either "2" or "5", corresponding to 2.4GHz and 5GHz.
        :return: BSSID for this node at the specified frequency band
        """
        try:
            for interface in self.json["core.wireless"]["interfaces"]:
                if str(self.json["core.wireless"]["interfaces"][interface]["frequency"])[:1] == frequency_band:
                    return self.json["core.wireless"]["interfaces"][interface]["bssid"]
        except NameError:
            print("Error parsing JSON file for " + str(self.filename))


    def getNodeNeighbors(self, frequency_band="2"):
        """
        returns a dictionary of all access points in the vicinity along with the signal strength of each access point.
        :param: frequency_band: either "2" or "5", corresponding to 2.4GHz and 5GHz.
        :return: a dictionary of neighbors at the specified frequency band
        """
        if frequency_band == "2":
            frequency_band_max_channel = 14
            frequency_band_min_channel = 1
        elif frequency_band == "5":
            frequency_band_max_channel = 165
            frequency_band_min_channel = 36
        else:
            print("frequency band not recognized")

        try:
            for radio in self.json["core.wireless"]["radios"]:
                for neighbor in self.json["core.wireless"]["radios"][str(radio)]["survey"]:
                    if neighbor["channel"] <= frequency_band_max_channel and neighbor["channel"] >= frequency_band_min_channel:
                        return self.json["core.wireless"]["radios"][radio]["survey"]
        except KeyError:
            pass
        except NameError:
            print("Error parsing JSON file for " + str(self.filename))