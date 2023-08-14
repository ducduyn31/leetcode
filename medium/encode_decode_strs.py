import unittest
from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        return ','.join([self.encode_str(s) for s in strs])

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        return list(map(lambda encoded: self.decode_str(encoded), s.split(',')))

    def encode_str(self, s: str):
        lookup = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+/'
        bytes_representation = s.encode('ascii')
        result = []

        for i in range(0, len(bytes_representation), 3):
            current_chunk = bytes_representation[i:i + 3]
            chunk_len = len(current_chunk)
            n = int.from_bytes(current_chunk, byteorder='big')

            parts, remain_bits = divmod(chunk_len * 8, 6)

            for j in range(parts):
                mask = (1 << 6) - 1
                x = (n >> (6 * (parts - 1 - j) + remain_bits)) & mask
                result.append(lookup[x])

            if chunk_len < 3:
                mask = (1 << remain_bits) - 1
                x = (n & mask) << (6 - remain_bits)
                result.append(lookup[x])
                result.extend(['='] * (3 - parts))

        return ''.join(result)

    def decode_str(self, s: str):
        lookup = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                  'C': 12,
                  'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23,
                  'O': 24,
                  'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35,
                  'a': 36,
                  'b': 37, 'c': 38, 'd': 39, 'e': 40, 'f': 41, 'g': 42, 'h': 43, 'i': 44, 'j': 45, 'k': 46, 'l': 47,
                  'm': 48,
                  'n': 49, 'o': 50, 'p': 51, 'q': 52, 'r': 53, 's': 54, 't': 55, 'u': 56, 'v': 57, 'w': 58, 'x': 59,
                  'y': 60,
                  'z': 61, '+': 62, '/': 63}

        result = bytearray()

        for i in range(0, len(s), 4):
            current_chunk = s[i:i + 4]
            value = 0
            padding = 0
            for c in current_chunk:
                if c == '=':
                    padding += 1
                    continue
                value <<= 6
                value += lookup[c]

            chunk_len = (24 - padding * 6) // 8
            value >>= (2 * padding)

            result.extend(value.to_bytes(chunk_len, byteorder='big'))

        return result.decode('ascii')


class CodecTest(unittest.TestCase):

    def setUp(self) -> None:
        self.codec = Codec()

    def test_codec_should_work_with_strs(self):
        inp = ['Hello', 'World']
        self.assertCountEqual(inp, self.codec.decode(self.codec.encode(inp)))

    def test_codec_should_work_with_empty_strs(self):
        inp = ['']
        self.assertCountEqual(inp, self.codec.decode(self.codec.encode(inp)))
