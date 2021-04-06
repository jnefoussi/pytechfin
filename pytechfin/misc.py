import re

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


def get_tenant_techfin(carol_tenant, techfin_tenant):
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

def is_guid(techfin_tenant):
    """Validate guid arg

    Args:
        tenant (str): techfin tenant id

    Returns:
        bool: true if is valid guid value
    """
    c = re.compile('[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}', re.I)
    res = c.match(techfin_tenant)
    return res
     

def get_tenant_name(techfin_tenant):
    """Returns carol tenant name.

    Args:
        techfin_tenant (str): techfin tenant id
    Raises:
        ValueError: Raises error if techfin_tenant is not a valid guid value

    Returns:
        str: carol tenant name
    """
    if techfin_tenant is None:
        raise ValueError('Either `carol_tenant` or `techfin_tenant` must be set.')
    
    techfin_tenant = techfin_tenant.strip()
    if(is_guid(techfin_tenant)):
        return f"tenant{techfin_tenant.replace('-','')}"
    else: 
        raise ValueError(' `techfin_tenant` must be a valid guid value')
