import platform
import socket
import subprocess
import psutil
import time


# ============================================================
# Utility Functions
# ============================================================

def run_command(command):
    """Run a Linux command safely and return its output."""
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True
        )

        return result.stdout.strip()

    except FileNotFoundError:
        return f"Command not found: {command[0]}"

    except subprocess.CalledProcessError as error:
        return f"Command failed: {error}"

    except Exception as error:
        return f"Unexpected error: {error}"


def print_header(title):
    """Print a formatted section header."""
    print(f"\n{title}")
    print("-" * 40)


# ============================================================
# System Information
# ============================================================

def get_system_info():
    """Display basic system information."""

    hostname = socket.gethostname()
    os_name = platform.system()
    os_version = platform.release()
    architecture = platform.machine()

    print_header("SYSTEM INFORMATION")

    print(f"Hostname        : {hostname}")
    print(f"Operating System: {os_name}")
    print(f"OS Version      : {os_version}")
    print(f"Architecture    : {architecture}")


# ============================================================
# Network Information
# ============================================================

def get_ip_address():
    """Display the primary non-loopback IPv4 address."""

    output = run_command(
        ["ip", "-4", "-o", "addr", "show", "scope", "global"]
    )

    for line in output.splitlines():

        if line.startswith("Command ") or line.startswith("Unexpected"):
            break

        parts = line.split()

        if len(parts) >= 4:
            interface = parts[1]
            ip_address = parts[3].split("/")[0]

            print(f"Primary IP      : {ip_address}")
            print(f"Interface       : {interface}")
            return

    print("Primary IP      : Unable to determine")


def get_network_interfaces():
    """Display all network interfaces."""

    print_header("NETWORK INTERFACES")

    output = run_command(
        ["ip", "-br", "addr"]
    )

    print(output)


def get_default_gateway():
    """Display the default network gateway."""

    print_header("DEFAULT GATEWAY")

    output = run_command(
        ["ip", "route", "show", "default"]
    )

    if output:
        print(output)
    else:
        print("Default gateway: Unable to determine")


def get_routing_table():
    """Display the Linux routing table."""

    print_header("ROUTING TABLE")

    output = run_command(
        ["ip", "route"]
    )

    print(output)


# ============================================================
# DNS
# ============================================================

def test_dns():
    """Test DNS resolution."""

    print_header("DNS RESOLUTION TEST")

    domain = "google.com"

    try:
        ip_address = socket.gethostbyname(domain)

        print(f"Domain          : {domain}")
        print(f"Resolved IP     : {ip_address}")
        print("DNS Status      : Working")

    except socket.gaierror:
        print(f"Domain          : {domain}")
        print("DNS Status      : Failed")


# ============================================================
# Ports & Connections
# ============================================================

def get_listening_ports():
    """Display listening TCP and UDP ports."""

    print_header("LISTENING PORTS")

    output = run_command(
        ["ss", "-tuln"]
    )

    print(output)


def get_active_connections():
    """Display active TCP and UDP connections."""

    print_header("ACTIVE NETWORK CONNECTIONS")

    output = run_command(
        ["ss", "-tun"]
    )

    print(output)


# ============================================================
# System Health
# ============================================================

def get_system_health():
    """Display CPU, memory, disk and uptime information."""

    print_header("SYSTEM HEALTH")

    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    uptime_seconds = int(
        time.time() - psutil.boot_time()
    )

    days = uptime_seconds // 86400
    hours = (uptime_seconds % 86400) // 3600
    minutes = (uptime_seconds % 3600) // 60

    print(f"CPU Usage       : {cpu_usage}%")
    print(f"Memory Usage    : {memory.percent}%")
    print(f"Disk Usage      : {disk.percent}%")
    print(f"Uptime          : {days} days, {hours} hours, {minutes} minutes")


# ============================================================
# Full Report
# ============================================================

def full_report():
    """Display the complete system and network report."""

    print("\n" + "=" * 40)
    print("       FULL SYSTEM NETWORK REPORT")
    print("=" * 40)

    get_system_info()
    get_ip_address()
    get_network_interfaces()
    get_default_gateway()
    get_routing_table()
    test_dns()
    get_listening_ports()
    get_active_connections()
    get_system_health()

    print("\n" + "=" * 40)
    print("             REPORT COMPLETE")
    print("=" * 40)


# ============================================================
# Menu
# ============================================================

def show_menu():
    """Display the main application menu."""

    print("\n" + "=" * 40)
    print("       SYSTEM NETWORK INFO")
    print("=" * 40)

    print("1. System Information")
    print("2. Network Information")
    print("3. Default Gateway")
    print("4. Routing Table")
    print("5. DNS Test")
    print("6. Listening Ports")
    print("7. Active Connections")
    print("8. System Health")
    print("9. Full Report")
    print("0. Exit")

    print("=" * 40)


def main():
    """Run the interactive CLI application."""

    while True:

        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            get_system_info()

        elif choice == "2":
            get_ip_address()
            get_network_interfaces()

        elif choice == "3":
            get_default_gateway()

        elif choice == "4":
            get_routing_table()

        elif choice == "5":
            test_dns()

        elif choice == "6":
            get_listening_ports()

        elif choice == "7":
            get_active_connections()

        elif choice == "8":
            get_system_health()

        elif choice == "9":
            full_report()

        elif choice == "0":
            print("\nExiting System Network Info. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select a valid option.")


# ============================================================
# Program Entry Point
# ============================================================

if __name__ == "__main__":
    main()
