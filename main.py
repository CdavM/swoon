import decoder
import numpy

def getSocialSNR(IP_array):
    """
    Returns an average SNR of all the nodes in node_list
    :param node_array: array of IPs of nodes in the network
    :return: SocialSNR, a number representing the average SNR of the network
    """
    node_list = {}
    for IP in IP_array:
        node_list[IP] = decoder.Decoder("test_data/" + IP + ".feed")
    SNR_list = {}
    for node in node_list.values():
        SNR_list[node.getNodeIP()] = node.getNodeSNR()
    return numpy.mean([SNR_list[key] for key in SNR_list])

ip_list = []
for i in range(40,54):
    ip_list.append('10.20.32.'+str(i))

print(getSocialSNR(ip_list))
