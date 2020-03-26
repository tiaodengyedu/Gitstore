*** Settings ***

Library  	添加客户.py	WITH NAME	M
Force Tags	冒烟

Library  	添加客户.c1	WITH NAME	c1

Library  	添加客户.c2	WITH NAME	c2

Library  	添加客户.c3	WITH NAME	c3
*** Test Cases ***
API-0151
  [Teardown]    c1.teardown

  c1.teststeps
API-0152
  [Setup]    c2.setup
  [Teardown]    c2.teardown

  c2.teststeps
API-0153

  [Tags]	触发错误	 

  c3.teststeps