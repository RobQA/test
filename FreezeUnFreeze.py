from Utils import Utils
import random
import time

class FreezeUnFreeze:
    freezeUnFreezeFormData = {
        'payeeId': '17031994',
        'updateFrozenAmounts': None,
        'notes': '123123',
        'overPayments[0].freeze': None,
        'overPayments[0].amountToUse': '1',
        'overPayments[1].freeze': None,
        'overPayments[1].amountToUse': '123',
        #'operationUpdateFrozenAmounts': None,
        #'confirmOper': None

    }

    @staticmethod
    def un_freeze():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        time.sleep(1)
        Utils.check_select('iff', 1)
        time.sleep(1)
        Utils.driver.find_element_by_id('payeeId').send_keys('17031994')
        time.sleep(1)
        Utils.driver.find_element_by_id('updateFrozenAmounts').click()
        Utils.driver.find_element_by_id('overPayments[0].freeze').click()
        Utils.driver.find_element_by_id('overPayments[1].amountToUse').send_keys('1')
        Utils.fill_form(FreezeUnFreeze.freezeUnFreezeFormData)
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationUpdateFrozenAmounts').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()

    ###############################################################################################################

    payee_id = ['17031994', '77778888', '86915977', '02228898', '00008037', '00092757', '003646445', '00001182',
                '00471885', '84168159', '25293353', '02664656', '47813265', '00891529', '05544509', '87613918',
                '70985319', '37464898', '27949116', '06922436', '06605211', '05020569', '01801161', '01234557']
    freezeFormData = {
        'payeeId': payee_id[random.randint(0, len(payee_id)-1)],
        'updateFrozenAmounts': None,
        'notes': '123123',
        'overPayments[5].amountToUse': '1',
        #'operationUpdateFrozenAmounts': None,
        #'confirmOper': None
    }

    @staticmethod
    def freeze():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.driver.find_element_by_id('clearCriteria').click()
        Utils.check_select('iff', 1)
        Utils.fill_form(FreezeUnFreeze.freezeFormData)
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationUpdateFrozenAmounts').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
