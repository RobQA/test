from Utils import Utils
import random


class ViewOverpaymentsDebts:
    payee_id = ['17031994', '77778888', '86915977', '02228898', '00008037', '00092757', '003646445', '00001182',
                '00471885', '84168159', '25293353', '02664656', '47813265', '00891529', '05544509', '87613918',
                '70985319', '37464898', '27949116', '06922436', '06605211', '05020569', '01801161', '01234557']
    customs_Office_Code = ['05100041', '05100040', '05100034', '05100033', '05100031', '05100030', '05100022', '05100021', '05100020', '05100018', '05100011', '05100010', '05100035', '05100032', '05100017', '05100016', '05100015', '05100013', '05100012', '05100036']
    document_Code = ['25', '02', '55', 'БЗ', 'БН', 'НР', 'ПК', 'ПС']
    viewOverpaymentsDebtsFormData = {
        'payeeId': payee_id[random.randint(0, len(payee_id)-1)],
        'customsOfficeCode': customs_Office_Code[random.randint(0, len(customs_Office_Code)-1)],
        'documentCode': document_Code[random.randint(0, len(document_Code)-1)],
        'showOverpayments': None,

    }

    @staticmethod
    def view_overpayments_debts():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        Utils.check_select('iff', 1)
        Utils.fill_form(ViewOverpaymentsDebts.viewOverpaymentsDebtsFormData)
        driver.find_element_by_class_name('btn').click()
        driver.get('https://uatapp3.fipsoft.com/cap/?lang=ru')
        driver.find_element_by_class_name('clearCriteria').click()
