from pytechfin.context import CarolContext

context = CarolContext(use_production_context=True, carol_tenant='tenantf6ea21aa445511eb950a0a58646001ad')


print(context.staging)

from pycarol import Carolina

context.add_module('carolina', Carolina)

print(context._all_modules)