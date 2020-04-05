# Collaborative-Learning-Simulator

A python library to simulate Collaborative Deep Learning. It provides the flexibility to simulate various network architectures, Collaborative Learning Stratergies, and privacy invasion attacks. Currently built for Pytorch, this library is a work in progress.

## Pre-requisites
It is recommended to install the simulator in a virtual environment, and install the dependencies in this environment. In a Linux system, this can be done using terminal as follows:
```bash
python3 -m pip install --user virtualenv
python3 -m venv my_env
source my_env/bin/activate
pip install -r requirements.txt
```

## Example Implementations
The repository contains two example implementation. 
### Federated Averaging:
Implemented in the "federated_averaging.ipynb" file, this simulates a two part setting where we train an image based gender classifier.
### Reference Script:
Implemented in the "reference_training_script.ipynb" file, this demonstrates training a gender classifer on a single system.

## License

MIT
