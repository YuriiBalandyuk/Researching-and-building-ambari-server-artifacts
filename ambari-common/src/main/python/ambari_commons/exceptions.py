#!/usr/bin/python2

"""
Licensed to the Apache Software Foundation (ASF) under one
or more contributor license agreements.  See the NOTICE file
distributed with this work for additional information
regarding copyright ownership.  The ASF licenses this file
to you under the Apache License, Version 2.0 (the
"License"); you may not use this file except in compliance
with the License.  You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


class FatalException(Exception):
    def __init__(self, code, reason):
      self.code = code
      self.reason = reason

    def __str__(self):
        return repr("Fatal exception: %s, exit code %s" % (self.reason, self.code))


class NonFatalException(Exception):
  def __init__(self, reason):
    self.reason = reason

  def __str__(self):
    return repr("NonFatal exception: %s" % self.reason)


class TimeoutError(Exception):
  def __str__(self):
    return repr("Timeout error: %s" % self.message)
