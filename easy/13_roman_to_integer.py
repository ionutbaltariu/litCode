class Solution:
    def romanToInt(self, s: str) -> int:
        l = len(s)
        i = 0
        num = 0

        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        composite_numbers = {
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4
        }

        while i < l - 1:
            if (cn := s[i:i+2]) in composite_numbers:
                num += composite_numbers[cn]
                i += 2
            else:
                num += values[s[i]]
                i += 1

        if i == l - 1:
            num += values[s[i]]

        return num

