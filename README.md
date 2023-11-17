# CheckMK Special Agent for Mirth Connect

## Tested with Mirth Connect versions 3.12 to 4.4.0

## How to use

- Activate the special agent with the rule "Mirth Special Agent Configuration"
- You need credentials for the Mirth API
- If you want to verify the ssl certificate, the root certificate has to be imported on the checkmk operating system

## What is monitored

- Mirth channel status and connection states (warning and error states are triggered only from the channel status currently)
- Channel metrics are collected (packets per check interval)
- Server logs and connection logs are created as Logwatch service (can be disabled)

## Additional WATO rules

- Change channel parameters with the rule "Mirth Channel Parameters"