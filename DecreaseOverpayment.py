from Utils import Utils
import random
import time


class DecreaseOverpayment:
    payee_id = ['17031994', '77778888', '86915977', '02228898', '00008037', '00092757', '003646445', '00001182',
                '00471885', '84168159', '25293353', '02664656', '47813265', '00891529', '05544509', '87613918',
                '70985319', '37464898', '27949116', '06922436', '06605211', '05020569', '01801161', '01234557']
    decreaseOverpaymentFormData = {
        'payeeId': payee_id[random.randint(0, len(payee_id)-1)],
        'decreaseOverpayment': None,
        'customsOfficeCode': '05100010',
        'notes': '123',
        'overPaymentsByLines[1].amountToUse': '1',
        #'operationDecreaseOverpayment': None,
        #'confirmOper': None
    }

    @staticmethod
    def decrease_overpayment():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        time.sleep(1)
        Utils.driver.find_element_by_id('clearCriteria').click()
        time.sleep(1)
        Utils.check_select('iff', 1)
        time.sleep(1)
        Utils.fill_form(DecreaseOverpayment.decreaseOverpaymentFormData)
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationDecreaseOverpayment').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()

