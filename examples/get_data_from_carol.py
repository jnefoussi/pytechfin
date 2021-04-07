from pytechfin.context import Context

context = Context(use_production_context=True, carol_tenant='tenant70827589d8a611eabbf10a586460272f')

# Get data from staging
df = context.carol.caroltechfin.get_staging_data('se1')
print(df)

# Get data from realtime
rt = context.carol.caroltechfin.get_realtime_data('arinvoice')
print(rt)