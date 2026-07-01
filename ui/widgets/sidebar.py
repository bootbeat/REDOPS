self.buttons = {}

pages = [
    "Dashboard",
    "Recon",
    "Threat Intel",
    "Log Analysis",
    "PCAP",
    "Malware",
    "Reports",
    "Settings"
]

for page in pages:
    button = QPushButton(page)
    layout.addWidget(button)
    self.buttons[page] = button

layout.addStretch()