# Genetic Algorithm-Guided Machine Learning for Accelerated Screening and Experimental Validation of Plasma-Assisted Ni-Fe-Based OER Electrocatalysts

> **Note:** This is the repository for the paper *Genetic Algorithm-Guided Machine Learning for Accelerated Screening and Experimental Validation of Plasma-Assisted Ni-Fe-Based OER Electrocatalysts*. 
>
> 🚀 **The source code, processed datasets, and pre-trained models will be made publicly available upon the formal acceptance of the manuscript.**

---

## 📖 Abstract

Nickel-iron-based catalysts show great promise for the oxygen evolution reaction (OER). Specifically, plasma-assisted and electrodeposition methods are compatible with large-scale industrial fabrication. However, the vast compositional space remains largely unexplored due to the inefficiency of traditional trial-and-error discovery. 

In this work, we develop a **machine learning-guided genetic algorithm (ML-GA) paradigm** with two complementary modes: **exploration and exploitation**. The exploration mode balances population diversity and predicted performance to broadly search the chemical space, while the exploitation mode focuses on high-performance regions to identify promising catalysts. 

Guided by this framework, **NiFe/NiS catalysts were synthesized via plasma-assisted electrodeposition** and demonstrated remarkable OER activity, achieving low overpotentials of **218 mV** and **315 mV** at current densities of **10** and **1000 mA cm⁻²**, respectively. This work provides a demonstration of the effectiveness of the ML-GA approach in overcoming data limitations and accelerating the design of high-performance OER electrocatalysts.

---

## ✨ Key Highlights

This framework is designed to navigate the **high-dimensional parameter space** of plasma-assisted synthesis, which is traditionally difficult to optimize due to the complex coupling of physical (plasma) and chemical (deposition) parameters.

### 1. Dual-Mode Genetic Algorithm (Exploration & Exploitation)
Unlike traditional optimization algorithms that easily get trapped in local optima, our GA operates in two distinct modes:
- **🔍 Exploration Mode:** Prioritizes population diversity to navigate broad, unexplored chemical spaces, mitigating the bias from uneven data distribution.
- **🎯 Exploitation Mode:** Focuses on refining candidates in high-potential regions to pinpoint the global optimum.

### 2. Transferable to Plasma-Assisted Synthesis
The framework supports flexible input descriptors, making it readily transferable to complex synthesis methods.
- **Descriptors:** Compatible with compositional ratios (Ni/Fe) and synthesis parameters (Plasma Power, Gas Pressure, Deposition Time).
- **Application:** Successfully applied to optimize **Plasma-Assisted Electrodeposition** processes.

### 3. Rigorous Experimental Validation
The predicted materials were not just theoretical. We synthesized the optimal **NiFe/NiS** catalyst, validating the algorithm's practical utility for industrial-scale applications.

---

## 🛠️ Framework Overview

The proposed workflow integrates data-driven ML models with evolutionary strategies to close the loop between prediction and experimental validation.

![Framework Workflow](assets/workflow.png)
*(Placeholder: Add your framework flowchart here, e.g., Figure 1 from your paper)*

### Workflow Stages:
1. **Data Preprocessing & Augmentation:** - Handling uneven data distributions from published OER datasets.
   - Normalization of synthesis descriptors.
2. **Surrogate Model Training:** - Training regression models (e.g., RF, XGBoost) to map synthesis parameters to Overpotential ($\eta$).
3. **GA-Driven Evolution:** - **Initialization**: Generating random virtual catalysts.
   - **Selection & Crossover**: Evolving generations based on fitness functions derived from the ML predictor.
   - **Mutation**: Introducing stochastic variations to escape local minima.

---

## 📊 Results & Validation

Guided by the ML-GA framework, we identified the optimal synthesis parameters for NiFe-based catalysts.

| Catalyst | Synthesis Method | $\eta_{10}$ (mV) | $\eta_{1000}$ (mV) |
| :--- | :--- | :---: | :---: |
| **Optimized NiFe/NiS** | **Plasma-Assisted Electrodeposition** | **218** | **315** |
| Baseline NiFe | Conventional Electrodeposition | >250 | >350 |

![Experimental Results](assets/results.png)
*(Placeholder: Add your key experimental result figures here, e.g., LSV curves or structure characterization)*

---

## 📅 Roadmap to Release

We are committed to open science. The following assets will be released:

- [ ] **Source Code**: Complete Python implementation of the Dual-Mode GA and ML training scripts.
- [ ] **Datasets**: The cleaned and preprocessed OER dataset used for model training.
- [ ] **Pre-trained Models**: Serialized models ready for inference.
- [ ] **Tutorials**: Jupyter notebooks demonstrating how to use the framework for new catalyst discovery.

---

## 🔗 Citation

If you find this work helpful, please consider citing our paper (BibTeX entry will be updated upon publication):

```bibtex
@article{YourName2026_ML_GA_OER,
  title={Genetic Algorithm-Guided Machine Learning for Accelerated Screening and Experimental Validation of Plasma-Assisted Ni-Fe-Based OER Electrocatalysts},
  author={Your Name and Co-authors},
  journal={Plasma Science and Technology (Under Review)},
  year={2026}
}
