# Flight Delay Prediction and Hub Airport Analysis

This project looks at flight delays in the 2015 U.S. flight dataset and follows the CRISP-DM process from start to finish.

There are two main questions in the project:

- Q1: can a flight be predicted to be delayed by more than 15 minutes using information known before departure?
- Q2: do hub airports seem to show stronger delay patterns than non-hub airports?

## Project Structure

- `data/`
  Contains raw and processed datasets (not commited to the repo).

- `notebooks/`
  Contains the CRISP-DM phase notebooks and the separate Q2 analysis notebook.

- `src/`
  Contains reusable Python code for loading data, preparing it, merging tables, and handling simple model save/load steps.

- `models/`
  Used for saved model files from the deployment stage.


## Main Notebooks

- `Phase_1_Business_Understanding.ipynb`
  Defines the project goals, scope, and plan.

- `Phase_2_Data_Understanding.ipynb`
  Loads the data, checks its quality, and explores early patterns.

- `Phase_3_Data_Preparation.ipynb`
  Cleans the data, creates the target variable, and prepares the modelling dataset.

- `Phase_4_Modeling.ipynb`
  Trains and compares the classification models for Q1.

- `Phase_5_Evaluation.ipynb`
  Reviews how well the selected model answers the business question.

- `Phase_6_Deployment.ipynb`
  Shows a simple deployment example using a saved model pipeline.

- `Q2_Hub_Airport_Delays.ipynb`
  Looks at the hub airport question separately using grouped comparisons and scraped airport hub data.

## Data Used

The main dataset is the 2015 Kaggle Flight Delays and Cancellations dataset.

For Q2, a small extra airport table was scraped from Wikipedia and merged into the analysis so hub airports could be identified using an external source.

## Model Summary

For Q1, the final selected model was Logistic Regression. It was not perfect, but it gave the most useful overall result for the project out of the models tested.

The target used for Q1 is:

- `DELAY_15 = 1` if departure delay is more than 15 minutes
- `DELAY_15 = 0` otherwise

## Running the Project

The notebooks were written to be run in order for Q1:

1. Phase 1
2. Phase 2
3. Phase 3
4. Phase 4
5. Phase 5
6. Phase 6

Q2 is in its own notebook and can be run separately after the main project notebooks.

If you are running the notebooks yourself, make sure:

- the raw dataset files are in `data/raw/`
- the processed dataset has been created before running the later notebooks (saved in `data/processed/`)
- A python environment containing all the required libraries is used