*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  aaaaaaaa
    Set Password  aaaaaaa1
    Set Password Confirmation  aaaaaaa1
    Click  button >> text=Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  aa
    Set Password  aaaaaaa1
    Set Password Confirmation  aaaaaaa1
    Click  button >> text=Register
    Register Should Fail With Message  Invalid username or password

Register With Valid Username And Too Short Password
    Set Username  aaa
    Set Password  a
    Set Password Confirmation  a
    Click  button >> text=Register
    Register Should Fail With Message  Invalid username or password


Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Fail With Message  Invalid username or password


Register With Password Containing Letters And Numbers
    Set Username  newuser
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Letters And Special Characters
    Set Username  newuser
    Set Password  kalle#abc
    Set Password Confirmation  kalle#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing Only Lowercase Letters
    Set Username  newuser
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click  button >> text=Register
    Register Should Fail With Message  Invalid username or password

Register With Password Containing Only Mixed Case Letters
    Set Username  newuser
    Set Password  KalleKalle
    Set Password Confirmation  KalleKalle
    Click  button >> text=Register
    Register Should Fail With Message  Invalid username or password


Register With Matching Password Confirmation
    Set Username  newuser
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Nonmatching Password Confirmation
    Set Username  newuser
    Set Password  kalle123
    Set Password Confirmation  kalle456
    Click  button >> text=Register
    Register Should Fail With Message  Password and password confirmation do not match


*** Keywords ***
Register Should Succeed
    Get Title  ==  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Set Password Confirmation
    [Arguments]  ${password}
    Fill Secret  id=password_confirmation  $password

Reset Application Create User And Go To Register Page
  Reset Application
  Create User  kalle  kalle123
  Go To Register Page
