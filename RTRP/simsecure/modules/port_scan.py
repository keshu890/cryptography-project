"""
Port Scanner Module - Performs basic TCP port scanning
"""

import socket
import threading
from colorama import Fore, Style


# Common ports and their services
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    5432: "PostgreSQL",
    5984: "CouchDB",
    6379: "Redis",
    8080: "HTTP Proxy",
    27017: "MongoDB",
    8443: "HTTPS Alt"
}

# Thread-safe list to store open ports
open_ports = []
lock = threading.Lock()


def check_port(host, port):
    """
    Check if a single port is open on the target host.
    
    Args:
        host (str): Target hostname or IP address
        port (int): Port number to check
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((host, port))
        
        if result == 0:
            with lock:
                open_ports.append(port)
                service = COMMON_PORTS.get(port, "Unknown Service")
                print(f"{Fore.RED}[+] Port {port} is OPEN ({service}){Style.RESET_ALL}")
        
        sock.close()
    
    except socket.gaierror:
        # Host resolution error - will be caught in main function
        pass
    except socket.error:
        # Socket error
        pass
    except Exception:
        pass


def scan_ports(host):
    """
    Perform port scanning on common ports.
    
    Args:
        host (str): Target hostname or IP address
    
    Returns:
        tuple: (security_score, findings_list)
    """
    findings = []
    score = 0
    
    # Reset global open_ports list
    global open_ports
    open_ports = []
    
    try:
        print(f"\n{Fore.CYAN}[*] Scanning Ports on: {host}{Style.RESET_ALL}")
        
        # Resolve hostname
        try:
            ip_address = socket.gethostbyname(host)
            print(f"{Fore.CYAN}[*] Resolved IP: {ip_address}{Style.RESET_ALL}")
        except socket.gaierror:
            print(f"{Fore.RED}[!] Invalid hostname or domain: {host}{Style.RESET_ALL}")
            findings.append(f"ERROR: Could not resolve hostname: {host}")
            return 0, findings
        
        print("-" * 70)
        
        # Create threads for concurrent port scanning
        threads = []
        for port in COMMON_PORTS.keys():
            thread = threading.Thread(target=check_port, args=(host, port))
            thread.daemon = True
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join(timeout=5)
        
        print("-" * 70)
        
        # Generate findings and score
        if not open_ports:
            print(f"{Fore.GREEN}[+] No open ports detected{Style.RESET_ALL}")
            findings.append("All scanned ports are closed or filtered")
            score = 10
        else:
            num_open = len(open_ports)
            print(f"\n{Fore.YELLOW}[!] Open Ports Found: {num_open}{Style.RESET_ALL}")
            print(f"{Fore.CYAN}Open ports: {', '.join(map(str, sorted(open_ports)))}{Style.RESET_ALL}")
            
            findings.append(f"Detected {num_open} open port(s): {', '.join(map(str, sorted(open_ports)))}")
            
            # Calculate security score based on number of open ports
            if num_open == 0:
                score = 10
            elif num_open == 1:
                score = 9
                findings.append("Single open port detected - verify if necessary")
            elif num_open == 2:
                score = 8
                findings.append("Two open ports detected - may indicate required services")
            elif num_open <= 4:
                score = 6
                findings.append("Multiple open ports - recommended to verify necessity")
            else:
                score = 4
                findings.append("Many open ports detected - significant security exposure")
                findings.append("Recommendation: Close unnecessary ports and apply firewall rules")
        
        print(f"\n{Fore.CYAN}Security Score: {Fore.YELLOW}{score}/10{Style.RESET_ALL}")
        
        return score, findings
    
    except Exception as e:
        print(f"{Fore.RED}[!] Error during port scan: {str(e)}{Style.RESET_ALL}")
        findings.append(f"ERROR: {str(e)}")
        return 0, findings
