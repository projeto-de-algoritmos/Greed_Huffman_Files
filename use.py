from huffman import HuffmanCoding
import sys

path = "exemplo.txt"

h = HuffmanCoding(path)

output_path = h.compress()
print("Arquivo Compactado: " + output_path)

decom_path = h.decompress(output_path)
print("Arquivo Descompactado: " + decom_path)