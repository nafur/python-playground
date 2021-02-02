#!/usr/bin/env python3

import resource
import subprocess

def limit():
    resource.setrlimit(resource.RLIMIT_CPU, (1.5, 1.5))

subprocess.Popen(['ls'], preexec_fn=limit)

