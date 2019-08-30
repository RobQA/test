from selenium import webdriver


from Roles import Roles
from Logout import Logout
from TestCase import TestCase
from TestGroup import TestGroup
from Utils import Utils
from External import External

driver = webdriver.Chrome()
driver.implicitly_wait(1)
Utils.driver = driver

payViaExternalPDCSTEPS = [
    {'func': Utils.login1, 'args': [Roles.CAP_EXTERNAL]},
    {'func': External.pay_via_external_pdc, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]

PDC = TestCase('PAY_VIA_EXTERNAL_PDC', payViaExternalPDCSTEPS, '')

payViaExternalTDPSTEPS = [
    #{'func': Utils.login2, 'args': [Roles.CAP_EXTERNAL]},
    {'func': External.pay_via_external_tdp, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]

TDP = TestCase('PAY_VIA_EXTERNAL_TDP', payViaExternalTDPSTEPS, '')

payViaExternalCUSADSTEPS = [
    #{'func': Utils.login2, 'args': [Roles.CAP_EXTERNAL]},
    {'func': External.pay_via_external_cusad, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]

CUSAD = TestCase('PAY_VIA_EXTERNAL_CUSAD', payViaExternalCUSADSTEPS, '')

payViaExternalPICSSTEPS = [
    #{'func': Utils.login2, 'args': [Roles.CAP_EXTERNAL]},
    {'func': External.pay_via_external_pics, 'args': None},
    {'func': Logout.logout, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]

PICS = TestCase('PAY_VIA_EXTERNAL_PICS', payViaExternalPICSSTEPS, '')

payViaExternalCUSADLIMITSTEPS = [
    {'func': Utils.login2, 'args': [Roles.CAP_EXTERNAL_LIMIT]},
    {'func': External.pay_via_external_cusad_limit, 'args': None},
    #{'func': Utils.close_browser, 'args': None}
]

CUSAD_LIMIT = TestCase('PAY_VIA_EXTERNAL_CUSAD_LIMIT', payViaExternalCUSADLIMITSTEPS, '')

TestGroup('TEST_CROUP_EXTERNAL_ROLL', [PDC, TDP, CUSAD, PICS, CUSAD_LIMIT])


