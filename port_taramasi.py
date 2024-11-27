import nmap
#nm=nmap.PortScanner()
#print("Nmap çalışır")

def port_taramasi(target_ip):
    scanner = nmap.PortScanner()
    scan_result = scanner.scan(hosts=target_ip,arguments='-p 1-1024')
    return scan_result['scan']