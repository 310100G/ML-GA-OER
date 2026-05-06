# Machine Learning-Guided Genetic Algorithm for Accelerated Screening of Ni-Fe-Based OER Electrocatalysts with Plasma-Assisted Synthesis

Code and data for the paper: **"Machine Learning-Guided Genetic Algorithm for Accelerated Screening of Ni-Fe-Based OER Electrocatalysts with Plasma-Assisted Synthesis"**.

## 📂 Repository Structure

```text
ML-GA-OER/
│
├── data/                    # Shared or general datasets
│
├── round1/                  # Initial screening phase (Exploration Mode)
│   ├── data_cleaning/       # Scripts and data for feature engineering and preprocessing
│   ├── exp_data/            # Raw and processed experimental datasets for round 1
│   ├── ga/                  # Genetic algorithm scripts for generating initial candidates
│   └── model_training/      # Machine learning regression models training for round 1
│
├── round2/                  # Active learning phase (Exploitation Mode)
│   ├── data_cleaning/       # Scripts and data for feature engineering and preprocessing
│   ├── exp_data/            # Experimental datasets containing validated candidates for round 2
│   ├── ga/                  # Genetic algorithm scripts focusing on high-performance regions
│   └── model_training/      # Refined machine learning models training for round 2
│
├── environment.yml          # Anaconda environment configuration (Recommended)
├── requirements.txt         # Pip dependencies and package versions
├── LICENSE                  # Open-source license (MIT)
└── README.md                # Project documentation
```

## ⚙️ Installation & Dependencies

To ensure reproducibility, we recommend setting up a virtual environment. Install the required dependencies using the provided `requirements.txt` file:

```bash
# Clone the repository
git clone [https://github.com/310100G/ML-GA-OER.git](https://github.com/310100G/ML-GA-OER.git)
cd ML-GA-OER

# Create and activate the Anaconda environment
conda env create -f environment.yml
conda activate your_env_name

# If you are using standard Python, you can install the core dependencies
# Install required packages
pip install -r requirements.txt
