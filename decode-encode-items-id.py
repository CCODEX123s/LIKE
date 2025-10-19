def EncryptItems(value):
    result = []
    while value > 0:
        byte = value & 0x7F
        value >>= 7
        if value > 0:
            byte |= 0x80
        result.append(byte)
    return bytes(result).hex()
def DecryptItems(hex_value):
    bytes_value = bytes.fromhex(hex_value)
    r, _ = 0, 0
    for byte in bytes_value:
        r |= (byte & 0x7F) << _
        if not (byte & 0x80):
            break
        _ += 7
    return r
encoded_value = EncryptItems(909000012)
print("Encoded value (hex):", encoded_value)
#decoded_value = DecryptItems(encoded_value)
#print("Decoded value:", decoded_value)