import rdkit
from rdkit import Chem, DataStructs
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

SMARTS_df = pd.read_csv("https://raw.githubusercontent.com/DIFACQUIM/HANA/refs/heads/main/SMARTS/HANA_1363.csv")
SMARTS_list = list(SMARTS_df["SMARTS"])

def hana (mol,bits): #HANA 
  bits_list = [] # List of bits

  # Bits
  SMARTS_bits = SMARTS_list[:bits]
    
  for i in SMARTS_bits:
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
