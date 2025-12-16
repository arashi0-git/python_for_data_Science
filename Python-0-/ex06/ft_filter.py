def ft_filter(function, iterable):
    """Recode filter"""
    return (x for x in iterable if function(x))
