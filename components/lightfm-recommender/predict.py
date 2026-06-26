"""Inference script for LightFM model.

Usage:
    python predict.py --data processed.csv --model lightfm_model.pkl \
        --user <user_id> [--top_n N]

The script loads the trained LightFM model from a pickle file, rebuilds the
LightFM ``Dataset`` based on the processed CSV used during training, and predicts
the scores for all items for the specified user. The top N items (default 5)
are printed.
"""

import argparse
import sys
import pickle
import numpy as np
import pandas as pd
from lightfm import LightFM
from lightfm.data import Dataset


def load_model(model_path: str) -> LightFM:
    """Load a LightFM model from a pickle file.

    Parameters
    ----------
    model_path: str
        Path to the pickled LightFM model.
    Returns
    -------
    LightFM
        The deserialized model instance.
    """
    with open(model_path, "rb") as f:
        return pickle.load(f)


def build_dataset(df: pd.DataFrame) -> Dataset:
    """Create a LightFM ``Dataset`` and fit it with user and item IDs.

    LightFM expects string identifiers to be hashable. The function copies the
    DataFrame, coerces the identifier columns to ``str`` and then fits a new
    ``Dataset`` instance. The resulting ``Dataset`` is used only for its internal
    ID mappings – we do not need the interaction matrix for inference.
    """
    df = df.copy()
    df["user_id"] = df["user_id"].astype(str)
    df["item_id"] = df["item_id"].astype(str)

    dataset = Dataset()
    dataset.fit(users=df["user_id"].unique(), items=df["item_id"].unique())
    return dataset


def get_top_n_items(
    model: LightFM,
    dataset: Dataset,
    user_id: str,
    top_n: int = 5,
) -> list[tuple[str, float]]:
    """Return the top‑N items for a given user.

    Parameters
    ----------
    model: LightFM
        Trained LightFM model.
    dataset: Dataset
        LightFM ``Dataset`` containing the ID mappings.
    user_id: str
        Raw user identifier (as it appears in the original CSV).
    top_n: int, optional
        Number of highest‑scoring items to return.

    Returns
    -------
    list[tuple[str, float]]
        List of ``(item_id, score)`` pairs sorted by descending score.
    """
    user_mapping, _, item_mapping, _ = dataset.mapping()
    if user_id not in user_mapping:
        raise ValueError(f"User id {user_id!r} not found in the dataset.")
    user_index = user_mapping[user_id]

    # All item indices as a NumPy array.
    item_indices = np.array(list(item_mapping.values()))
    # Repeat the user index for each item.
    user_indices = np.full_like(item_indices, user_index)

    # Predict scores for (user, item) pairs.
    scores = model.predict(user_indices, item_indices)

    # Get indices of the highest scores.
    top_idx = np.argsort(-scores)[:top_n]
    # Reverse lookup from internal index to raw item id.
    rev_item_mapping = {v: k for k, v in item_mapping.items()}
    top_items = [
        (rev_item_mapping[int(item_indices[i])], float(scores[i])) for i in top_idx
    ]
    return top_items


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(
        description="Run inference with a trained LightFM model."
    )
    parser.add_argument(
        "--data",
        required=True,
        help="Path to the processed CSV used during training.",
    )
    parser.add_argument(
        "--model",
        default="lightfm_model.pkl",
        help="Path to the pickled LightFM model (default: lightfm_model.pkl).",
    )
    parser.add_argument(
        "--user",
        required=True,
        help="Raw user ID for which to generate recommendations.",
    )
    parser.add_argument(
        "--top_n",
        type=int,
        default=5,
        help="Number of top items to display (default: 5).",
    )
    args = parser.parse_args(argv)

    # Load processed data and the trained model.
    df = pd.read_csv(args.data)
    model = load_model(args.model)

    # Recreate the dataset mappings used during training.
    dataset = build_dataset(df)

    try:
        top_items = get_top_n_items(
            model, dataset, user_id=str(args.user), top_n=args.top_n
        )
    except ValueError as exc:
        print(exc, file=sys.stderr)
        sys.exit(1)

    print(f"Top {args.top_n} recommendations for user {args.user}:")
    for rank, (item_id, score) in enumerate(top_items, start=1):
        print(f"{rank}. Item {item_id} – score {score:.4f}")


if __name__ == "__main__":
    main()
