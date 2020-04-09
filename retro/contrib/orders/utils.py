def adminfield(short_description=None, allow_tags=False, boolean=False, admin_order_field=None):
    """
    This decorator set arguments passed to it as atributes of function wich decorate.
    This is for faster making of fields in django administration with fancy attributes
    """
    def decorator(func):
        if short_description is not None:
            func.short_description = short_description
        if admin_order_field is not None:
            func.admin_order_field = admin_order_field
        func.allow_tags = allow_tags
        func.boolean = boolean
        return func
    return decorator