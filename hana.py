import rdkit
print(f"rdkit_version: {rdkit.__version__}")

import pandas as pd
import numpy as np
from rdkit import Chem
import matplotlib.pyplot as plt

SMARTS_df = pd.read_csv("https://raw.githubusercontent.com/DIFACQUIM/HANA/refs/heads/main/SMARTS_list.csv")
print(SMARTS_df.tail(2))

SMARTS_list = list(SMARTS_df["SMARTS"])
print(SMARTS_list[:2])

def HANA (smi): #HANA molecular fingerprint
  bits_list = [] # List of bits

  mol = Chem.MolFromSmiles(smi)

  # Bits
  for i in SMARTS_list:
    if mol.HasSubstructMatch(Chem.MolFromSmarts(i)):
      bits_list.append(1)
    else:
      bits_list.append(0)

  return bits_list