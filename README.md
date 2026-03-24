"# Medicine_Reviews" 
 "========================================================================"

 #  Medicine Recommendation System (NLP Based)

##  Project Overview

This project is a Natural Language Processing (NLP) based recommendation system that suggests medicines based on user reviews and conditions.

The system analyzes the text reviews provided by users and recommends the most relevant medicines using TF-IDF vectorization and cosine similarity.

---

##  Objective

1. To recommend medicines based on user reviews
2. To help users find suitable medicines for specific conditions
3. To apply NLP techniques in a real-world problem

---

##  How It Works

1. User provides a review or condition
2. Text is cleaned and preprocessed
3. TF-IDF vectorization is applied
4. Cosine similarity is calculated
5. Top similar reviews are found
6. Medicines associated with those reviews are recommended

---

##  Project Structure

```
MLPROJECT_MEDICINE_REVIEW/
│
├── artifacts/
├── notebooks/
│   ├── EDA_PROCESS.ipynb
│   ├── model_training.ipynb
│
├── src/
│   └── medicine_review/
│       ├── components/
│       │   ├── data_ingestion.py
│       │   ├── data_transformation.py
│       │   ├── model_trainer.py
│       │
│       ├── pipeline/
│       │   ├── training_pipeline.py
│       │   ├── prediction_pipeline.py
│       │
│       ├── utils.py
│       ├── logger.py
│       ├── exception.py
│
├── app.py
├── requirements.txt
├── setup.py
├── README.md
```

---

## Technologies Used

* Python 
* Pandas & NumPy
* Scikit-learn
* NLP (TF-IDF)
* Cosine Similarity
* 

---

## 🔄 Pipeline Flow

```
Data → Cleaning → TF-IDF → Similarity → Recommendation
```


##  Dataset

* Dataset: Medicine Reviews Dataset
* Features:

  * `drugName`
  * `condition`
  * `review`
  * `rating`
  * `date`
  * `usefulCount`

---

## Installation & Setup

###  Clone the repository

```
git clone https://github.com/PankajMishra99/Medicine_Reviews.git
cd Medicine_Reviews
```

###  Create virtual environment

```
conda create -p venv python=3.12 -y
conda activate venv/
```

### Install dependencies

```
pip install -r requirements.txt
```

---

## Run the Project

### Run training pipeline

```
python src/medicine_review/model_trainer.py
```

### Run application

```
python app.py
```

---

##  Features

* NLP-based recommendation system
* Content-based filtering
* Logging and exception handling
* Scalable architecture

---

## Future Improvements

* Use Word2Vec / BERT embeddings
* Add user-based recommendation
* Deploy on cloud (AWS/GCP)
* Add UI improvements

---

##  Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

---

##  Contact

For any queries, feel free to reach out.

---


