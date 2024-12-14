import argparse
import re
import sys
# Construct the argument parser
ap = argparse.ArgumentParser()

# Add the arguments to the parser
ap.add_argument("-v", "--version", required=True,
   help="version")

ap.add_argument("-d", "--date", required=True,
   help="version")

args = vars(ap.parse_args())

version = args['version']
date = args['date']

if date in version:
    last_version = re.search(r'-([0-9]{1,2})$', args['version'])
    if last_version:
        new_version = f"{date}-{int(last_version.group(1)) + 1}"
    else:
        new_version = f"{date}-1"
    print(new_version)
    sys.exit
else:
    version = date
    print(version)
