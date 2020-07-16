class ValidateIPAddress:
    def validIPAddress(self, IP: str) -> str:
        if "." in IP and self.ipv4(IP):
            return "IPv4"
        elif ":" in IP and self.ipv6(IP):
            return "IPv6"
        else:
            return "Neither"

    def ipv4(self, IP):
        octets = IP.split(".")
        try:
            return len(octets) == 4 and all(res == str(int(res)) and int(res) <= 255 and res[0] != "-" for res in octets)
        except:
            return False

    def ipv6(self, IP):
        comps = IP.split(":")
        try:
            return len(comps) == 8 and all(int(res, 16) >= 0 and len(res) < 5 and res[0] != "-" for res in comps)
        except:
            return False


if __name__ == '__main__':
    init = ValidateIPAddress()
    print(init.validIPAddress("172.16.254.1"))
    print(init.validIPAddress("2001:0db8:85a3:0:0:8A2E:0370:7334"))
    print(init.validIPAddress("256.256.256.256"))
    print(init.validIPAddress("1e1.4.5.6"))
    print(init.validIPAddress("15.16.-255.1"))
    print(init.validIPAddress("2001:0db8:85a3:00000:0:8A2E:0370:7334"))
    print(init.validIPAddress("20EE:FGb8:85a3:0:0:8A2E:0370:7334"))
    print(init.validIPAddress("1081:db8:85a3:01:-0:8A2E:0370:7334"))
