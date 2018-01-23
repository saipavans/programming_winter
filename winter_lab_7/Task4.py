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

    def getAddress(self):
        return self.address_fields

    def getMask(self):
        mask_as_list = []
        octet_index, remaining_one_bits = divmod(self.mask, 8) ## ex, 26-> 3,2
        octet_mask = self.bits_to_decimal(remaining_one_bits)
        for i in range(4):
            if i < octet_index:
                mask_as_list.append(255)
            elif i == octet_index:
                mask_as_list.append(octet_mask)
            else:
                mask_as_list.append(0)
        return mask_as_list

    @staticmethod
    def bits_to_decimal(num):
        res = 0
        for i in range(num):
            res += ((2) ** (7 - i))
        return res


def main():
    ip = IPv4([10, 0, 1, 255], 30)
    print (ip.getAddress())
    print (ip.getNetwork())
    print (ip.getMask())


if __name__ == '__main__':
    main()