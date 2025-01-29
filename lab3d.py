#!/usr/bin/env python3

# Author ID: seimina

import os
import subprocess

def free_space():
    # Launch the Linux command as a new process
    p = subprocess.Popen(
        "df -h | grep '/$' | awk '{print $4}'",
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        shell=True
    )

    # Capture the output
    output = p.communicate()

    # Convert stdout to a string and strip newline characters
    stdout = output[0].decode('utf-8').strip()
    return stdout

if __name__ == "__main__":
    print(free_space())
