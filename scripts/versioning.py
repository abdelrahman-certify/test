import argparse
import re
import sys
# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-v", "--version", required=True,
   help="version")

ap.add_argument("-p", "--prefix", required=True,
   help="version")

args = vars(ap.parse_args())

version = args['version']
prefix = args['prefix']

if prefix in version:
    last_version = re.search(r'-([0-9]{1,2})$', args['version'])
    if last_version:
        new_version = f"{prefix}-{int(last_version.group(1)) + 1}"
    else:
        new_version = f"{prefix}-1"
    print(new_version)
    sys.exit
else:
    version = prefix
    print(version)
