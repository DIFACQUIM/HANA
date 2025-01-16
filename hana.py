import rdkit
print(f"rdkit_version: {rdkit.__version__}")

import pandas as pd
import numpy as np
from rdkit import Chem
import matplotlib.pyplot as plt

SMARTS_1 = pd.read_csv("https://raw.githubusercontent.com/DIFACQUIM/HANA/refs/heads/main/SMARTS_list.csv")
SMARTS_2 = pd.read_csv("https://raw.githubusercontent.com/DIFACQUIM/HANA/refs/heads/main/SMARTS_list2.csv")
SMARTS_list1 = list(SMARTS_1["SMARTS"])
SMARTS_list2 = list(SMARTS_2["SMARTS"])

def hana (smi, bits): #HANA molecular fingerprint
  bits_list = [] # List of bits

  mol = Chem.MolFromSmiles(smi)

  # Bits
  if bits =1000
  for i in SMARTS_list2:
    if mol.HasSubstructMatch(Chem.MolFromSmarts(i)):
      bits_list.append(1)
    else:
      bits_list.append(0)
      
  else:
  for i in SMARTS_list1:
    if mol.HasSubstructMatch(Chem.MolFromSmarts(i)):
      bits_list.append(1)
    else:
      bits_list.append(0)

  return bits_list
