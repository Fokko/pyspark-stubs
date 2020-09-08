#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from typing import Any, Tuple, List
from pyspark._typing import F

import threading

__all__: List[str]

def print_exec(stream: Any) -> None: ...

class VersionUtils:
    @staticmethod
    def majorMinorVersion(sparkVersion: str) -> Tuple[int, int]: ...

def fail_on_stopiteration(f: F) -> F: ...
def _parse_memory(s: str) -> int: ...
def _print_missing_jar(
    lib_name: str, pkg_name: str, jar_name: str, spark_version: str
) -> None: ...

class InheritableThread(threading.Thread):
    def __init__(self, target: Any, *args: Any, **kwargs: Any): ...
    def __del__(self) -> None: ...
