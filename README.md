Requirements:
Python 3.6
Numpy
Scipy
Sklearn


I have submitted paper to ESWA journal and is under review.

# iwmh
To perform 1-NN classification for ICWS and PCWS methods,
1. Run knn_set.py
2. to change dataset, change the value of indd variable in knn_set.py according to the indices of the datasets in the comment of knn_set.py

To perform 1-NN classification for IWMH and WMH methods,
1. Run knn_vec.py
2. to change dataset, change the value of indd variable in knn_vec.py according to the indices of the datasets in the comment of knn_vec.py

Results will be stored in knn.txt.

Same process can be repeated for Top-K retrieval task with topk_set.py and topk_vec.py
Results will be stored in map.txt, preci.txt, and topk.txt (for runtime)
