import re

log_pattern = re.compile(r'(?P<ip>\S+) \S+ \S+ \[.*?\] "(GET|POST) (?P<endpoint>\S+) HTTP/1.1" (?P<status>\d{3}) \d+ "(.*?)" "(?P<agent>.*?)"')

def parse_log_line(line):
    match = log_pattern.match(line)
    if match:
        ip = match.group("ip")
        endpoint = match.group("endpoint")
        status = int(match.group("status"))
        agent = match.group("agent")
        return ip, endpoint, status, agent
    return None
