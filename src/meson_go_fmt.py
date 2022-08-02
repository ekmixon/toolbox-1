#!/usr/bin/env python3
#
# Copyright © 2022 Red Hat Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import subprocess
import sys

if len(sys.argv) != 2:
    print(f'{sys.argv[0]}: wrong arguments', file=sys.stderr)
    print(f'Usage: {sys.argv[0]} [SOURCE DIR]', file=sys.stderr)
    sys.exit(1)

source_dir = sys.argv[1]

try:
    gofmt = subprocess.run(['gofmt', '-d', source_dir], capture_output=True, check=True)
except subprocess.CalledProcessError as e:
    print(
        f'{sys.argv[0]}: gofmt returned non-zero exit status {e.returncode}',
        file=sys.stderr,
    )

    sys.exit(e.returncode)

if gofmt.stdout:
   diff = gofmt.stdout.decode()
   print(diff)
   sys.exit(1)

sys.exit(0)
