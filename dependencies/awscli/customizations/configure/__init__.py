# Copyright 2016 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"). You
# may not use this file except in compliance with the License. A copy of
# the License is located at
#
#     http://aws.amazon.com/apache2.0/
#
# or in the "license" file accompanying this file. This file is
# distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF
# ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.
import string
from botocore.vendored.six.moves import shlex_quote

NOT_SET = '<not set>'
PREDEFINED_SECTION_NAMES = ('preview', 'plugins')
_WHITESPACE = ' \t'


class ConfigValue(object):

    def __init__(self, value, config_type, config_variable):
        self.value = value
        self.config_type = config_type
        self.config_variable = config_variable

    def mask_value(self):
        if self.value is NOT_SET:
            return
        self.value = mask_value(self.value)


class SectionNotFoundError(Exception):
    pass


def mask_value(current_value):
    if current_value is None:
        return 'None'
    else:
        return ('*' * 16) + current_value[-4:]


def profile_to_section(profile_name):
    """Converts a profile name to a section header to be used in the config."""
    if any(c in _WHITESPACE for c in profile_name):
        profile_name = shlex_quote(profile_name)
    return 'profile %s' % profile_name
