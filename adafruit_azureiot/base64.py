# The MIT License (MIT)
#
# Copyright (c) 2020 Jim Bennett
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""
`base64`
================================================================================

RFC 3548: Base64 Data Encodings


* Author(s): Jim Bennett

Implementation Notes
--------------------

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

"""

import adafruit_binascii as binascii

__all__ = ["b64encode", "b64decode"]


def _bytes_from_decode_data(data: str):
    try:
        return data.encode("ascii")
    except Exception as e:
        raise ValueError("string argument should contain only ASCII characters") from e


def b64encode(toencode: bytes) -> bytes:
    """Encode a byte string using Base64.

    toencode is the byte string to encode.  Optional altchars must be a byte
    string of length 2 which specifies an alternative alphabet for the
    '+' and '/' characters.  This allows an application to
    e.g. generate url or filesystem safe Base64 strings.

    The encoded byte string is returned.
    """
    # Strip off the trailing newline
    return binascii.b2a_base64(toencode)[:-1]


def b64decode(todecode: str) -> bytes:
    """Decode a Base64 encoded byte string.

    todecode is the byte string to decode.  Optional altchars must be a
    string of length 2 which specifies the alternative alphabet used
    instead of the '+' and '/' characters.

    The decoded string is returned.  A binascii.Error is raised if todecode is
    incorrectly padded.

    If validate is False (the default), non-base64-alphabet characters are
    discarded prior to the padding check.  If validate is True,
    non-base64-alphabet characters in the input result in a binascii.Error.
    """
    return binascii.a2b_base64(_bytes_from_decode_data(todecode))
