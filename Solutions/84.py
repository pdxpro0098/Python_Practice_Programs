import zlib
data = b'compress me'
compressed = zlib.compress(data)
print("Compressed:", compressed)
decompressed = zlib.decompress(compressed)
print("Decompressed:", decompressed)
