import decoder
import numpy

class NodeSociety:
    def __init__(self, IP_array):
        self.IP_array = IP_array
        self.node_list = {}
        for IP in IP_array:
            self.node_list[IP] = decoder.Decoder("test_data/" + IP + ".feed")

    def getSocialSNR(self):
        """
        Returns an average SNR of all the nodes in node_list
        :param node_array: array of IPs of nodes in the network
        :return: SocialSNR, a number representing the average SNR of the network
        """
        SNR_list = {}
        for node in self.node_list.values():
            SNR_list[node.getNodeIP()] = node.getNodeSNR()
        return numpy.mean([SNR_list[key] for key in SNR_list])

    def optimizeSocialSNR(self, frequency_band="2"):
        """
        returns a list of nodes with optimal channels
        :param frequency_band: either "2" or "5", corresponding to 2.4GHz and 5GHz.
        :return: a dictionary of nodes with an associated channel that optimizes Social SNR
        """
        #TODO: implement
        return self.node_list


ip_list = []
for i in range(40,54):
    ip_list.append('10.20.32.'+str(i))

society = NodeSociety(ip_list)

print(society.getSocialSNR())
