#!/usr/bin/env python
#
import shlex
from glob import glob
#

cmd = 'herp derp "fuzzy bear" "wanga tanga" pop'  # <1>

print(cmd.split())  # <2>
print()

print(shlex.split(cmd))  # <3>


cmd = 'some_program -v Italy France "Burkina Faso"'
params = "../DATA/presidents.*"

cmd_to_run = shlex.split(cmd) + glob(params)

print(f"cmd_to_run: {cmd_to_run}")
