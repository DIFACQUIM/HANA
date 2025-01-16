# HANA

**Requirements** 

1. Dowloand Anaconda navigator.
https://www.anaconda.com/download

2. Create a virtual ambient with conda and rdkit.
        
        conda create -c conda-forge -n my-rdkit-env rdkit
   
3. Install Jupyter notebook. Open anaconda navigator with:

        anaconda-navigator
   
   In Anaconda navigator change <base(root)> to <my-rdkit-env>. Then, install Jupyter notebook.
   Close Anaconda navigator and return to terminal.
        
4. Activate virtual ambient.

        conda activate my-rdkit-env

5. Install git module

        pip install gitpython
6. Clone repository

       git clone https://github.com/DIFACQUIM/HANA.git
   
8. See examples_files.py
