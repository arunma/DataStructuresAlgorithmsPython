class ValidateIPAddress:

    def validIPAddress(self, ip):
        if ip.count(".") == 3:
            return self.isValidIpv4(ip)
        elif ip.count(":") == 7:
            return self.isValidIpv6(ip)
        else:
            return "Neither"

    def isValidIpv4(self, ip):
        splits=ip.split(".")
        for split in splits:
            if len(split)==0 or len(split)>3:
                return "Neither"
            if (split[0]=='0' and len(split)!=1) or not split.isdigit() or int(split)>255:
                return "Neither"
        return True

    def isValidIpv6(self, ip):
        splits=ip.split(":")
        alphas="1234567890ABCDEFabcdef"
        for split in splits:
            if len(split)==0 or len(split)>4:
                return "Neither"
            if not all(c in alphas for c in split):
                return "Neither"
        return True



if __name__ == '__main__':
    init = ValidateIPAddress()
    print(init.validIPAddress("172.16.254.1"))
    print(init.validIPAddress("1.1.1.1."))
    print(init.validIPAddress("1.1.1.1"))
    print(init.validIPAddress("01.1.1.1"))
    print(init.validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))
