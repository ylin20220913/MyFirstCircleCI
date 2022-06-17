*** Settings ***
Library         m7ats.device.Device

*** Test Cases ***
Test
    ${result}=        Convert to integer    0
    turn device input off    ${result}
    sleep    5s
    turn device input on    ${result}
    sleep    5s
    turn device input off    ${result}
    sleep    5s
    