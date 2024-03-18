## ASN to IP list
import requests
import json
import ipaddress

def convert_asn_to_ips(asn_list_file, output_file):
    # Read ASN list file
    with open(asn_list_file, 'r') as f:
        asn_list = f.readlines()

    # Remove comments and blank lines from files
    asn_list = [line.strip().split('//')[0].strip() for line in asn_list if line.strip() and not line.strip().startswith('//')]

    # Loop through ASN list and convert to IP list
    ip_list = []
    for asn_entry in asn_list:
        asn = asn_entry.split(',')[1].strip()
        # Construct the URL and download the IP list corresponding to the ASN
        url = f"https://raw.githubusercontent.com/ipverse/asn-ip/master/as/{asn}/aggregated.json"
        response = requests.get(url)
        if response.status_code == 200:
            data = json.loads(response.text)
            ipv4_subnets = data['subnets']['ipv4']
            ipv6_subnets = data['subnets']['ipv6']
            ip_list.extend(ipv4_subnets)
            ip_list.extend(ipv6_subnets)

    # Split IPv4, IPv6 addresses and sort
    ipv4_list = sorted([ip for ip in ip_list if ipaddress.ip_network(ip).version == 4], key=ipaddress.IPv4Network)
    ipv6_list = sorted([ip for ip in ip_list if ipaddress.ip_network(ip).version == 6], key=ipaddress.IPv6Network)
    sorted_ip_list = ipv4_list + ipv6_list

    with open(output_file, 'w') as file:
        for ip in sorted_ip_list:
            file.write(f"{ip}\n")
    with open(output_file_v4, 'w') as file:
        for ip in ipv4_list:
            file.write(f"{ip}\n")
    with open(output_file_v6, 'w') as file:
        for ip in ipv6_list:
            file.write(f"{ip}\n")
            
# Input ASN list file and output file name
asn_list_file = "ASN.China.list"
output_file = "IP.ASN.China.list"
output_file_v4  = "IPv4.ASN.China.list"
output_file_v6  = "IPv6.ASN.China.list"

# Call functions to convert and save
convert_asn_to_ips(asn_list_file, output_file)
