def verificar_status(pc):
    ip = pc.get("ip", "0.0.0.0")
    latencia = pc.get("latencia", 0)
    perda = pc.get("perda", 0)
    
    if perda > 80:
        return "Offline"
    
    if latencia > 100 or perda > 10:
        return "Instavel"
    
    return "Online"

def main():
    pcs = [
        {"ip": "192.168.1.10", "latencia": 20, "perda": 2},
        {"ip": "192.168.1.11", "latencia": 150, "perda": 5},
        {"ip": "192.168.1.12", "latencia": 30, "perda": 90}
    ]
    
    for pc in pcs:
        status = verificar_status(pc)
        print(f"IP: {pc['ip']} - Status: {status}")

main()