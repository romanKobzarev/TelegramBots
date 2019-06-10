import random as r

ip = "192.68.1.1"
ip_list = ["192.168.1.1", "56.43.234.12", "13123.1231231.12135.687", "12312.657.567.865", "678678"]
index = r.randint(0, len(ip_list) - 1)
print(index)
print("""
    Такой IP {IP} не существует
    Попробуйте один из этих {OTHER_IP}  
    """.format(OTHER_IP=ip_list[index], IP=ip))
