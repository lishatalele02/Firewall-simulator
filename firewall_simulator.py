import tkinter as tk
from tkinter import messagebox
import socket

firewall_rules = {
    "allow": [("192.168.1.1", 80), ("192.168.1.2", 22), ("example.com", 80)],
    "block": [("192.168.1.100", 443), ("blockedsite.com", 443)]
}

def check_traffic(ip_or_domain, port):
    try:
        # Only resolve if it's a domain, not an IP address
        ip = socket.gethostbyname(ip_or_domain) if not ip_or_domain.replace('.', '').isdigit() else ip_or_domain
    except socket.error:
        return f"Invalid IP/Domain: {ip_or_domain}"

    # Check in the firewall rules
    if (ip, port) in firewall_rules["allow"]:
        return f"Traffic from {ip_or_domain}:{port} is ALLOWED."
    elif (ip, port) in firewall_rules["block"]:
        return f"Traffic from {ip_or_domain}:{port} is BLOCKED."
    else:
        return f"Traffic from {ip_or_domain}:{port} is UNDEFINED."

import os

def log_traffic(ip_or_domain, port, status):
    file_path = os.path.abspath("firewall_log.txt")
    print("Log file location:", file_path)
    with open(file_path, "a") as log_file:
        log_file.write(ip_or_domain + ":" + str(port) + " - " + status + "\n")

def add_rule():
    ip_or_domain = ip_entry.get()
    port = int(port_entry.get())
    action = action_var.get()
    
    # Check if the rule already exists in the opposite list
    opposite_action = "allow" if action == "block" else "block"
    if (ip_or_domain, port) in firewall_rules[action]:
        messagebox.showerror("Firewall", f"Rule already exists in {action} list.")
        return
    if (ip_or_domain, port) in firewall_rules[opposite_action]:
        messagebox.showerror("Firewall", f"Cannot add rule. {ip_or_domain}:{port} is already in the {opposite_action} list.")
        return

    # Add the rule to the specified action list
    firewall_rules[action].append((ip_or_domain, port))
    messagebox.showinfo("Firewall", f"Rule added: {action} {ip_or_domain}:{port}")


def view_rules():
    rules = "\n".join([action + ": " + str(rule) for action, rules in firewall_rules.items() for rule in rules])
    messagebox.showinfo("Firewall Rules", rules)

def simulate_traffic():
    ip_or_domain = ip_entry.get()
    port = int(port_entry.get())
    status = check_traffic(ip_or_domain, port)
    log_traffic(ip_or_domain, port, status)
    messagebox.showinfo("Traffic Status", status)

root = tk.Tk()
root.title("Firewall Simulator")

tk.Label(root, text="IP/Domain:").grid(row=0, column=0)
ip_entry = tk.Entry(root)
ip_entry.grid(row=0, column=1)

tk.Label(root, text="Port:").grid(row=1, column=0)
port_entry = tk.Entry(root)
port_entry.grid(row=1, column=1)

tk.Label(root, text="Action:").grid(row=2, column=0)
action_var = tk.StringVar(value="allow")
tk.OptionMenu(root, action_var, "allow", "block").grid(row=2, column=1)

tk.Button(root, text="Add Rule", command=add_rule).grid(row=3, column=0)
tk.Button(root, text="View Rules", command=view_rules).grid(row=3, column=1)
tk.Button(root, text="Check Traffic", command=simulate_traffic).grid(row=4, column=0, columnspan=2)

root.mainloop()
