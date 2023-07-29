def get_bit_plane(channel):
    bit_planes = [channel & (1 << i) for i in range(8)]
    return bit_planes


def access_bit(data, num):
    base = int(num // 8)
    shift = int(num % 8)
    return (data[base] >> shift) & 0x1
