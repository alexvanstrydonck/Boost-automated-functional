Feature: loginBackEndApi

  Scenario: As a technician, I want to login the backEndApi
     Given i m authorized to log in the backEndApi
     When I log in the backEndApi
     Then i'm authenticated to the backEndApi