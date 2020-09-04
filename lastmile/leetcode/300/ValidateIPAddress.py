import re


class ValidateIPAddress:
    def validIPAddress(self, IP: str) -> str:
        IPv4Pattern = re.compile("((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[0-9]?[0-9])(\.)){3}((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])($))")
        IPv6Pattern = re.compile("(([0-9a-fA-F]{1,4}(:)){1,7}([0-9a-fA-F]{1,4}($)))")

        if IPv4Pattern.match(IP):
            return "IPv4"
        elif IPv6Pattern.match(IP):
            return "IPv6"
        else:
            return "Neither"


if __name__ == '__main__':
    init = ValidateIPAddress()
    print(init.validIPAddress("172.16.254.1"))
    print(init.validIPAddress("1.1.1.1."))
    print(init.validIPAddress("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))

# patternIPv4 = re.compile("((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)(\.|$)){4}")
# patternIPv6 = re.compile("((([0-9a-fA-F]{1,4})(\:|$)){1,7}([0-9a-fA-F]){1,4})$")
# if patternIPv4.match(IP):
#     return "IPv4"
# elif patternIPv6.match(IP):
#     return "IPv6"
# else:
#     return "Neither"