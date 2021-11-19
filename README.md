# plant_soil_borne_fungal_diseases
The open-source Python-based toolkit is depending on the Python environment (Python Version 3.7).

#### **conda environment**
    conda list
    conda env list
    conda create -n py3.7 python=3.7
    conda activate py3.7

### **Install packages**
    numpy
    pandas
    sklearn
    matplotlib
    seaborn
    scikit-bio
    statsmodels
    tensorflow

### **Feature selection** 
**The format of input files refer to the folder "./Features/disease"**
    
    python feature_selection.py -i (your file) -k 102(your feature number) -o ./training_results (output file)

### **Model testing** 
**The format of test_data files refer to the folder "./test_data"**

    python generate_models_acc.py training_results  60 --e test_data (your test data set)

### **References** 

    (1) Yansu Wang et al. Multiple feature ranking strategies for predicting plant soil-borne fungal disease occurrence from soil microbiome data
    (2) Reiman, Derek, et al. "Meta-Signer: Metagenomic Signature Identifier based on Rank Aggregation of Features." bioRxiv (2020).
