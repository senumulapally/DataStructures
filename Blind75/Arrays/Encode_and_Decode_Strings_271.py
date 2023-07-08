"""
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.

Machine 1 (sender) has the function:

string encode(vector<string> strs) {
  // ... your code
  return encoded_string;
}
Machine 2 (receiver) has the function:
vector<string> decode(string s) {
  //... your code
  return strs;
}
So Machine 1 does:

string encoded_string = encode(strs);
and Machine 2 does:

vector<string> strs2 = decode(encoded_string);
strs2 in Machine 2 should be the same as strs in Machine 1.

Implement the encode and decode methods.

You are not allowed to solve the problem using any serialize methods (such as eval).


Example 1:
Input: dummy_input = ["Hello","World"]
Output: ["Hello","World"]
Explanation:
Machine 1:
Codec encoder = new Codec();
String msg = encoder.encode(strs);
Machine 1 ---msg---> Machine 2

Machine 2:
Codec decoder = new Codec();
String[] strs = decoder.decode(msg);

Example 2:
Input: dummy_input = [""]
Output: [""]


Sol: Encode is sone by adding length of the string and # before the string
While decoding, Get the number while s!=# and then consider the chars from char after the # to the len(s) as a complete
string and append it to the result. Then re assign 'i' to the next char of string. Repeat until you loop complete string.
"""


class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        result = ''
        for s in strs:
            result += str(len(s)) + '#' + s
        return result

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        i = 0
        res = []
        while i<len(s):
            j = i
            while s[j] != '#':
                j += 1
            num = int(s[i:j])
            res.append(s[j+1:j+1+num])
            i = j+1+num
        return res

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))


obj = Codec()
print(obj.decode(obj.encode(["63/Rc","h","BmI3FS~J9#vmk","7uBZ?7*/","24h+X","O "])))