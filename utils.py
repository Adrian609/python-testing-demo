def strtobool(val):
    true_vals = ['yes', 'y', '', '1']
    false_vals = ['no', 'n', '0']
    try:
        val = val.lower().strip()
    except AttributeError:
        val = str(val).lower()
    if val in true_vals:
        return True
    elif val in false_vals:
        return False
    else:
        raise ValueError('Invalid input value: %s' % val)
