from pytechfin.context import Context
from pycarol import CarolHandler

context = Context(use_production_context=True, carol_tenant='tenantf6ea21aa445511eb950a0a58646001ad')

print(context.carol.staging)

context.carol.add_module('carolandler', CarolHandler)

print(context.carol._all_modules)