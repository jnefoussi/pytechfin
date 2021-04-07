from enum import Enum

class EnumApps(Enum):
    """Techfin Apps Enumerator
    """
    FMSCASH = 'fmscash'
    CASHFLOW = 'cashflow'
    RAC = 'totvs.rac'

    @classmethod
    def exists_key(cls, item): 
        return item in cls.__members__

    @classmethod
    def exists_value(cls, item): 
        return item in set([f.value for f in cls])

#TODO: Add table information
class DataModelInfo():
    """ Carol & Techfin DataModel Informations
    """
    apinvoiceaccounting           = {'name':'apinvoiceaccounting','techfin_key':'invoiceaccounting_id' , 'subscribed_app': ['cashflow'], 'techfin_table' : '' }
    apinvoice                     = {'name':'apinvoice','techfin_key':'invoice_id' , 'subscribed_app': ['cashflow'], 'techfin_table' : '' }
    apinvoiceinstallment          = {'name':'apinvoiceinstallment', 'techfin_key':'invoiceinstallment_id', 'subscribed_app': ['cashflow'], 'techfin_table' : '' }
    apinvoicepayments             = {'name':'apinvoicepayments','techfin_key':'invoicepayments_id' , 'subscribed_app': ['cashflow'], 'techfin_table' : '' }
    arinvoiceaccounting           = {'name':'arinvoiceaccounting','techfin_key':'invoiceaccounting_id' , 'subscribed_app': ['cashflow'], 'techfin_table' : '' }
    arinvoicebra                  = {'name':'arinvoicebra', 'techfin_key':'invoicebra_id', 'subscribed_app': ['fmscash'], 'techfin_table' : '' }
    arinvoice                     = {'name':'arinvoice','techfin_key':'invoice_id' , 'subscribed_app': ['fmscash', 'cashflow'], 'techfin_table' : '' }
    arinvoiceinstallment          = {'name':'arinvoiceinstallment', 'techfin_key':'invoiceinstallment_id', 'subscribed_app': ['fmscash', 'cashflow'], 'techfin_table' : '' }
    arinvoiceorigin               = {'name':'arinvoiceorigin','techfin_key':'_id','subscribed_app': ['fmscash'], 'techfin_table' : '' }
    arinvoicepartner              = {'name':'arinvoicepartner', 'techfin_key':'invoicepartner_id', 'subscribed_app': ['fmscash'], 'techfin_table' : '' }
    arinvoicepayments             = {'name':'arinvoicepayments','techfin_key':'invoicepayments_id' , 'subscribed_app': ['fmscash', 'cashflow'], 'techfin_table' : '' }
    arpaymentstype                = {'name':'arpaymentstype', 'techfin_key':'transactiontype_id' ,'subscribed_app': ['fmscash', 'cashflow'], 'techfin_table' : '' }
    cfbankbalance                 = {'name':'cfbankbalance','techfin_key':'_id','subscribed_app': ['cashflow'], 'techfin_table' : '' }
    company                       = {'name':'company','techfin_key':'uuid' , 'subscribed_app': ['cashflow'], 'techfin_table' : '' }
    fndbankaccount                = {'name':'fndbankaccount', 'techfin_key':'bankaccount_id' ,'subscribed_app': ['fmscash', 'cashflow'], 'techfin_table' : '' }
    mdaccount                     = {'name':'mdaccount','techfin_key':'account_id' , 'subscribed_app': ['cashflow'], 'techfin_table' : '' }
    mdbankaccount                 = {'name':'mdbankaccount','techfin_key':'bank_id','subscribed_app': ['fmscash', 'cashflow'], 'techfin_table' : '' }
    mdbusinesspartnerdocreference = {'name':'mdbusinesspartnerdocreference','techfin_key':'_id','subscribed_app': ['fmscash', 'cashflow'], 'techfin_table' : '' }
    mdbusinesspartner             = {'name':'mdbusinesspartner','techfin_key':'businesspartner_id' , 'subscribed_app': ['fmscash', 'cashflow'], 'techfin_table' : '' }
    mdbusinesspartnergroup        = {'name':'mdbusinesspartnergroup', 'techfin_key':'businesspartnergroup_id', 'subscribed_app': ['fmscash', 'cashflow'], 'techfin_table' : '' }
    mdcostcenter                  = {'name':'mdcostcenter', 'techfin_key':'costcenter_id', 'subscribed_app': ['cashflow'], 'techfin_table' : '' }
    mdcurrency                    = {'name':'mdcurrency', 'techfin_key':'currency_id', 'subscribed_app': ['fmscash', 'cashflow'], 'techfin_table' : '' }
    mddocreference                = {'name':'mddocreference', 'techfin_key':'docreference_id', 'subscribed_app': ['fmscash', 'cashflow'], 'techfin_table' : '' }
    mdfinancialcategory           = {'name':'mdfinancialcategory','techfin_key':'financialcategoryid','subscribed_app': ['cashflow'], 'techfin_table' : '' }
    organization                  = {'name':'organization', 'techfin_key':'uuid' ,'subscribed_app': ['fmscash', 'cashflow'], 'techfin_table' : '' }

 