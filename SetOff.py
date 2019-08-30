from Utils import Utils
import random
import time


class SetOff:
    payee_id = ['17031994', '77778888', '86915977', '02228898', '00008037', '00092757', '003646445', '00001182',
                '00471885', '84168159', '25293353', '02664656', '47813265', '00891529', '05544509', '87613918',
                '70985319', '37464898', '27949116', '06922436', '06605211', '05020569', '01801161', '01234557']
    setOffFormData = {
        'payeeId': payee_id[random.randint(0, len(payee_id)-1)],
        'reAllocate': None,
        'customsOfficeCode': '05100010',
        'taxCode': '4521',
        'budgetAccount': '900005004271',
        'notes': '12312',
        'overPaymentsByLines[1].amountToUse': '1',
        #'operationTransmit': None,
        #'confirmOper': None
    }

    @staticmethod
    def set_off():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        time.sleep(1)
        Utils.driver.find_element_by_id('clearCriteria').click()
        time.sleep(1)
        Utils.check_select('iff', 1)
        time.sleep(1)
        Utils.fill_form(SetOff.setOffFormData)
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationTransmit').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
