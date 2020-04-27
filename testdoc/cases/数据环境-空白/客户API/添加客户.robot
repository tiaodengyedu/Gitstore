*** Settings ***

Library  	添加客户.py	WITH NAME	M

Force Tags	冒烟

Library  	添加客户.C1	WITH NAME	C1

Library  	添加客户.C2	WITH NAME	C2

Library  	添加客户.C3	WITH NAME	C3
*** Test Cases ***
'API-0151'
  [Teardown]    C1.teardown

  C1.teststeps
'API-0152'
  [Setup]    C2.setup
  [Teardown]    C2.teardown

  C2.teststeps
'API-0153'

  [Tags]	触发错误

  C3.teststeps