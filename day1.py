def prep_input():
    """read in & format txt file of depth info"""
    with open('input.txt') as f:
        input = f.read()

    # convert to int
    return [int(i) for i in input.split()]


def count_increases(depth_readout):
    """count # of times depth increases relative to previous measurement"""
    increase_count = 0
    for count, measurement in enumerate(depth_readout):
        if count != 0 and depth_readout[count - 1] < measurement:
            increase_count += 1
    return increase_count


def get_sliding_avg():
    """create sliding average"""
    depth_readout = prep_input()
    sliding_avg = []
    for count, measurement in enumerate(depth_readout):
        if count < len(depth_readout) - 2:
            sliding_avg.append(measurement + depth_readout[count + 1]
                               + depth_readout[count + 2])
    return sliding_avg


print(count_increases(prep_input()))
print(count_increases(get_sliding_avg()))
