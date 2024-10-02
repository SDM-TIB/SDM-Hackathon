# LDM-QA

This project presents LDM-QA, a question answering system over the federation of the LDM and ORKG KGs. The input question is translated into a SPARQL query that uses the predicates from the LDM and ORKG KGs.

# How to execute LDM-QA

python LLM_Call.py prompt.txt "QUESTION"

where QUESTION is a natural language expression representing a question against the federation of the LDM and ORKG KGs. 

# Examples of questions and their corresponding generated SPARQL queries

QUESTION 1: "What are the resources that include word "metadata" in the description of the resource?"

QUESTION 2: "What is the  frequency of the datasets per data formats?"

QUESTION 3: "What is the frequency of the datasets per organizations?"

QUESTION 4: "What are the resources that include word "metadata" in the description of the resource?"

QUESTION 5: "What are  title, year, and research field label of the papers that describe a dataset?"

QUESTION 6: "What is the title of the datasets that are described by papers, also provide  title, year, and research field label of these papers?"

