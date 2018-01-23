class SubnetDetails():
    network_address = [0, 0, 0, 0]
    broatcast_address = [0, 0, 0, 0]
    first_host = [0, 0, 0, 0]
    last_host = [0, 0, 0, 0]
    number_of_hosts = 0

    def __str__(self):
        return s


class IPv4:
    address_fields = [0, 0, 0, 0]
    mask = 0

    def __init__(self, address, mask):
        self.address_fields = address
        self.mask = mask

    def getNetwork(self):
        network = []
        octet_index, octet_mask = divmod(self.mask, 8)
        octet_mask = self.convert_to_binary(octet_mask)
        for index in range(len(self.address_fields)):
            if index < octet_index:
                network.append(self.address_fields[index])
            elif index == octet_index:
                masked_value = self.address_fields[index] & octet_mask
                network.append(masked_value)
            else:
                network.append(0)
        return network

    def getBroadcast(self):
        network = []
        octet_index, octet_mask = divmod(self.mask, 8)
        for index in range(len(self.address_fields)):
            if index < octet_index:
                network.append(self.address_fields[index])
            elif index == octet_index:
                masked_value = self.address_fields[index] | self.getWildCard()
                network.append(masked_value)
            else:
                network.append(255)
        return network

    def getAddress(self):
        return self.address_fields

    def getMask(self):
        mask_as_list = []
        octet_index, octet_mask = divmod(self.mask, 8)
        octet_mask = self.convert_to_binary(octet_mask)
        for i in range(4):
            if i < octet_index:
                mask_as_list.append(255)
            elif i == octet_index:
                mask_as_list.append(octet_mask)
            else:
                mask_as_list.append(0)
        return mask_as_list

    def getWildCard(self):
        mask_as_list = []
        octet_index, octet_mask = divmod(self.mask, 8)
        octet_mask = self.convert_to_binary(octet_mask)
        for i in range(4):
            if i < octet_index:
                mask_as_list.append(0)
            elif i == octet_index:
                mask_as_list.append(255-octet_mask)
            else:
                mask_as_list.append(255)
        return mask_as_list

    @staticmethod
    def convert_to_binary(num):
        res = 0
        for i in range(num):
            res += ((2) ** (7 - i))
        return res

    def subnet_calculator(self):
        subnet = SubnetDetails()
        subnet.network_address = self.getNetwork()
        subnet.broatcast_address = self.getBroadcast()
        return subnet


def main():
    ip = IPv4([192, 168, 255, 22], 31)
    print (ip.getNetwork())
    print (ip.getBroadcast())


if __name__ == '__main__':
    main()