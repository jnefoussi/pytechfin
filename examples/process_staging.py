from pytechfin.context import Context

context = Context(use_production_context=True, carol_tenant='tenant70827589d8a611eabbf10a586460272f')

stagings = [
         "se1_invoice","se1_installments", "se1_payments","se1_payments_abatimentos",
         "se2_invoice","se2_installments", "se2_payments","se2_payments_abatimentos"            
]

context.carol.caroltechfin.process_staging(stagings)
