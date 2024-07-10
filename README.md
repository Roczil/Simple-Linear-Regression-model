# Project: Linear Regression using TensorFlow

## Project Description
- **Project Topic**: Linear Regression using TensorFlow.
- **Project Goal**: Train a linear regression model.
- **Project Features**: Data generation, model training, result visualization.
- **Technologies Used**: TensorFlow, Matplotlib, NumPy.

## Project Setup Instructions

1. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

2. Run the main script:
    ```sh
    python main.py
    ```

## Requirements Analysis

- **Functional Requirements**:
    - Generate training data.
    - Train a linear regression model.
    - Visualize the results.

- **Non-functional Requirements**:
    - Code divided into modules.
    - Error and exception handling.
    - Unit tests.

## Implementation

- **Data Structure**: TensorFlow Variable, TensorFlow Tensor, NumPy.
- **Class and Attributes**: Class `Model` with attributes `weight` and `bias`.
- **Modules**: Code divided into `main.py`, `model.py`, `utils.py`.
- **Errors and Exceptions**: Error handling in `main.py`.
- **Generators and List Comprehensions**: Used in `generate_data`.
- **Standard Library**: Matplotlib used for result visualization.
- **AI Framework**: TensorFlow used for model training.

## Testing

### Unit Test Implementation

Unit tests have been implemented in the `test_model.py` file using the `unittest` framework.

### Test Results
Ran 2 tests in 0.237s

OK

## Possible Improvements
### At this stage, no errors were detected in the tested functionality. The code works as expected. Future improvements may include:

- **Extending unit tests with additional test scenarios.**
- **Optimizing the model training process.**
- **Basing the AI model on real data.**

### Conclusions
The project was implemented as planned. A linear regression model was successfully implemented, tested, and visualized. Future work can focus on extending functionality and optimizing the code.

