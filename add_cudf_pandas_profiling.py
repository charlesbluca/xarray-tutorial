# after modifying the notebooks execute all with 
# jupyter nbconvert --execute --inplace $(find . -type f -name "*.ipynb" -printf '%P\n' | tr '\n' ' ')

import os
import nbformat

# Function to add a line to the beginning of each code cell
def add_cudf_pandas_profiling(notebook_path):
    with open(notebook_path, "r") as f:
        notebook = nbformat.read(f, as_version=4)

    for cell in notebook.cells:
        if cell.cell_type == "code":
            cell.source = "%%cudf.pandas.profile\n\n" + cell.source

    notebook.cells.insert(0, nbformat.v4.new_code_cell("%load_ext cudf.pandas"))

    with open(notebook_path, "w") as f:
        nbformat.write(notebook, f)

directory = '/home/nfs/charlesb/git/xarray-contrib/xarray-tutorial'

for root, dirs, files in os.walk(directory):
    for file in files:
        if file.endswith(".ipynb"):
            notebook_path = os.path.join(root, file)
            add_cudf_pandas_profiling(notebook_path)
