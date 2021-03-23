from pytechfin import Techfin, TOTVSRacAuth, TechfinDataModel


tf = Techfin()
dm = TechfinDataModel(tf)


r = dm.get_pks(dm_name='apinvoiceaccounting', carol_tenant='tenant0e9b44667b6211eb9ba10a58646140cf',
               page_size=5000,)

print(r)