# SIFT_FV_imagenet
The final project for the Applied Machine Learning (COMP 551) course at McGill University, under the supervision of Sarath Chandar.

# Scripts
  ## Downloading Data
    1) /ImageNet_Downloads/sysnets.txt: contains the references for all the classes to be downloaded
    2) /ImageNet_Downloads/DataDownload.py: downloads class by class based on the sysnets provided in the text file; runs parallel to the representation learning algorithm. 
  
  ## Representation Learning
    1) /scripts/representationLearning_SIFT_FV.m: extracts the SIFT descriptors from the images and encodes them into fisher vectors
    2) /others/RepresentationLearning_Histograms.m: a less accurate attempt using the histogram method
    3) /others/RepresentationLearning_VLAD.m: a less accurate attempt using Vector of Locally Aggregated Descriptors (VLAD)
 
  ## Classifiers
    1) /scripts/train_fisher.py: training various different classifiers on the fisher vectors
    2) /scripts/LogisticRegressionTraining.py: hyperparameter tuning on Logistic Regression 
    3) /scripts/SGDTraining.py: hyperparameter tuning on classifier using SGD
    
  ## Others
    1) /scripts/splitter_manual.py: splits the full dataset into training, validation and testing data
    2) /others/splitter.py: first draft of the script to split the data
    3) /others/countlines.py: counts the number of lines in the huge csv files
    4) /others/prepare10Classes.py: extracting only 10 classes
    5) /others/train_fisher_10classes.py: training various different classifiers on the fisher vectors of the 10 classes
