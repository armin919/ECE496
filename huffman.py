################Huffman Coding############

import heapq #necessary for priority queue

freq = [
            (8.167, 'a'), (1.492, 'b'), (2.782, 'c'), (4.253, 'd'),
            (12.702, 'e'),(2.228, 'f'), (2.015, 'g'), (6.094, 'h'),
            (6.966, 'i'), (0.153, 'j'), (0.747, 'k'), (4.025, 'l'),
            (2.406, 'm'), (6.749, 'n'), (7.507, 'o'), (1.929, 'p'), 
            (0.095, 'q'), (5.987, 'r'), (6.327, 's'), (9.056, 't'), 
            (2.758, 'u'), (1.037, 'v'), (2.365, 'w'), (0.150, 'x'),
            (1.974, 'y'), (0.074, 'z')]


encode_table = {'z': '001011000', 'o': '1101', 'j': '001011011', 'd': '11111', 'u': '01000', 'r': '0101', 'p': '110001', 'h': '0110', 'x': '001011010', 'b': '110000', 'g': '110011', 'k': '0010111', 'f': '00100', 's': '0111', 'a': '1110', 'w': '00110', 'l': '11110', 'c': '01001', 'q': '001011001', 'm': '00111', 'e': '100', 'v': '001010', 't': '000', 'n': '1010', 'i': '1011', 'y': '110010'}

decode_table = {'001011010': 'x', '001010': 'v', '00111': 'm', '000': 't', '01001': 'c', '11111': 'd', '1010': 'n', '0010111': 'k', '110000': 'b', '1011': 'i', '001011000': 'z', '110011': 'g', '0111': 's', '0101': 'r', '00100': 'f', '0110': 'h', '1110': 'a', '001011011': 'j', '00110': 'w', '11110': 'l', '110010': 'y', '1101': 'o', '001011001': 'q', '01000': 'u', '100': 'e', '110001': 'p'}



class Node(object):
    def __init__(self, left = None, right = None,root=None): 
        self.left = left #Left Child
        self.right = right #Right Child
        

#Frequency table generator, input a text file, output a list with probability of each char
def freqTableGenerator(text):
    charFreqDic = {}
    total = 0
    with open(text,encoding='utf8') as textFile: #reading utf8 encoding
        for line in textFile:  
            for char in line: 
                if char not in charFreqDic:
                    charFreqDic[char] = 1
                    total += 1
                else:
                    charFreqDic[char] += 1
                    total += 1
                
    for char in charFreqDic:
        probability = charFreqDic[char]/total
        freqTable.append((probability,char))

                
           
    
#freqTableGenerator("holmes.txt")

#Responsible for creating huffman tree
def createHuffmanTree(frequency_table):
        
    while len(frequency_table) > 1:
        
        heapq.heapify(frequency_table) #heapfies freq table at the place
        left = frequency_table.pop(0)
        heapq.heapify(frequency_table)
        #print(freq)
        
        right = frequency_table.pop(0) #getting the two smallest values
        
        node = Node(left,right) #make a node 
        frequency_table.append((left[0]+right[0],node)) #adding up the values of each node
       
    return 
    


    
createHuffmanTree(freq)
  
#Walking Huffman tree and construct coding scheme recursively
def huffmanTreeWalk(node, prefix="", code={}):
    if isinstance(node[1].left[1], Node):  #Is the node->left another node?
        huffmanTreeWalk(node[1].left,prefix+"0", code) #Yes, continue to go down
    else:
        code[node[1].left[1]]=prefix+"0" #No, assign (node[1].left[1]) which is a char to the code
    if isinstance(node[1].right[1],Node):
        huffmanTreeWalk(node[1].right,prefix+"1", code)
    else:
        code[node[1].right[1]]=prefix+"1"
    return(code)

#For making a hashtable for decoding bits into characters
def huffmanDecodeDict(encodeTable):
    
    return {v: k for k, v in encodeTable.items()} #reversing Hashtable value and keys

#Encoder input a string as a text,output bit sequence
def Encoder(text):
    encoded = str()
    for char in text:
        encoded += encode_table[char]
    return encoded

#Decoder bitseq in int output string 
def Decoder(bitSeq):
    bitChunk = str()
    text = str()
    bit = 0
    while bit < len(bitSeq):
        bitChunk += bitSeq[bit]
        if bitChunk in decode_table:
            text += decode_table[bitChunk]
            bit += 1
            bitChunk = "" #Resetting the bitchunk to get ready for next Char
        else:
            bit+=1
    return text
        
        
        
    

code1 = huffmanTreeWalk(freq[0],prefix="",code={})
decodeDict  = huffmanDecodeDict(code1)
print(code1)
print(decodeDict)
encoded = Encoder("weareelectricalengineerfromuniversityoftoronto")
print(encoded)
print(Decoder('0011010011100101100100111101000100100001011011010011110111101001010110011101110101001000101001000101110100111010001010101100101010001010111101100011001011010010000011010101110110100001101'))
