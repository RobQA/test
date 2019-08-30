from Utils import Utils
import random
import time

co_tt_bl = []
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '17031994', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100011', 'taxType': '1010', 'bl': '900013555017', 'tin': '77778888', 'documentType': '082',
                 'docNumber': '00999999999999999', 'pay': '9999999999999', 'notes': 'fdf2534'})
co_tt_bl.append({'co': '05100011', 'taxType': '1010', 'bl': '900013555017', 'tin': '86915977', 'documentType': '082',
                 'docNumber': '2345', 'pay': '9999999999999', 'notes': 'fdf2534'})
co_tt_bl.append({'co': '05100013', 'taxType': '1011', 'bl': '900013523015', 'tin': '02228898', 'documentType': '088',
                 'docNumber': '2345fgsdfgdffgdg45', 'pay': '99999999999999999',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100015', 'taxType': '1020', 'bl': '900013324018', 'tin': '00008037', 'documentType': '089',
                 'docNumber': '2345fgsdfgdffgdg45', 'pay': '4563456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100016', 'taxType': '1050', 'bl': '900013030011', 'tin': '00092757', 'documentType': '089',
                 'docNumber': '888888888', 'pay': '4563456', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100017', 'taxType': '1090', 'bl': '900013576013', 'tin': '003646445', 'documentType': '082',
                 'docNumber': '85678568567', 'pay': '4563456', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100018', 'taxType': '1510', 'bl': '900013555017', 'tin': '00001182', 'documentType': '081',
                 'docNumber': '8888888888', 'pay': '23465785', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100020', 'taxType': '20', 'bl': '900005014015', 'tin': '00471885', 'documentType': '083',
                 'docNumber': '1234215', 'pay': '99999999999999999',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100021', 'taxType': '2010', 'bl': '900005000618', 'tin': '84168159', 'documentType': '088',
                 'docNumber': '1234215', 'pay': '456366666456', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100022', 'taxType': '2011', 'bl': '900005015012', 'tin': '25293353', 'documentType': '082',
                 'docNumber': '2345fgsfsdffgdg45', 'pay': '99999999999999999',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100030', 'taxType': '2040', 'bl': '900005061370', 'tin': '02664656', 'documentType': '083',
                 'docNumber': '1234215', 'pay': '412346456', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100031', 'taxType': '2041', 'bl': '900005061370', 'tin': '47813265', 'documentType': '082',
                 'docNumber': '1234215', 'pay': '99999999999999999',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100032', 'taxType': '2051', 'bl': '900005061370', 'tin': '00891529', 'documentType': '089',
                 'docNumber': '8888888888', 'pay': '4563456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100033', 'taxType': '30', 'bl': '900005168415', 'tin': '05544509', 'documentType': '089',
                 'docNumber': '1234215', 'pay': '45635665345456', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100034', 'taxType': '4510', 'bl': '900005004230', 'tin': '87613918', 'documentType': '082',
                 'docNumber': '009999999999', 'pay': '4563456', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100035', 'taxType': '4511', 'bl': '900005004230', 'tin': '70985319', 'documentType': '088',
                 'docNumber': '1234215', 'pay': '99999999999999999', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100036', 'taxType': '4520', 'bl': '900005004271', 'tin': '37464898', 'documentType': '083',
                 'docNumber': '888888888888', 'pay': '99999999999999999', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100036', 'taxType': '4520', 'bl': '900005004248', 'tin': '27949116', 'documentType': '081',
                 'docNumber': '2345fggsdffgdg45', 'pay': '99999999999999999',
                 'notes': 'fdfgfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh234'})
co_tt_bl.append({'co': '05100040', 'taxType': 'VCT', 'bl': '900005024055', 'tin': '06922436', 'documentType': '082',
                 'docNumber': '66666666666', 'pay': '345634699788', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100041', 'taxType': 'MVT', 'bl': '900293063013', 'tin': '06605211', 'documentType': '083',
                 'docNumber': '0099999999999', 'pay': '56745674567',
                 'notes': 'fdgfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghf234'})
co_tt_bl.append({'co': '05100041', 'taxType': 'MTT', 'bl': '900005014015', 'tin': '05020569', 'documentType': '088',
                 'docNumber': '2345fgsdfffgdg45', 'pay': '2345234537347',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100041', 'taxType': 'MCV', 'bl': '900293063013', 'tin': '01801161', 'documentType': '082',
                 'docNumber': '1234215', 'pay': '4563456', 'notes': 'fdf234'})
co_tt_bl.append({'co': '05100041', 'taxType': 'HVT', 'bl': '900005012134', 'tin': '01234557', 'documentType': '089',
                 'docNumber': '2345fgsdsdffgdg45', 'pay': '8888888888',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '01234557', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '01801161', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '05020569', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '06605211', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '06922436', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '27949116', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '37464898', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '70985319', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '87613918', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '05544509', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '00891529', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '02664656', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '47813265', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '25293353', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '84168159', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '00471885', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '00001182', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '003646445', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '00092757', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '00008037', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '02228898', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '01529053', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})
co_tt_bl.append({'co': '05100010', 'taxType': '10', 'bl': '900013323010', 'tin': '77778888', 'documentType': '081',
                 'docNumber': '1234215', 'pay': '1234123456',
                 'notes': 'gfhdgerytrrrrrrrrrrrrrrrrrrrr6thdghdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdghgfhdgeryt67yurrrrrrrrrrrrrrrrrrrrrrrrrrrrr6thdgh'})


class IncreaseOverpayment:

    @staticmethod
    def x(obj):
        return {
            'customsOfficeCode': obj['co'],
            'payeeId': obj['tin'],
            'taxCode': obj['taxType'],
            'budgetAccount': obj['bl'],
            'amount': obj['pay'],
            'paymentDocumentNumber': obj['docNumber'],
            'notes': obj['notes'],
            #'operationIncreaseOverpayment': None,
            #'confirmOper': None
        }

    @staticmethod
    def increase_overpayment():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cap/payment/increaseOverpayment?lang=ru')
        Utils.check_select('iff', 1)
        Utils.set_date('paymentDate', '17/01/2018')
        rInt = random.randint(0, len(co_tt_bl) - 1)
        Utils.fill_form(IncreaseOverpayment.x(co_tt_bl[rInt]))
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationIncreaseOverpayment').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
