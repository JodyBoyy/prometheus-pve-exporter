"""
Proxmox VE exporter for the Prometheus monitoring system.
"""
import pve_exporter.proxy
import threading
from pve_exporter.cli import main

# main()
t1 = threading.Thread(main())
t2 = threading.Thread(pve_exporter.proxy.main())