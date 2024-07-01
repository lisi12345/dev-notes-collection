Use conda environment

to run 
%matplotlib widget
from pyvista import set_plot_theme
set_plot_theme('document')
pv.set_jupyter_backend('pythreejs')


<!-- run in teminal, not Python interactive cell -->
pip install ipympl
conda install nodejs
pip install --upgrade jupyterlab
pip install pythreejs
jupyter lab build 

if above failed and error said something like "", then try to execute below:
<!-- https://stackoverflow.com/questions/62849352/conda-not-recognizing-that-i-have-node-installed/ -->
conda install -c conda-forge/label/gcc7 nodejs
jupyter lab build 