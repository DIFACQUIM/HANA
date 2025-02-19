import rdkit
from rdkit import Chem, DataStructs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

SMARTS_1 = pd.read_csv("https://raw.githubusercontent.com/DIFACQUIM/HANA/refs/heads/main/SMARTS_list.csv")
SMARTS_2 = pd.read_csv("https://raw.githubusercontent.com/DIFACQUIM/HANA/refs/heads/main/SMARTS_list2.csv")
SMARTS_list1 = list(SMARTS_1["SMARTS"])
SMARTS_list2 = list(SMARTS_2["SMARTS"])

def hana (mol,bits): #HANA 
  bits_list = [] # List of bits

  # Bits
  if bits==200:
    SMARTS_list = SMARTS_list1
    
  elif bits==1000:
    SMARTS_list = SMARTS_list2
    
  for i in SMARTS_list:
    if mol.HasSubstructMatch(Chem.MolFromSmarts(i)):
      bits_list.append(1)
    else:
      bits_list.append(0)
      
  fp = DataStructs.ExplicitBitVect(bits)
  for i, bit in enumerate(bits_list):
    if bit == 1:
      fp.SetBit(i)  # Set the bits based on the original fingerprint values
  return fp

print("> Thank you so much for use Hana. Have a nice day!")
