import nbformat

nb = nbformat.read('object_detection.ipynb', as_version=4)

# Remove any markdown cells containing “Release Notes”
nb.cells = [
    cell for cell in nb.cells
    if not (cell.cell_type == 'markdown'
            and 'Release Notes' in ''.join(cell.source))
]

# Clear outputs and Colab metadata on every cell
for cell in nb.cells:
    cell.outputs = []
    cell.metadata.pop('colab', None)
    cell.metadata.pop('execution', None)

nbformat.write(nb, 'object_detection.ipynb')
