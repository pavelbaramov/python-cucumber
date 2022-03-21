#Feature: Compose Message
#
#    @compose_message
#    Scenario: Compose message with recipient, subject, message body and validate it was sent
#        Given user is on the inbox page
#        When user composes a message with recipient "recipient@recipient's_email.com" and subject "Test Subject" and message "Test Message"
#        And user sends message
#        Then the message is sent successfully