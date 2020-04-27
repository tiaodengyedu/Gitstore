*** Settings ***

Library  	UI-0101.py	WITH NAME	M
Library  	UI-0101.C1	WITH NAME	C1

Suite Setup    M.suite_setup

Suite Teardown    M.suite_teardown


*** Test Cases ***

'UI-0101'

  C1.teststeps