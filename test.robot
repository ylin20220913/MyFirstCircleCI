*** Settings ***
Library         m7ats.device.Device

*** Test Cases ***
Test
    turn_all_device_inputs_off
    sleep    2s
    turn_all_device_inputs_on
    sleep    2s
    turn_all_device_inputs_off
    sleep    2s
