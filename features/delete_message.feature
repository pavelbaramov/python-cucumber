#Feature: Delete Message
#
#    @delete_message
#    Scenario: Compose then delete message
#        Given user is on the inbox page
#        And user composes a message with recipient "recipient@recipient's_email.com" and subject "Test Subject" and message "Test Message"
#        And user sends message
#        When user deletes the message
#        Then the message is successfully deleted
