# 📊 Log Analyzer – Advanced Log File Parser in Python

A modular tool written in Python for analyzing and extracting insights from web server access logs (Apache/Nginx style). It provides request statistics, IP hit counts, suspicious activity detection, and more.

## 🔍 Features

- Modular parsing and analysis of server logs
- Built-in suspicious behavior detection (e.g. scan patterns, bots)
- Top IPs, endpoints, user-agents
- Easily extensible (plugin-ready)

## 🧰 Requirements

- Python 3.7+
- Standard library only (no external dependencies)

## 📦 Structure

- `analyzer.py`: Main script – runs analysis and prints results
- `parser.py`: Log line parser based on Apache/Nginx format
- `suspicious.py`: Heuristics to detect suspicious requests
- `utils.py`: Helper functions
- `logs/access.log`: Sample log file (can be replaced)

## 🚀 Usage

```bash
python analyzer.py logs/access.log
```

## 📈 Sample Output

```
Top 5 IPs:
  - 192.168.1.10 (124 requests)
  - 10.0.0.5 (87 requests)
Top 5 Endpoints:
  - /login
  - /index.html
Suspicious Activity:
  - 192.168.1.10: Scanning attempt (many 404s)
  - 10.0.0.5: Unusual User-Agent detected
```

## 📄 License

MIT License. Contributions welcome!
