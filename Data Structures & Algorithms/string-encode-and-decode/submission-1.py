class Solution:

    def encode(self, strs: List[str]) -> str:
        return_str = ''
        for strings in strs:
            for char in strings:
                return_str += char
            return_str += '~'
        return return_str
    def decode(self, s: str) -> List[str]:
        return_list = []
        return_str = ''
        for char in s:
            if char == '~':
                return_list.append(return_str)
                return_str = ''
            else:
                return_str += char
        return return_list
