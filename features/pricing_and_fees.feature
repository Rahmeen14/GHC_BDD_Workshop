Feature: Pricing and fees

  Scenario: Total cost of the flight displayed upfront, including all taxes and fees.
    Given user has entered their travel information
     When they view their search results
     Then the total cost of each flight should be displayed upfront, including all taxes and fees

  Scenario: Option for users to pay in their local currency
    Given user has opened the checkout page
     When they select the "Pay in Local Currency" option
     And  they choose British pounds
     Then the total cost of their booking should be displayed in pounds
     And  the payment should be processed in pounds
