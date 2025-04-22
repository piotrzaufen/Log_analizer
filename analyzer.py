from parser import parse_log_line
from suspicious import is_suspicious
from collections import Counter
import sys

def analyze(file_path):
    ip_counter = Counter()
    endpoint_counter = Counter()
    suspicious_ips = set()

    with open(file_path, 'r') as f:
        for line in f:
            parsed = parse_log_line(line)
            if parsed:
                ip, endpoint, status, agent = parsed
                ip_counter[ip] += 1
                endpoint_counter[endpoint] += 1
                if is_suspicious(status, agent):
                    suspicious_ips.add(ip)

    print("Top 5 IPs:")
    for ip, count in ip_counter.most_common(5):
        print(f"  - {ip} ({count} requests)")

    print("Top 5 Endpoints:")
    for endpoint, count in endpoint_counter.most_common(5):
        print(f"  - {endpoint}")

    print("Suspicious Activity:")
    for ip in suspicious_ips:
        print(f"  - {ip}: flagged for review")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyzer.py <logfile>")
        sys.exit(1)
    analyze(sys.argv[1])
