# CheckMK Special Agent for Mirth Connect

## Tested with Mirth Connect versions 3.12 and 4.4.0

## How to use
- Install the mkp package in Checkmk. [HowTo](https://docs.checkmk.com/latest/en/mkps.html)
- Activate the special agent with the rule "Mirth Special Agent Configuration"
- If you want to verify the ssl certificate, the CA certificate has to be imported on the checkmk operating system

## What is monitored

- Mirth channel status and connection states (warning and error states are triggered only from the channel status, error states for connections are logged by the logwatch service)
- Channel metrics are collected (packets per check interval)
- Server logs and connection logs are created as Logwatch service (can be disabled)

## Additional WATO rules

- Change channel parameters with the rule "Mirth Channel Parameters"

## Debugging problems
If you experience errors, try to run the special agent in the console and check the output

Sample command: ```python3 agent_mirth -i <mirth_ip> -u <username> -s <secret> -p 8443 -ls```

For further information append the ```-d``` flag (debug mode)