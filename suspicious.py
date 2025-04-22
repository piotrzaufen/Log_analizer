def is_suspicious(status, agent):
    suspicious_agents = ["sqlmap", "nmap", "curl", "bot"]
    if status == 404:
        return True
    if any(bot in agent.lower() for bot in suspicious_agents):
        return True
    return False
