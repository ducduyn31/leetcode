import unittest
from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return '//s'.join(strs)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return s.split('//s')


class CodecTest(unittest.TestCase):

    def setUp(self) -> None:
        self.codec = Codec()

    def test_codec_should_work_with_strs(self):
        inp = ['Hello', 'World']
        self.assertCountEqual(inp, self.codec.decode(self.codec.encode(inp)))

    def test_codec_should_work_with_empty_strs(self):
        inp = ['']
        self.assertCountEqual(inp, self.codec.decode(self.codec.encode(inp)))
