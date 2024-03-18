# Export IP.ASN.China.list to a Clash-compatible yaml file
with open("IP.ASN.China.list", 'r') as f:
    iplist = f.readlines()
with open("IPv4.ASN.China.list", 'r') as f:
    iplistv4 = f.readlines()
with open("IPv6.ASN.China.list", 'r') as f:
    iplistv6 = f.readlines()

output = 'payload:\n'
for line in iplist:
    output += "  - '" + line.strip() + "'\n"
with open('IP.ASN.China.yaml', 'w') as f:
    f.write(output)

for line in iplistv4:
    output += "  - '" + line.strip() + "'\n"
with open('IPv4.ASN.China.yaml', 'w') as f:
    f.write(output)

for line in iplistv6:
    output += "  - '" + line.strip() + "'\n"
with open('IPv6.ASN.China.yaml', 'w') as f:
    f.write(output)
