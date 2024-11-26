def categorize_health(bp, fbs):
    if bp <= 120 and fbs < 100:
        return "General"
    elif 120 < bp <= 139 and 100 <= fbs <= 125:
        return "Risk"
    elif 140 <= bp <= 159 and 125 <= fbs <= 154:
        return "High Risk 1"
    elif 160 <= bp <= 179 and 155 <= fbs <= 182:
        return "High Risk 2"
    elif bp >= 180 and fbs >= 183:
        return "High Risk 3"
    else:
        return "Uncategorized"


bp = 160
fbs = 180
print(categorize_health(bp, fbs))

import unittest

class TestHealthCategorization(unittest.TestCase):
    def test_General(self):
        self.assertEqual(categorize_health(120, 99), "General")
        self.assertEqual(categorize_health(110, 90), "General")

    def test_Risk(self):
        self.assertEqual(categorize_health(125, 110), "Risk")
        self.assertEqual(categorize_health(130, 120), "Risk")
        self.assertEqual(categorize_health(139, 125), "Risk")

    def test_High_Risk_1(self):
        self.assertEqual(categorize_health(150, 130), "High Risk 1")
        self.assertEqual(categorize_health(140, 150), "High Risk 1")

    def test_High_Risk_2(self):
        self.assertEqual(categorize_health(170, 160), "High Risk 2")
        self.assertEqual(categorize_health(160, 180), "High Risk 2")

    def test_High_Risk_3(self):
        self.assertEqual(categorize_health(190, 190), "High Risk 3")
        self.assertEqual(categorize_health(180, 185), "High Risk 3")

    def test_uncategorized(self):
        self.assertEqual(categorize_health(125, 90), "Uncategorized")
        self.assertEqual(categorize_health(130, 99), "Uncategorized")
        self.assertEqual(categorize_health(139, 126), "Uncategorized")
        self.assertEqual(categorize_health(160, 120), "Uncategorized")

if __name__ == '__main__':
    unittest.main() 