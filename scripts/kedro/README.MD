# Kedro

## setup
brew install --cask anaconda
export PATH=/usr/local/anaconda3/bin:"$PATH"
conda list

conda create --name kedro-environment python=3.7 -y
conda activate kedro-environment
conda install -c conda-forge kedro
kedro info


## Deactivate
```conda deactivate```

## Notes
- Environment needs to be activated to run script
