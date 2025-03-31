import unittest
from standardizationer import Standardization
from normalizer import Normalizer


class TestFeatureScalingML(unittest.TestCase):

    inputData = []

    # The setUp method is a special method that is called before each test method
    # It is used to set up the test environment
    def setUp(self):
        print("Setting up test environment...")
        TestFeatureScalingML.inputData = [
            {
                "id": "blue",
                "name": "Lura Senger",
                "email": "XXXXXXXXXXXXXXXXXXXXXXXX",
                "salary": 70000,
                "age": 45,
            },
            {
                "id": "purple",
                "name": "Wilburn Weber",
                "email": "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
                "salary": 60000,
                "age": 44,
            },
            {
                "id": "red",
                "name": "Lampard Cauteru",
                "email": "XXXXXXXXXXXXXXXXXXXXXXXXXXX",
                "salary": 52000,
                "age": 40,
            },
        ]

    # The tearDown method is a special method that is called after each test method
    # It is used to clean up the test environment
    def tearDown(self):
        print("Cleaning up test environment...")

    # The test method is a special method that is called to run the test
    # It is used to test the functionality of the code
    # The test method is called by the unittest framework

    def test_normalizer_salary(self):
        normalizer = Normalizer("normalizer")
        normalizedDataResp = normalizer.normalizeData(
            TestFeatureScalingML.inputData, "salary"
        )
        print(normalizedDataResp)
        # find the item for id=red
        for item in normalizedDataResp:
            if item["id"] == "purple":
                self.assertEqual(0.444, item["salary"]["normalized"])

    def test_normalizer_age(self):
        normalizer = Normalizer("normalizer")
        normalizedDataResp = normalizer.normalizeData(
            TestFeatureScalingML.inputData, "age"
        )
        print(normalizedDataResp)
        # find the item for id=purple
        for item in normalizedDataResp:
            if item["id"] == "purple":
                self.assertEqual(0.8, item["age"]["normalized"])

    def test_standardizer_salary(self):
        standardizer = Standardization("standardizer")
        standardizedDataResp = standardizer.standardizeData(
            TestFeatureScalingML.inputData, "salary"
        )
        print(standardizedDataResp)
        # find the item for id=red
        for item in standardizedDataResp:
            if item["id"] == "purple":
                self.assertEqual(-0.0905357460425182, item["salary"]["standardized"])


# The final block shows a simple way to run the tests
if __name__ == "__main__":
    unittest.main()
