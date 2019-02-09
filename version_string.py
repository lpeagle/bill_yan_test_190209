from enum import Enum
import re


class CompareResult(Enum):
    EQUAL = 0,
    GREATER = 1,
    LESS = 2


def compare_version(version_str1, version_str2):
    """
    Suppose version string is in the format of {major}.{minor}.{patch}
    major, minor are integers, while patch is letter a-z
    this function compares two version string
    :param version_str1: 1st version str
    :param version_str2: 2nd version str
    :return: CompareResult.GREATER, if version2 greater than version1, CompareResult.EQUAL they are equal,
    CompareResult.LESS version2 less than version1
    """
    compare_result = 0
    pattern = '([^\.]+)\.?([^\.]*)\.?([^\.]*)'
    match1 = re.match(pattern, version_str1.strip())
    match2 = re.match(pattern, version_str2.strip())
    major2 = match2.group(1)
    major1 = match1.group(1)
    minor2 = match2.group(2) if match2.group(2) else '0'
    minor1 = match1.group(2) if match1.group(2) else '0'
    patch2 = match2.group(3) if match2.group(3) else '0'
    patch1 = match1.group(3) if match1.group(3) else '0'

    if int(major2) > int(major1):
        return CompareResult.GREATER
    elif int(major2) < int(major1):
        return CompareResult.LESS
    else:  # same major version
        if int(minor2) > int(minor1):
            return CompareResult.GREATER
        elif int(minor2) < int(minor1):
            return CompareResult.LESS
        else:
            if patch2 > patch1:
                return CompareResult.GREATER
            elif patch2 < patch1:
                return CompareResult.LESS
            else:
                return CompareResult.EQUAL
