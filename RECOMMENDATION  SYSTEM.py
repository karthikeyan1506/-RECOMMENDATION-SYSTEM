# ===================================
# RECOMMENDATION SYSTEM (COLAB)
# User-based Collaborative Filtering with KNN
# Dataset: MovieLens 100K
# ===================================

# Step 0 - Install library
!pip install -q scikit-surprise

# Step 1 - Imports
import pandas as pd
from surprise import Dataset, Reader, KNNBasic, accuracy
from surprise.model_selection import train_test_split
from collections import defaultdict

# Step 2 - Load built-in MovieLens dataset
data = Dataset.load_builtin('ml-100k')

# Step 3 - Train/test split
trainset, testset = train_test_split(data, test_size=0.2, random_state=42)

# Step 4 - Define similarity options (User-based collaborative filtering)
sim_options = {
    "name": "cosine",   # similarity metric: cosine, msd, pearson
    "user_based": True  # True for user-user similarity, False for item-item
}

# Build model
algo = KNNBasic(sim_options=sim_options)
algo.fit(trainset)

# Step 5 - Evaluate model
predictions = algo.test(testset)
rmse = accuracy.rmse(predictions, verbose=False)
mae = accuracy.mae(predictions, verbose=False)
print(f"Test RMSE: {rmse:.4f}, MAE: {mae:.4f}")

# Step 6 - Top-N recommendations
def get_top_n(predictions, n=10):
    top_n = defaultdict(list)
    for uid, iid, true_r, est, _ in predictions:
        top_n[uid].append((iid, est))
    for uid, user_ratings in top_n.items():
        user_ratings.sort(key=lambda x: x[1], reverse=True)
        top_n[uid] = user_ratings[:n]
    return top_n

top_n = get_top_n(predictions, n=5)

# Display top-5 recommendations for first 5 users
for uid, recs in list(top_n.items())[:5]:
    print(f"\nUser {uid} recommended items:")
    for iid, rating in recs:
        print(f"  Item {iid}, predicted rating {rating:.2f}")

# ===================================
# How to use your own CSV:
# df = pd.read_csv("your_ratings.csv")
# reader = Reader(rating_scale=(1, 5))
# data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)
# ===================================
