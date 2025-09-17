# new_drug_uptake
This is a Data Science Innovation Accelerator 2025 project looking to model the uptake of new medicines in ScoMed (Scottish Combined Medicines Dataset, PHS).

## Folder structure

- denodo contains examples of connecting to the scomed denodo database (by Gatz Osorio)
- scripts contain python scripts to extract and work on scomed data

### Setting up the environment

The project sets up a python environment named .venv and loads required packages from requirements.txt.
It then uses setconfigs.py to set up a connection to the PostgreSQL (Denodo) database, pulling config information from config.ini. A file called exampleconfig.ini is provided in git.


