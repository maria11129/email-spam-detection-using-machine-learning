# Spam Detector CLI

Welcome to the **Spam Detector CLI**! This command-line tool helps you determine if an email is spam or not.

## Project Structure

* **data manipulation/** : Data manipulation and visualization notebooks
* **model/** : Trained model notebook

#### 1. Clone the repository:

```bash
git clone https://github.com/maria11129/email-spam-detection-using-machine-learning
```

#### 2.Install Python dependencies:

```
`pip install -r requiremenets.txt`

```

## Usage

#### Run the CLI with the email content:

```
`cd Command_line_interface
 spamdetector -e "Your email content here" cd Command_line_interface spamdetector -e "Your email content here" `

```

### Example output:

![image alt](https://github.com/maria11129/email-spam-detection-using-machine-learning/blob/76fd0def0a4d7251f149092696b04706f3cede3e/images/CLI-output.png)

#### **Data Visualization**

To better understand the dataset, I visualized the key aspects of the data, such as class distribution and common words in spam and ham emails.

1. **Class Distribution**
   The dataset was imbalanced, with significantly more "Ham" emails than "Spam." This imbalance can bias the model toward predicting "Ham." To address this, I applied SMOTE (Synthetic Minority Oversampling Technique) to balance the dataset.
   > The graph above shows the proportion of "Ham" and "Spam" emails before applying SMOTE.
   >

---

2. **Word Frequency Analysis**
   I created a word cloud to visualize the most frequent words in spam and ham emails. This helped identify distinct patterns in text, such as spam emails containing words like "Congratulations," "Free," and "Prize."

   * **Spam Word Cloud**
   * **Ham Word Cloud**

   > These visualizations provided insight into the dataset's text patterns and guided the feature engineering process.
   >

---

3. **TF-IDF Distribution**
   I plotted the TF-IDF scores of spam and ham emails to understand their separation in the feature space. This helped validate that TF-IDF was effectively transforming the data.
   > This plot helped confirm that spam and ham emails have distinguishable TF-IDF patterns, aiding classification.
   >

---
![image alt](https://github.com/maria11129/email-spam-detection-using-machine-learning/blob/d5451f13f10be4ac910fe153d4c83d334d76ace3/images/big-one.png)
