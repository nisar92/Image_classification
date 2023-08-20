echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.11"
conda create --prefix ./env python=3.11 -y
echo [$(date)]: "activate env"
source activate ./env
echo [$(date)]: "END"
