
# AI Grader

## Project Overview
AI Grader is a project designed to helping students study a specific topic via repetition. Using questions from an API, students can respond to relevant questions and receive real time grading by ChatGPT.

## Problem we are Solving
We are helping students study on *blank* topic by giving them many questions focused around *blank*.

## Project Interface
AI Grader interfaces with:
- **Students** who use the application.
- **API data** for our questions.
- **ChatGPT** for evaluating answers and providing grades.

## Inputs and Outputs

### Inputs
- **Username**
- **Password (maybe)**
- **User answers/guesses**

### Outputs
- **ChatGPT's answers**
- **ChatGPT's grade**

## Workflow (Input to Output)
1. **User signs in**
2. **User is asked a question**
3. **Send user input to ChatGPT**
4. **ChatGPT analyzes the answer and gives a grade**
5. **Update the user's grade**

## Risks
- **ChatGPT hallucination**: ChatGPT might generate incorrect or misleading answers or grades.
- **User attempts SQL injection**: Malicious Users

## Success Metrics
We determine our success via:
- The database updates correctly with user grades.
- Outputs (answers and grades) are displayed accurately to the user.

## Created by Matthew & Brice
