import psutil
import socket
import time
from datetime import datetime
import os

LOG_DIR = "net_logs"
os.makedirs(LOG_DIR, exist_ok=True)

def get_log_path():
    now = datetime.now()
    return os.path.join(LOG_DIR, now.strftime("conn_log_%Y-%m-%d.txt"))

def resolve_ip(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Unknown"

def log_connections():
    seen = set()

    while True:
        connections = psutil.net_connections(kind='inet')
        for conn in connections:
            if not conn.raddr:
                continue

            laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "N/A"
            raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "N/A"
            rhost = resolve_ip(conn.raddr.ip)
            pid = conn.pid or "N/A"
            status = conn.status

            conn_id = (laddr, raddr, pid, status)

            if conn_id in seen:
                continue
            seen.add(conn_id)

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            log_entry = (
                f"{'='*60}\n"
                f"🕒 Timestamp        : {timestamp}\n"
                f"📍 Local Address    : {laddr}\n"
                f"🌐 Remote Address   : {raddr}\n"
                f"🔍 Remote Hostname  : {rhost}\n"
                f"⚙️  Process PID      : {pid}\n"
                f"🔁 Connection Status: {status}\n"
            )

            print(log_entry)
            with open(get_log_path(), "a", encoding="utf-8") as f:
                f.write(log_entry)

        time.sleep(2)

if __name__ == "__main__":
    print("🔎 Windows Network Monitor (No Npcap Required)")
    print("Press Ctrl+C to stop.\n")
    try:
        log_connections()
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user. Goodbye!")
