import pandas as pd
from lightfm import LightFM
from lightfm.data import Dataset
import pickle
import sys
import os

def load_processed_data(path):
    "Load processed data CSV produced by recommendation-preprocessing."
    return pd.read_csv(path)

def train_model(
    df: pd.DataFrame,
    n_factors: int = 2,
    regularization: float = 0.02,
    random_state: int = 42,
    epochs: int = 30,
    num_threads: int = 2,
) -> tuple[LightFM, Dataset]:
    """Train a LightFM matrix factorization model.

    Parameters
    ----------
    df : pandas.DataFrame
        DataFrame containing at least ``user_id`` and ``item_id`` columns.
    n_factors : int, optional
        Number of latent factors for the model.
    regularization : float, optional
        L2 regularisation strength for both users and items.
    random_state : int, optional
        Random seed for reproducibility.
    epochs : int, optional
        Number of training epochs.
    num_threads : int, optional
        Number of parallel threads to use.

    Returns
    -------
    model : LightFM
        The trained LightFM model.
    dataset : Dataset
        LightFM ``Dataset`` used for ID mapping.
    """
    # Ensure that IDs are strings – LightFM expects hashable IDs.
    df = df.copy()
    df["user_id"] = df["user_id"].astype(str)
    df["item_id"] = df["item_id"].astype(str)

    # Initialise the LightFM Dataset and register all users and items.
    dataset = Dataset()
    dataset.fit(users=df["user_id"].unique(), items=df["item_id"].unique())

    # Build the interaction matrix from the DataFrame.
    interactions, _ = dataset.build_interactions(
        [(row.user_id, row.item_id) for row in df.itertuples()]
    )

    # Create and train the LightFM model.
    model = LightFM(
        no_components=n_factors,
        item_alpha=regularization,
        user_alpha=regularization,
        random_state=random_state,
    )
    model.fit(interactions, epochs=epochs, num_threads=num_threads)

    return model, dataset

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python train.py path/to/processed.csv")
        sys.exit(1)
    df = load_processed_data(sys.argv[1])
    model, dataset = train_model(df)
    # Save model
    model_path = "lightfm_model.pkl"
    with open(model_path, "wb") as f:
        pickle.dump(model, f)
    print(f"Model saved to {model_path}")