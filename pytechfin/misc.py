
def get_guid(tenant):
    """Generate UUID from carol's tenant name

    Args:
        tenant (str): carol tenant name

    Returns:
        str: techfin tenant id
    """
    tenant = tenant[6:]
    uuid_tenant = tenant[:8] + '-' + tenant[8:12] + '-' + tenant[12:16] + '-' + tenant[16:20] + '-' + tenant[20:]
    return uuid_tenant


def get_tenant_id(carol_tenant, techfin_tenant):
    """Returns techfin tenant id.

    Args:
        carol_tenant (str): catol tenant name
        techfin_tenant (str): techfin tenant id

    Raises:
        ValueError: Raises error if both parameters are empty

    Returns:
        str: techfin tenant id
    """

    if carol_tenant is None:

        if techfin_tenant is None:
            raise ValueError('Either `carol_tenant` or `techfin_tenant` must be set.')
        
        return techfin_tenant
    else:
        return get_guid(carol_tenant)
