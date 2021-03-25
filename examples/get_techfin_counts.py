from pytechfin import Techfin, TOTVSRacAuth, TechfinDataModel


tf = Techfin()
dm = TechfinDataModel(tf)


r = dm.get_table_record_count( carol_tenant='tenant0e9b44667b6211eb9ba10a58646140cf',)

print(r)