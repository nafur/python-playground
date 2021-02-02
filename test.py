#!/usr/bin/env python3

import resource

resource.setrlimit(resource.RLIMIT_CPU, (1.5, 1.5))
