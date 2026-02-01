# Krish's Approach
import zlib
data = b'compress me'
compressed = zlib.compress(data)
print("Compressed:", compressed)
decompressed = zlib.decompress(compressed)
print("Decompressed:", decompressed)

# Dalip's Approach
import zlib;

data = b"abbccceedd3a"

compressed_data = zlib.compress(data)
print(f"Original Data size: {len(data)}")
print(f"Compressed Data size: {len(compressed_data)}")
print(f"Compressed Data: {compressed_data}")

decompressed_data = zlib.decompress(compressed_data)
print(f"Decompressed Data: {decompressed_data}")
