# Installation
- `conda create --name [ENV_NAME] python=3.11.0`
- `conda activate [ENV_NAME]`
- `pip install -r .\requirements.txt`

# How to run experiments
1. Create victim circuits using `create_victim_circuits.ipynb`. This will create new victim circuits and save them to a pickle file in `./pickles/victim_circs`.
2. Create circuits with attacker using `create_full_circ.ipynb`. This will create new full circuits and save them to a pickle file in `./pickles/full_circs`.
3. You can now compile and run them on IBM's quantum computers using `run_experiment.ipynb`. Here you can configure the backend and the qubit layout. Make sure that your layout choice is compatible with the backend.

# Note
## VS Code
Make the following change in the Jupyter extension:
Set the root directory for running notebooks and the Interactive window. - ${workspaceFolder}
