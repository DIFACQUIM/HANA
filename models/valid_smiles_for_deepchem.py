"""
"""

from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.Scaffolds import MurckoScaffold
import numpy as np

def valid_smiles_for_deepchem(smiles_list):
    cleaned_smiles = []
    invalid_smiles = []

    for smi in smiles_list:
        try:
            mol = Chem.MolFromSmiles(smi, sanitize=False)
            if mol is None:
                invalid_smiles.append(smi)
                cleaned_smiles.append(smi)
                continue

            # sanitize without stereo
            mol.UpdatePropertyCache(strict=False)
            Chem.FastFindRings(mol)
            Chem.SetAromaticity(mol)

            # Cleaning stereo in double bonds 
            for bond in mol.GetBonds():
                bond.SetBondDir(Chem.BondDir.NONE)
                if bond.GetStereo() == Chem.BondStereo.STEREOANY:
                    bond.SetStereo(Chem.BondStereo.STEREONONE)

            # Reassign Stereo from Geometry
            Chem.AssignStereochemistry(mol, cleanIt=True, force=True)

            # Review scaffold 
            try:
                MurckoScaffold.MurckoScaffoldSmiles(
                    mol=mol, includeChirality=False
                )
            except RuntimeError:
                # Final opion: delete stereoquemestry in doble bonds
                for bond in mol.GetBonds():
                    if bond.GetBondTypeAsDouble() == 2.0:
                        bond.SetStereo(Chem.BondStereo.STEREONONE)
                        bond.SetBondDir(Chem.BondDir.NONE)
                Chem.AssignStereochemistry(mol, cleanIt=True, force=True)

            # SMILES with chirality
            smi_clean = Chem.MolToSmiles(
                mol,
                isomericSmiles=True,  # Retain @, @@, /, \ --> For avoid error in DeepChem
                canonical=True
            )
            cleaned_smiles.append(smi_clean)

        except Exception as e:
            print(f"⚠️ SMILES problemático: {smi} → {e}")
            invalid_smiles.append(smi)
            cleaned_smiles.append(smi)

    print(f"\nTotal procesados  : {len(cleaned_smiles)}")
    print(f"Total problemáticos: {len(invalid_smiles)}")

    return np.array(cleaned_smiles)
