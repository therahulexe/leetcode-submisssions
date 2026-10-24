
class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []

        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    result.append(".".join(parts))
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]

                # No leading zeros
                if len(part) > 1 and part[0] == '0':
                    continue

                # Each part must be between 0 and 255
                if int(part) > 255:
                    continue

                backtrack(start + length, parts + [part])

        # A valid IP needs exactly 4 digits groups
        if 4 <= len(s) <= 12:
            backtrack(0, [])

        return result
