#!/usr/bin/env python3

import sys
import libvirt

URI = 'qemu:///session'

conn = libvirt.open(URI)

if conn == None:
    print("Failed to open connection to %s" % URI, file=sys.stderr)
    exit(1)
else:
    print("Successfully opened connection to %s" % URI)
    conn.close()
    exit(0)
