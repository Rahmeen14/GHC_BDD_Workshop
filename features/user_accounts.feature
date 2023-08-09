Feature: User Accounts

  Scenario: Users should be able to easily log in and access their account information.
    Given user has created an account on the website
     When they log in to their account
     Then they should be able to view their booking history
     And  they should be able to view their upcoming flights
     And  they should be able to make changes to their bookings as needed

  Scenario: Users should be able to manage their personal information and preferences
    Given user logged in to their account
     When they navigate to the account settings page
     Then they should be able to update their personal information like contact information
     And  they should be able to update their preferences like food, seat etc

  Scenario: Users should earn loyalty points for their flights and redeem them for future bookings
    Given user is enrolled in the loyalty program
     When they they book a flight
     Then they should earn loyalty points for that booking
     And  they should be able to view their balance points
     And  they should be able to redeem points for future bookings
    



