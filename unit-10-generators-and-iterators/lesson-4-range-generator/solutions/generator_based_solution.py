def rmotr_range(start, end, step=1):
    current = start
    while current < end:
        num = current
        current += step
        yield num
