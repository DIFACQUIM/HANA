import pandas as pd
from rdkit import Chem
from molvs.standardize import Standardizer
from molvs.charge import Uncharger, Reionizer
from molvs.fragment import LargestFragmentChooser
from molvs.tautomer import TautomerCanonicalizer

# Define functions
STD = Standardizer() # Get the standardized version of a given SMILES string (canonical SMILES).
LFC = LargestFragmentChooser() # Select the largest fragment from a salt (ionic compound).
UC = Uncharger() # Charge corrections are applied to ensure, for example, that free metals are correctly ionized.
RI = Reionizer() # Neutralize molecule by adding/removing hydrogens.
TC = TautomerCanonicalizer()  # Return a tautomer “reasonable” from a chemist’s point, but it isn’t guaranteed to be the most energetically favourable.

def fix_stereo_any(mol):
    """
    Cleaning an ambiguous double bond or STEREOANY.
    RDKit can not canonicalize ambiguous double bonds: RuntimeError in Canon.cpp
    """
    for bond in mol.GetBonds():
        if bond.GetBondTypeAsDouble() == 2.0:  # Double bond.
            if bond.GetStereo() == Chem.rdchem.BondStereo.STEREOANY:
                # Reset STEREONONE so that Canon.cpp does not fail.
                bond.SetStereo(Chem.rdchem.BondStereo.STEREONONE)
    return mol

def MasterStandarization(smi):
    try:
      # 1. Read SMILES
        mol = Chem.MolFromSmiles(smi,sanitize=True)
        if mol == None:
            #If rdkit could not parse the smiles, it returns "Error 1".
            return "Error 1"
        else:
            # 2. Standardizer and fragment chooser
            mol = STD(mol)
            mol = LFC(mol)

            # 3. Generate valid valences
            try:
              Chem.SanitizeMol(mol)
            except:
              return "Error 2" #If molecule contains invalid valences, return "Error 2".

            # 4. Retain allowed elements
            allowed_elements = {"H","B","C","N","O","F","Si","P","S","Cl","Se","Br","I"}
            actual_elements = set([atom.GetSymbol() for atom in mol.GetAtoms()])
            if len(actual_elements-allowed_elements) == 0:

              # 5. Uncharge and remove isotopes
              mol = UC(mol)
              mol = RI(mol)

              # 6. Assign Sterochemistry from geometry
              Chem.AssignStereochemistry(mol, cleanIt=True, force=True)
              mol = fix_stereo_any(mol)
            
              # 7. Canonical tautomer
              mol = TC(mol)

              # 8. SMILES validation
              smi_cleaned = Chem.MolToSmiles(
                  mol,
                  isomericSmiles=True,  # Retain @, @@, /, \ --> For avoid errors in DeepChem.
                  canonical=True        
                  ) 
              
              if Chem.MolFromSmiles(smi_cleaned) is None:
                # If invalid SMILES persist, return "Error 4".
                return "Error 4"
            else:
              return "Error 3" # If molecule contains other than the allowed elements, return "Error 3".
            
            return smi_cleaned

    except:
        return "Something else was found"
