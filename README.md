# 🔍 Windows Network Monitor (No Npcap Required)

A lightweight Python network connection monitor that tracks active connections without requiring Npcap/WinPcap. Logs local/remote addresses, hostnames, process IDs, and connection status with timestamps.

## Features
- 🚫 **No Npcap Dependency** - Uses built-in system APIs via `psutil`
- 📝 **Automatic Daily Logging** - Creates dated log files in `net_logs/` directory
- 🔄 **New Connection Detection** - Only logs newly established connections
- 🌐 **Hostname Resolution** - Translates remote IP addresses to hostnames
- ⏱️ **Timestamped Records** - Includes exact date/time for each connection
- 📊 **Connection Details** - Logs local/remote addresses, ports, PID, and status
- 🛡️ **Automatic Directory Creation** - Handles log directory setup

## Requirements
- Python 3.6+
- `psutil` package (`pip install psutil`)

- View logs:

Check console output in real-time

Inspect historical logs in net_logs/ directory

Sample Output
text
============================================================
🕒 Timestamp        : 2023-08-15 14:30:45
📍 Local Address    : 192.168.1.10:49685
🌐 Remote Address   : 172.217.14.206:443
🔍 Remote Hostname  : fra16s48-in-f14.1e100.net
⚙️  Process PID      : 1234
🔁 Connection Status: ESTABLISHED
============================================================

Key Functions
get_log_path() - Generates daily log file paths

resolve_ip(ip) - Converts IP addresses to hostnames

log_connections() - Main monitoring loop (runs every 2 seconds)

Notes
Requires administrator privileges to access all process information

Only logs new connections (duplicates are filtered)

UDP connections show "N/A" for connection status

Press Ctrl+C to stop monitoring

Logs are appended to daily files in UTF-8 format

Limitations
Cannot capture packets (only active connections)

Limited process details for some system processes

Hostname resolution depends on DNS configuration
