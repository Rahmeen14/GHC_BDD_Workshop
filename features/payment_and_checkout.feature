Feature: Payment and Checkout

  Scenario: Multiple payment options on the Website
    Given user has opened the payment page
     When they select the "Pay with PayPal" option
     Then they should be directed to the PayPal website to complete the payment process
     And  they should receive confirmation of their booking

  Scenario: Website provides confirmation page and email with all the details of the booking
    Given user has completed the payment process
     When they are directed to the confirmation page
     Then they should receive a confirmation email
     And  they should see all the details of their booking, including the flight itinerary, total cost, and any special requests
