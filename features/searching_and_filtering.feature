Feature: Searching and Filtering

  Scenario: Users should be able to filter and sort results based on dates, destinations, price, duration, and number of stops.
    Given user has opened the flight search page
     When they select the "Non-stop" filter
     Then they should only see search results for flights that do not have any stops

  Scenario: Users should be able to search for flights by flexible dates.
    Given user has opened the flight search page
     When they select the "Flexible Dates" option
     And  they choose the month of August
     Then they should see a list of flights for that month sorted by price

  Scenario: Users should be able to save their search results and receive email alerts for price drops
    Given user has performed a flight search
     When they save their search results
     And  they enable email alerts
     Then they should receive an email notification if the prices for that flight route drop

