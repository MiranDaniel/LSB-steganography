def get_bit_plane(channel):
    bit_planes = [channel & (1 << i) for i in range(8)]
    return bit_planes
