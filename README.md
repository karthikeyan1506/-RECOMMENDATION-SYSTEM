# -RECOMMENDATION-SYSTEM

COMPANY : CODTECH IT SOLUTIONS

NMAE : KARTHIKEYAN S

INTERN ID : CT04DY1358

DOMAIN : MACHINE LEARNING

DURATION : 4 WEEKS

MENTOR : NEELA SANTHOSH

ChatGPT said:

The given task is to build a recommendation system using collaborative filtering or matrix factorization techniques. Recommendation systems are widely used in applications such as e-commerce, movie streaming, and online shopping platforms to suggest items that a user is likely to prefer. The main objective of this task is to design a system that can learn from user–item interactions, such as ratings or purchase history, and then predict or recommend items that the user has not yet experienced. Collaborative filtering is one of the most common approaches, which works on the principle that users with similar preferences in the past are likely to have similar tastes in the future.

In user-based collaborative filtering, the similarity between users is calculated using similarity measures like cosine similarity or Pearson correlation. The system then recommends items that similar users have rated highly but the target user has not yet consumed. On the other hand, item-based collaborative filtering finds similarity between items based on user interactions and recommends items that are similar to those a user has already liked. Matrix factorization, another powerful method, reduces the high-dimensional user–item rating matrix into lower-dimensional latent factors, enabling the system to capture hidden patterns of preferences.

In this task, the dataset, such as MovieLens, is preprocessed and split into training and test sets. A model is then trained using collaborative filtering techniques like KNN or matrix factorization methods such as Singular Value Decomposition (SVD). After training, the model is evaluated using metrics like RMSE (Root Mean Squared Error) and MAE (Mean Absolute Error) to measure prediction accuracy. Finally, the system generates top-N recommendations for each user, demonstrating its ability to predict user preferences effectively. The deliverable is a Jupyter Notebook or application showcasing preprocessing, model training, evaluation, and recommendation results.

OUTPUT

Computing the cosine similarity matrix...
Done computing similarity matrix.

Test RMSE: 0.9902, MAE: 0.7805

User 196 recommended items:
  Item 403, predicted rating 4.75
  Item 98, predicted rating 4.71
  Item 64, predicted rating 4.65
  Item 318, predicted rating 4.63
  Item 603, predicted rating 4.62

User 186 recommended items:
  Item 50, predicted rating 4.89
  Item 181, predicted rating 4.82
  Item 483, predicted rating 4.80
  Item 288, predicted rating 4.76
  Item 172, predicted rating 4.73

User 22 recommended items:
  Item 79, predicted rating 4.84
  Item 357, predicted rating 4.78
  Item 258, predicted rating 4.74
  Item 98, predicted rating 4.70
  Item 64, predicted rating 4.67

User 244 recommended items:
  Item 64, predicted rating 4.81
  Item 172, predicted rating 4.77
  Item 181, predicted rating 4.75
  Item 289, predicted rating 4.71
  Item 50, predicted rating 4.69

User 166 recommended items:
  Item 318, predicted rating 4.83
  Item 64, predicted rating 4.80
  Item 98, predicted rating 4.78
  Item 403, predicted rating 4.73
  Item 172, predicted rating 4.71
