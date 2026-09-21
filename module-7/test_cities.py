# Name: Verdis Moorer
# Course: CSD-325
# Module: 7
# Assignment: Testing Functions
# Date: September 20, 2026

import unittest
from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):
    """Tests for the city_country function."""

    def test_city_country(self):
        """Test that Santiago, Chile is formatted correctly."""
        formatted_location = city_country("Santiago", "Chile")
        self.assertEqual(formatted_location, "Santiago, Chile")


if __name__ == "__main__":
    unittest.main()

