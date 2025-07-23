
🔥 Firewall Simulator using Python & Tkinter

This project is a simple GUI-based Firewall Simulator built using Python and Tkinter. It allows users to add custom firewall rules (allow/block specific IPs/domains and ports), simulate network traffic, and check whether it's allowed, blocked, or undefined. It also logs the results in a local log file.

🛠️ Features
- ✅ Add custom rules (Allow or Block IP/Domain with Port)
- 🔍 Simulate and check traffic against firewall rules
- 📄 View all current firewall rules
- 🧾 Log all simulated traffic to a local file `firewall_log.txt`
- 🧠 Domain names are resolved to IPs automatically

🐍 Requirements
- Python 3.x
- Tkinter (comes pre-installed with Python)

🚀 Installation
1. Clone the repository:
   git clone https://github.com/yourusername/firewall-simulator.git
   cd firewall-simulator

2. Run the simulator:
   python firewall_simulator.py

🧪 Usage
1. Enter IP or Domain in the input field.
2. Enter Port Number.
3. Select Action (Allow or Block).
4. Click "Add Rule" to apply a rule.
5. Click "View Rules" to view existing firewall rules.
6. Click "Check Traffic" to simulate traffic and get the status.
7. All traffic simulation results are logged in `firewall_log.txt`.

📂 Log File
All simulated traffic checks are recorded in:
firewall_log.txt

Example log entry:
192.168.1.2:22 - Traffic from 192.168.1.2:22 is ALLOWED.

You can find this file in the same directory where the Python script is located.

🧠 How It Works
- User inputs an IP address or domain name and port number.
- The domain (if given) is resolved to an IP address.
- The app checks if the combination exists in the allow or block lists.
- The result (ALLOWED, BLOCKED, or UNDEFINED) is displayed and logged.

📌 To-Do / Future Improvements
- [ ] Add delete/edit rule functionality
- [ ] Export/import rules from/to JSON or CSV
- [ ] Real-time traffic monitoring (advanced feature)
- [ ] Better UI layout and dark mode support

👨‍💻 Author
Lisha Talele
GitHub: @lishatalele02

📃 License
This project is open source and available under the MIT License.
Feel free to use and modify it for your learning and development needs!
