import ipaddress

def verificar_ip_no_prefixo(ip, prefixo):
    endereco_ip = ipaddress.ip_address(ip)
    rede = ipaddress.ip_network(prefixo, strict=False)
    return endereco_ip in rede

ip = "192.168.1.5"
prefixo = "192.168.1.0/24"
resultado = verificar_ip_no_prefixo(ip, prefixo)
print(f"O IP {ip} está contido no prefixo {prefixo}? {resultado}")