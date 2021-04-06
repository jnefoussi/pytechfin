from pytechfin.context import Context

context = Context(use_production_context=True, carol_tenant='tenant70827589d8a611eabbf10a586460272f')
print(f"Current Carol Tenant: {context.current['carol']['env_name']}")
print(f"Current Techfin Tenant: {context.current['techfin']['tenant_id']}")