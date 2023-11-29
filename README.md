# Tpot_ec_prediction
EC number prediction models created using the TPOT tool. 
These models were done for the Master Dissertation "A Study of Machine Learning for Artificial Intelligence-Based Enzyme Classification.", of the Computational Biology and Bioinformatics Master from Lisbon's Nova University, at NOVA ITQB.
For using the models, you need to have Python and Anaconda and follow the next steps if you are on a terminal:
1. Clone the repository
```
git clone https://github.com/Ananas-bio/Tpot_ec_prediction.git
```
2. Create and activate a conda environment using the YAML file
```
conda env create -f environment.yml
conda activate tpot_ec
```

To run the models in the terminal window here is an example:
```
python ec_predict -i uniprot_test.fasta -l 3 -m c40
```

The -l and -m are optional, with the default of -l being 3 (as in prediction up to level 3) and -m the c40 model (can be c40 or swiss).
