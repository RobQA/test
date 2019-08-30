import time
from selenium.webdriver.support.wait import WebDriverWait
import random
from selenium.webdriver.common.keys import Keys



from Utils import Utils


class External:

    payViaExternalPDCFormData = {
        'customsOfficeCode': '05100010',
        'importerTIN': '17031994',
        'responsiblePerson': '64534575',
    }

    @staticmethod
    def pay_via_external_pdc():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/pdc/pdc/create/?lang=ru')
        Utils.check_select('applicantType', 0)
        Utils.fill_form(External.payViaExternalPDCFormData)
        time.sleep(2)
        driver.find_element_by_partial_link_text('Товар').click()
        Utils.driver.find_element_by_id('productName').send_keys('123412')
        Utils.driver.find_element_by_id('productDescription').send_keys('1235')
        Utils.driver.find_element_by_id('operationStore').click()
        Utils.driver.find_element_by_id('confirmOper').click()
        time.sleep(1)
        driver.find_element_by_class_name('glyphicon-pencil').click()
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[1])
        Utils.driver.find_element_by_id('operationSubmitCreated').click()
        Utils.driver.find_element_by_id('confirmOper').click()
        driver.find_element_by_partial_link_text('Платежи').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Оплата').click()
        driver.switch_to.window(driver.window_handles[2])
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        driver.find_element_by_class_name('serviceLink').click()
        driver.find_element_by_class_name('glyphicon-time').click()
        driver.find_element_by_class_name('operationLink').click()
        driver.find_element_by_class_name('serviceLink').click()
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationPayFromOverpaymentClass').click()
        Utils.driver.find_element_by_id('overPayments[12].amountToUse').send_keys('1')
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationPayFromOverpayment').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-eye-open")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-print")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-time")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        driver.find_element_by_css_selector("#paymentsTable .detailsOperationLink")
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationAddPaymentOrderClass').click()
        Utils.driver.find_element_by_id('modeOfPayment').send_keys('БЗ')
        Utils.driver.find_element_by_id('bankBranch').send_keys('111')
        Utils.driver.find_element_by_id('bankAccount').send_keys('123123')
        Utils.driver.find_element_by_id('notes').send_keys('123123')
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationCreate').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-pencil")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('operationUpdateClass').click()
        Utils.driver.find_element_by_id('modeOfPayment').clear()
        Utils.driver.find_element_by_id('modeOfPayment').send_keys('БН')
        Utils.driver.find_element_by_id('bankBranch').clear()
        Utils.driver.find_element_by_id('bankBranch').send_keys('16605')
        Utils.driver.find_element_by_id('bankAccount').clear()
        Utils.driver.find_element_by_id('bankAccount').send_keys('4567456')
        Utils.driver.find_element_by_id('notes').clear()
        Utils.driver.find_element_by_id('notes').send_keys('666666')
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationUpdate').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-time")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector("#paymentsTable .operationLink")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-eye-open")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-print")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-pencil")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('operationPayClass').click()
        Utils.driver.find_element_by_id('paidAmount').send_keys('100000')
        Utils.driver.find_element_by_id('paymentDocumentNumber').send_keys('100000')
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationPay').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()

    payViaExternalTDPFormData = {
        'registrationCustomsOfficeCode': '05100010',
        'destinationCountryCode': 'BY',
        'destinationCustomsCode': '11206505',
        'transitCustomOffices[0].code': '12401000',
        'totalNumberOfPackages': '123',
        'totalInvoiceCost': '123',
        'totalCurrencyCode': 'USD'
    }

    @staticmethod
    def pay_via_external_tdp():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/trade/?lang=ru')
        driver.get('https://uatapp3.fipsoft.com/tdp/transit/create?movementKind=TS')
        Utils.fill_form(External.payViaExternalTDPFormData)
        Utils.set_date('transitDateLimit', '17/01/2019')
        driver.find_element_by_partial_link_text('Стороны').click()
        Utils.driver.find_element_by_id('carrierOrganizationName').send_keys('аыва')
        Utils.driver.find_element_by_id('carrierAddresses[0].addressLine').send_keys('ыаыва')
        Utils.check_select('declarantIFF', 0)
        Utils.driver.find_element_by_id('declarantInn').send_keys('17031994')
        Utils.check_select('consignments[0].consignorIFF', 1)
        Utils.driver.find_element_by_id('consignments[0].consignorInn').send_keys('17031994')
        Utils.driver.find_element_by_id('consignments[0].consigneeAddress.countryCode').send_keys('AM')
        Utils.check_select('consignments[0].consigneeIFF', 1)
        Utils.driver.find_element_by_id('consignments[0].consigneeInn').send_keys('17031994')
        Utils.check_select('ffPersonIFF', 0)
        Utils.driver.find_element_by_id('ffPersonInn').send_keys('17031994')
        driver.execute_script("window.scrollTo( 0, 0 );")
        driver.find_element_by_partial_link_text('Транспортное').click()
        Utils.driver.find_element_by_id('departureVidTrans').send_keys('12')
        Utils.driver.find_element_by_id('departureTransportMeans[0].identityNumber').send_keys('2345')
        Utils.driver.find_element_by_id('guarantees[0].number').send_keys('345234')
        Utils.driver.find_element_by_id('goodsLocationCode').send_keys('MHT00014')
        driver.find_element_by_partial_link_text('Товары').click()
        Utils.driver.find_element_by_id('addItem').click()
        Utils.driver.find_element_by_id('tnVEDCode').send_keys('12030000000')
        Utils.driver.find_element_by_id('description').send_keys('апывап')
        Utils.driver.find_element_by_id('grossWeight').send_keys('123')
        Utils.driver.find_element_by_id('invoiceCost').send_keys('123')
        Utils.driver.find_element_by_id('deiGoodsQuantity').send_keys('123')
        Utils.driver.find_element_by_id('saveAddedItem').click()
        driver.find_element_by_partial_link_text('Документы').click()
        Utils.driver.find_element_by_id('docCode').send_keys('09999')
        Utils.driver.find_element_by_id('docRef').send_keys('123')
        Utils.set_date('docDate', '17/01/2015')
        Utils.driver.find_element_by_id('addAttachedDocument').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('docCode').send_keys('02024')
        Utils.driver.find_element_by_id('docRef').send_keys('123')
        Utils.set_date('docDate', '17/01/2015')
        Utils.driver.find_element_by_id('addAttachedDocument').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Таможенные').click()
        Utils.driver.find_element_by_id('preferenceCode').send_keys('OO')
        time.sleep(1)
        Utils.driver.find_element_by_id('operationSubmit').click()
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.switch_to.window(driver.window_handles[3])  # tab browers
        Utils.driver.find_element_by_id('operationRegister').click()
        Utils.driver.find_element_by_id('confirmOper').click()
        driver.find_element_by_partial_link_text('Платежи').click()
        driver.find_element_by_partial_link_text('Оплата').click()
        driver.switch_to.window(driver.window_handles[4])  # tab browers
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        driver.find_element_by_class_name('serviceLink').click()
        driver.find_element_by_class_name('glyphicon-time').click()
        driver.find_element_by_class_name('operationLink').click()
        driver.find_element_by_class_name('serviceLink').click()
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationPayFromOverpaymentClass').click()
        Utils.driver.find_element_by_id('overPayments[12].amountToUse').send_keys('1')
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationPayFromOverpayment').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-eye-open")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-print")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-time")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        driver.find_element_by_css_selector("#paymentsTable .detailsOperationLink")
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationAddPaymentOrderClass').click()
        Utils.driver.find_element_by_id('modeOfPayment').send_keys('БЗ')
        Utils.driver.find_element_by_id('bankBranch').send_keys('111')
        Utils.driver.find_element_by_id('bankAccount').send_keys('123123')
        Utils.driver.find_element_by_id('notes').send_keys('123123')
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationCreate').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-pencil")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('operationUpdateClass').click()
        Utils.driver.find_element_by_id('modeOfPayment').clear()
        Utils.driver.find_element_by_id('modeOfPayment').send_keys('БН')
        Utils.driver.find_element_by_id('bankBranch').clear()
        Utils.driver.find_element_by_id('bankBranch').send_keys('16605')
        Utils.driver.find_element_by_id('bankAccount').clear()
        Utils.driver.find_element_by_id('bankAccount').send_keys('4567456')
        Utils.driver.find_element_by_id('notes').clear()
        Utils.driver.find_element_by_id('notes').send_keys('666666')
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationUpdate').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-time")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector("#paymentsTable .operationLink")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-eye-open")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-print")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-pencil")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('operationPayClass').click()
        Utils.driver.find_element_by_id('paidAmount').send_keys('100000')
        Utils.driver.find_element_by_id('paymentDocumentNumber').send_keys('100000')
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationPay').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()

    payViaExternalCUSADFormData = {
        'customsModeCode': '40',
        'regCustomsOffices[0].code': '05100010',
        'goodsShipments[0].specificationNumber': '1',
        'goodsShipments[0].specificationListNumber': '1',
        'goodsShipments[0].mainContractTerms.tradeCountryCode': 'AM',
        'goodsShipments[0].mainContractTerms.totalInvoiceAmount': '1',
        'goodsShipments[0].mainContractTerms.contractCurrencyCode': 'ARS'
    }

    @staticmethod
    def pay_via_external_cusad():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get('https://uatapp3.fipsoft.com/cusad/sad/create?customsProcedure=IM&iff=I')
        Utils.fill_form(External.payViaExternalCUSADFormData)
        driver.find_element_by_partial_link_text('Стороны').click()
        Utils.driver.find_element_by_id('goodsShipments[0].consignor.organizationName').send_keys('апр')
        Utils.driver.find_element_by_id('goodsShipments[0].consignor.address.countryCode').send_keys('SD')
        Utils.driver.find_element_by_id('goodsShipments[0].consignee.raOrganizationFeatures.unn').send_keys('17031994')
        Utils.driver.find_element_by_id('goodsShipments[0].finRespPerson.raOrganizationFeatures.unn').send_keys('17031994')
        Utils.driver.find_element_by_id('goodsShipments[0].declarant.raOrganizationFeatures.unn').send_keys('17031994')
        driver.execute_script("window.scrollTo( 0, 0 );")
        driver.find_element_by_partial_link_text('Перевозка').click()
        time.sleep(1)
        Utils.check_select('goodsShipments[0].consigment.containerIndicator', 2)
        Utils.driver.find_element_by_id('goodsShipments[0].consigment.departureArrivalTransport.transportModeCode').send_keys('20')
        Utils.driver.find_element_by_id('goodsShipments[0].consigment.borderTransport.transportModeCode').send_keys('20')
        Utils.driver.find_element_by_id('goodsShipments[0].goodsLocation[0].informationTypeCode').send_keys('21')
        Utils.driver.find_element_by_id('goodsShipments[0].goodsLocation[0].customsOfficeCode').send_keys('05100010')
        Utils.driver.find_element_by_id('goodsShipments[0].goodsLocation[0].goodsLocationPlace.numberCustomsZoneCode').send_keys('05100010')
        driver.execute_script("window.scrollTo( 0, 0 );")
        driver.find_element_by_partial_link_text('Товары').click()
        time.sleep(1)
        driver.find_element_by_class_name('addItemBtn').click()
        Utils.driver.find_element_by_id('goodsTNVEDCode').send_keys('12051090000')
        Utils.driver.find_element_by_id('originCountryCode').send_keys('AE')
        Utils.driver.find_element_by_id('grossWeightQuantity').send_keys('1')
        Utils.driver.find_element_by_id('netWeightQuantity').send_keys('1')
        Utils.driver.find_element_by_id('netWeightQuantity2').send_keys('1')
        Utils.driver.find_element_by_id('customsProcedure.precedingCustomsModeCode').send_keys('00')
        Utils.driver.find_element_by_id('customsProcedure.goodsTransferFeatureCode').send_keys('000')
        Utils.driver.find_element_by_id('supplemGoodsQuantity.goodsQuantity').send_keys('1')
        Utils.driver.find_element_by_id('invoicedCost').send_keys('1')
        Utils.driver.find_element_by_id('customsCostCorrectMethodCode').send_keys('0')
        Utils.check_select('goodsPackaging.pakageTypeCode', 1)
        Utils.driver.find_element_by_id('goodsDsc').send_keys('вапва')
        Utils.driver.find_element_by_id('goodsDscRu').send_keys('вапва')
        Utils.driver.find_element_by_id('saveItem').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Документы').click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#fakePresentedDocuments .addIterativeRecord")
        driver.execute_script("arguments[0].click();", element)
        Utils.driver.find_element_by_id('fakePresentedDocuments[0].presentedDocumentModeCode').send_keys('460')
        Utils.driver.find_element_by_id('fakePresentedDocuments[0].providingIndicationMark').send_keys('0')
        Utils.driver.find_element_by_id('fakePresentedDocuments[0].prDocumentNumber').send_keys('123')
        Utils.set_date('fakePresentedDocuments[0].prDocumentDate', '17/01/2015')
        Utils.driver.find_element_by_id('fakePresentedDocuments[0].goodsNumbers').send_keys('1')
        element = driver.find_element_by_css_selector("#fakePresentedDocuments .addIterativeRecord")
        driver.execute_script("arguments[0].click();", element)
        Utils.driver.find_element_by_id('fakePresentedDocuments[1].presentedDocumentModeCode').send_keys('01999')
        Utils.driver.find_element_by_id('fakePresentedDocuments[1].providingIndicationMark').send_keys('0')
        Utils.driver.find_element_by_id('fakePresentedDocuments[1].prDocumentNumber').send_keys('123')
        Utils.set_date('fakePresentedDocuments[1].prDocumentDate', '17/01/2015')
        Utils.driver.find_element_by_id('fakePresentedDocuments[1].goodsNumbers').send_keys('1')
        Utils.driver.find_element_by_id('operationStore').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        driver.get('https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        element = driver.find_element_by_css_selector("#searchRes .glyphicon-pencil")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[5])
        Utils.driver.find_element_by_id('operationSubmitStored').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        driver.get('https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        element = driver.find_element_by_css_selector("#searchRes .glyphicon-pencil")
        driver.execute_script("arguments[0].click();", element)
        driver.switch_to.window(driver.window_handles[6])
        Utils.driver.find_element_by_id('operationRegisterSubmitted').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_partial_link_text('Платежи').click()
        driver.find_element_by_partial_link_text('Оплата').click()
        driver.switch_to.window(driver.window_handles[7])  # tab browers
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        driver.find_element_by_class_name('serviceLink').click()
        driver.find_element_by_class_name('glyphicon-time').click()
        driver.find_element_by_class_name('operationLink').click()
        driver.find_element_by_class_name('serviceLink').click()
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationPayFromOverpaymentClass').click()
        Utils.driver.find_element_by_id('overPayments[12].amountToUse').send_keys('1')
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationPayFromOverpayment').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-eye-open")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-print")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-time")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        driver.find_element_by_css_selector("#paymentsTable .detailsOperationLink")
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationAddPaymentOrderClass').click()
        Utils.driver.find_element_by_id('modeOfPayment').send_keys('БЗ')
        Utils.driver.find_element_by_id('bankBranch').send_keys('111')
        Utils.driver.find_element_by_id('bankAccount').send_keys('123123')
        Utils.driver.find_element_by_id('notes').send_keys('123123')
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationCreate').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-pencil")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('operationUpdateClass').click()
        Utils.driver.find_element_by_id('modeOfPayment').clear()
        Utils.driver.find_element_by_id('modeOfPayment').send_keys('БН')
        Utils.driver.find_element_by_id('bankBranch').clear()
        Utils.driver.find_element_by_id('bankBranch').send_keys('16605')
        Utils.driver.find_element_by_id('bankAccount').clear()
        Utils.driver.find_element_by_id('bankAccount').send_keys('4567456')
        Utils.driver.find_element_by_id('notes').clear()
        Utils.driver.find_element_by_id('notes').send_keys('666666')
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationUpdate').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-time")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector("#paymentsTable .operationLink")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-eye-open")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-print")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-pencil")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('operationPayClass').click()
        Utils.driver.find_element_by_id('paidAmount').send_keys('100000')
        Utils.driver.find_element_by_id('paymentDocumentNumber').send_keys('100000')
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationPay').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()

    payViaExternalPICSFormData = {
        #'consignmentId': '5126045',
        #'parcelNumber': 'cgte5345dg',
        #'countrySupplyCode': 'AE',
        'totalDeclaredWeight': '123',
        'totalDeclaredValue': '123',
        'currencyCode': 'AED',
        'consignmentId': '756781',

    }

    @staticmethod
    def pay_via_external_pics():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/pics/?lang=ru')
        driver.get('https://uatapp3.fipsoft.com/pics/pics/create?flow=IM')
        Utils.fill_form(External.payViaExternalPICSFormData)
        time.sleep(1)
        driver.find_element_by_partial_link_text('756781').click()
        time.sleep(1)
        Utils.driver.find_element_by_id('parcelNumber').send_keys(random.randint(1000000, 9999999999999999))
        Utils.driver.find_element_by_id('countrySupplyCode').send_keys('AE')
        driver.find_element_by_partial_link_text('Стороны').click()
        time.sleep(1)
        Utils.check_select('amResidentDocType', 5)
        time.sleep(1)
        Utils.driver.find_element_by_id('amResidentDocId').send_keys('234')
        Utils.driver.find_element_by_id('amResidentName').send_keys('234')
        Utils.driver.find_element_by_id('amResidentSurname').send_keys('234')
        Utils.driver.find_element_by_id('amResidentAddress').send_keys('sdf')
        Utils.driver.find_element_by_id('amResidentPhone').send_keys('sdf')
        Utils.driver.find_element_by_id('register').click()
        time.sleep(1)
        Utils.driver.find_element_by_css_selector("div.jconfirm-buttons>.btn-success").click()
        driver.find_element_by_class_name('glyphicon-pencil').click()
        Utils.driver.find_element_by_id('sendRegistered').click()
        Utils.driver.find_element_by_css_selector("div.jconfirm-buttons>.btn-success").click()
        driver.find_element_by_class_name('glyphicon-pencil').click()
        Utils.driver.find_element_by_id('calculateSent').click()
        Utils.driver.find_element_by_css_selector("div.jconfirm-buttons>.btn-success").click()
        time.sleep(10)
        driver.find_element_by_partial_link_text('Платежи').click()
        time.sleep(10)
        driver.find_element_by_partial_link_text('Платежи').click()
        driver.find_element_by_partial_link_text('Оплата').click()
        driver.switch_to.window(driver.window_handles[8])  # tab browers
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        driver.find_element_by_class_name('serviceLink').click()
        driver.find_element_by_class_name('glyphicon-time').click()
        driver.find_element_by_class_name('operationLink').click()
        driver.find_element_by_class_name('serviceLink').click()
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationPayFromOverpaymentClass').click()
        Utils.driver.find_element_by_id('overPayments[12].amountToUse').send_keys('1')
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationPayFromOverpayment').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-eye-open")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-print")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-time")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        driver.find_element_by_css_selector("#paymentsTable .detailsOperationLink")
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationAddPaymentOrderClass').click()
        Utils.driver.find_element_by_id('modeOfPayment').send_keys('БЗ')
        Utils.driver.find_element_by_id('bankBranch').send_keys('111')
        Utils.driver.find_element_by_id('bankAccount').send_keys('123123')
        Utils.driver.find_element_by_id('notes').send_keys('123123')
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationCreate').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-pencil")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('operationUpdateClass').click()
        Utils.driver.find_element_by_id('modeOfPayment').clear()
        Utils.driver.find_element_by_id('modeOfPayment').send_keys('БН')
        Utils.driver.find_element_by_id('bankBranch').clear()
        Utils.driver.find_element_by_id('bankBranch').send_keys('16605')
        Utils.driver.find_element_by_id('bankAccount').clear()
        Utils.driver.find_element_by_id('bankAccount').send_keys('4567456')
        Utils.driver.find_element_by_id('notes').clear()
        Utils.driver.find_element_by_id('notes').send_keys('666666')
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationUpdate').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-time")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector("#paymentsTable .operationLink")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-eye-open")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('serviceLink').click()
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-print")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-pencil")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('operationPayClass').click()
        Utils.driver.find_element_by_id('paidAmount').send_keys('1000000')
        Utils.driver.find_element_by_id('paymentDocumentNumber').send_keys('100000')
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationPay').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()

    payViaExternalCUSADLIMITFormData = {
        'customsModeCode': '40',
        'regCustomsOffices[0].code': '05100010',
        'goodsShipments[0].specificationNumber': '1',
        'goodsShipments[0].specificationListNumber': '1',
        'goodsShipments[0].mainContractTerms.tradeCountryCode': 'AM',
        'goodsShipments[0].mainContractTerms.totalInvoiceAmount': '1',
        'goodsShipments[0].mainContractTerms.contractCurrencyCode': 'ARS'
    }

    @staticmethod
    def pay_via_external_cusad_limit():
        driver = Utils.driver
        driver.get('https://uatapp3.fipsoft.com/cusad/?lang=ru')
        driver.get('https://uatapp3.fipsoft.com/cusad/sad/create?customsProcedure=IM&iff=I')
        Utils.fill_form(External.payViaExternalCUSADLIMITFormData)
        driver.find_element_by_partial_link_text('Стороны').click()
        Utils.driver.find_element_by_id('goodsShipments[0].consignor.organizationName').send_keys('апр')
        Utils.driver.find_element_by_id('goodsShipments[0].consignor.address.countryCode').send_keys('SD')
        Utils.driver.find_element_by_id('goodsShipments[0].consignee.raOrganizationFeatures.unn').send_keys('17031994')
        Utils.driver.find_element_by_id('goodsShipments[0].finRespPerson.raOrganizationFeatures.unn').send_keys(
            '17031994')
        Utils.driver.find_element_by_id('goodsShipments[0].declarant.raOrganizationFeatures.unn').send_keys('17031994')
        driver.execute_script("window.scrollTo( 0, 0 );")
        driver.find_element_by_partial_link_text('Перевозка').click()
        time.sleep(1)
        Utils.check_select('goodsShipments[0].consigment.containerIndicator', 2)
        Utils.driver.find_element_by_id(
            'goodsShipments[0].consigment.departureArrivalTransport.transportModeCode').send_keys('20')
        Utils.driver.find_element_by_id('goodsShipments[0].consigment.borderTransport.transportModeCode').send_keys(
            '20')
        Utils.driver.find_element_by_id('goodsShipments[0].goodsLocation[0].informationTypeCode').send_keys('21')
        Utils.driver.find_element_by_id('goodsShipments[0].goodsLocation[0].customsOfficeCode').send_keys('05100010')
        Utils.driver.find_element_by_id(
            'goodsShipments[0].goodsLocation[0].goodsLocationPlace.numberCustomsZoneCode').send_keys('05100010')
        driver.execute_script("window.scrollTo( 0, 0 );")
        driver.find_element_by_partial_link_text('Товары').click()
        time.sleep(1)
        driver.find_element_by_class_name('addItemBtn').click()
        Utils.driver.find_element_by_id('goodsTNVEDCode').send_keys('12051090000')
        Utils.driver.find_element_by_id('originCountryCode').send_keys('AE')
        Utils.driver.find_element_by_id('grossWeightQuantity').send_keys('1')
        Utils.driver.find_element_by_id('netWeightQuantity').send_keys('1')
        Utils.driver.find_element_by_id('netWeightQuantity2').send_keys('1')
        Utils.driver.find_element_by_id('customsProcedure.precedingCustomsModeCode').send_keys('00')
        Utils.driver.find_element_by_id('customsProcedure.goodsTransferFeatureCode').send_keys('000')
        Utils.driver.find_element_by_id('supplemGoodsQuantity.goodsQuantity').send_keys('1')
        Utils.driver.find_element_by_id('invoicedCost').send_keys('1')
        Utils.driver.find_element_by_id('customsCostCorrectMethodCode').send_keys('0')
        Utils.check_select('goodsPackaging.pakageTypeCode', 1)
        Utils.driver.find_element_by_id('goodsDsc').send_keys('вапва')
        Utils.driver.find_element_by_id('goodsDscRu').send_keys('вапва')
        Utils.driver.find_element_by_id('saveItem').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Документы').click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#fakePresentedDocuments .addIterativeRecord")
        driver.execute_script("arguments[0].click();", element)
        Utils.driver.find_element_by_id('fakePresentedDocuments[0].presentedDocumentModeCode').send_keys('460')
        Utils.driver.find_element_by_id('fakePresentedDocuments[0].providingIndicationMark').send_keys('0')
        Utils.driver.find_element_by_id('fakePresentedDocuments[0].prDocumentNumber').send_keys('123')
        Utils.set_date('fakePresentedDocuments[0].prDocumentDate', '17/01/2015')
        Utils.driver.find_element_by_id('fakePresentedDocuments[0].goodsNumbers').send_keys('1')
        element = driver.find_element_by_css_selector("#fakePresentedDocuments .addIterativeRecord")
        driver.execute_script("arguments[0].click();", element)
        Utils.driver.find_element_by_id('fakePresentedDocuments[1].presentedDocumentModeCode').send_keys('01999')
        Utils.driver.find_element_by_id('fakePresentedDocuments[1].providingIndicationMark').send_keys('0')
        Utils.driver.find_element_by_id('fakePresentedDocuments[1].prDocumentNumber').send_keys('123')
        Utils.set_date('fakePresentedDocuments[1].prDocumentDate', '17/01/2015')
        Utils.driver.find_element_by_id('fakePresentedDocuments[1].goodsNumbers').send_keys('1')
        Utils.driver.find_element_by_id('operationStore').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        element = driver.find_element_by_css_selector("#searchRes .glyphicon-pencil")
        driver.execute_script("arguments[0].click();", element)
        time.sleep(1)
        driver.switch_to.window(driver.window_handles[9])
        Utils.driver.find_element_by_id('operationSubmitStored').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        driver.get(
            'https://uatapp3.fipsoft.com/cusad/sad/search?status=&code=&id=&regNumberDoc=&filledPersonUnn=&iff=&consignorUnn=&consigneeUnn=&declarantUnn=&electronicDocumentSign=&customsProcedure=&customsModeCode=&op_executionDate=&Search=%D0%9F%D0%BE%D0%B8%D1%81%D0%BA')
        element = driver.find_element_by_css_selector("#searchRes .glyphicon-pencil")
        driver.execute_script("arguments[0].click();", element)
        driver.switch_to.window(driver.window_handles[10])
        Utils.driver.find_element_by_id('operationRegisterSubmitted').click()
        element = driver.find_element_by_css_selector(".jconfirm-buttons .btn-success")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_partial_link_text('Платежи').click()
        driver.find_element_by_class_name('glyphicon-print').click()
        time.sleep(1)
        driver.find_element_by_partial_link_text('Оплата').click()
        driver.switch_to.window(driver.window_handles[11])  # tab browers
        driver.find_element_by_class_name('glyphicon-eye-open').click()
        driver.find_element_by_class_name('cancel').click()
        driver.find_element_by_class_name('serviceLink').click()
        driver.find_element_by_class_name('glyphicon-print').click()
        driver.find_element_by_class_name('glyphicon-time').click()
        driver.find_element_by_class_name('operationLink').click()
        driver.find_element_by_class_name('cancel').click()
        driver.find_element_by_class_name('serviceLink').click()
        driver.find_element_by_class_name('glyphicon-pencil').click()
        driver.find_element_by_class_name('operationPayFromOverpaymentClass').click()
        Utils.driver.find_element_by_id('overPayments[11].amountToUse').send_keys('999999999999')
        driver.find_element_by_css_selector("div#formContainer #verify").click()
        time.sleep(1)
        Utils.driver.find_element_by_id('operationPayFromOverpayment').click()
        time.sleep(1)
        driver.find_element_by_css_selector("div.jconfirm-buttons .dialogue-yes").click()
        time.sleep(1)
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-eye-open")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('btn').click()
        driver.find_element_by_class_name('serviceLink').click()
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-print")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector("#paymentsTable .glyphicon-time")
        driver.execute_script("arguments[0].click();", element)
        element = driver.find_element_by_css_selector("#paymentsTable .operationLink")
        driver.execute_script("arguments[0].click();", element)
        driver.find_element_by_class_name('btn').click()






























































