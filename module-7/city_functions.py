# Name: Verdis Moorer
# Course: CSD-325
# Module: 7
# Assignment: Testing Functions
# Date: September 20, 2026

def city_country(city, country, population=None, language=None):
    """Return city and country with optional population and language."""
    location = f"{city}, {country}"

    if population is not None:
        location += f" - population {population}"

    if language is not None:
        location += f", {language}"

    return location


print(city_country("Tampa", "United States"))
print(city_country("Santiago", "Chile", 5000000))
print(city_country("Paris", "France", 2100000, "French"))
