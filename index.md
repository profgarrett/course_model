# Data Modeling in Python Course Notes


Books:

- [Data8](https://inferentialthinking.com/chapters/intro.html)
- [Whirlwind Tour of Python](https://jakevdp.github.io/WhirlwindTourOfPython/)
- [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)

- [How to think like a data scientist](how-to-think-like-a-data-scientist)
Link: https://www.data8.org/sp25/#week-3

(Visualizations)[https://www.data8.org/sp25/resources/]

Grading
- https://otter-grader.readthedocs.io/en/latest/tutorial.html
- [sample exams](https://www.data8.org/sp25/resources/)

## Schedule

### Week 1 (Aug 18, 2025)

*Introduction to ACT 426/BUDA 451*

- Outcomes
	- Understand the data modeling / prediction process
	- Install Python and run some code
- Syllabus
- Student/Faculty Introductions
- Install [Anaconda](https://www.anaconda.com/download/success)
- Install [Visual Studio Code](https://code.visualstudio.com/)
	- Use Anaconda interpreter (ctrl+shift+p, Python: Select Interpreter)
- [Read: A Visual Guide to Machine Learning](http://www.r2d3.us/visual-intro-to-machine-learning-part-1/)
	- Define terms:
		- Feature, split point, recursion, and overfitting
		- Scatterplot, decision tree, histogram
		- Accuracy
		- Training and test data
	
*Data8 Chapter 1: What is Data Science?*

- Outcomes
	- Define data science 
		- Exploration: identify patterns with vis + descriptive statistics
		- Prediction: guess about the future with ml + optimization
		- Inference: Quantify uncertainty with statistical tests + models
	- Get a brief introduction to Python language features
- Pre-class reading
	 - [d8: Intro](data8-textbook/chapters/intro.md)
	   [d8: 01. What Is Data Science](data8-textbook/chapters/01/what-is-data-science.md)
	 - [d8: 01.1. Intro](data8-textbook/chapters/01/1/intro.md)
	 - [d8: 01.1.2. Statistical Techniques](data8-textbook/chapters/01/1/2/statistical-techniques.md)
	   [d8: 01.2. Why Data Science](data8-textbook/chapters/01/2/why-data-science.md)
- Pre-class quiz in eCampus
- Class activities
	- [ml01](ml01/index.md): Introduction to Modeling


### Week 2 (Aug 25, 2025) 

*Data8 Chapter 2: Causality and Experiments*

- Outcomes
	- Define causality, observational studies, treatment, outcomes
	- Define treatment group and control group
	- Define a randomized control trial (RCT), placebo
- Reading
	- [02. Causality And Experiments](data8-textbook/chapters/02/causality-and-experiments.md)
	- [02.1. Observation And Visualization John Snow And The Broad Street Pump](data8-textbook/chapters/02/1/observation-and-visualization-john-snow-and-the-broad-street-pump.md)
	- [02.2. Snow S Grand Experiment](data8-textbook/chapters/02/2/snow-s-grand-experiment.md)
	- [02.3. Establishing Causality](data8-textbook/chapters/02/3/establishing-causality.md)
	- [02.4. Randomization](data8-textbook/chapters/02/4/randomization.md)
	- [02.5. Endnote](data8-textbook/chapters/02/5/endnote.md)
- Pre-class quiz in eCampus
- Class activities
	- Use these terms to discuss improving teaching at WVU. 

*Data8 Chapter 3: Programming in Python*

- Reading
	- [03. Programming In Python](data8-textbook/chapters/03/programming-in-python.md)
	- 03.1. Expressions ([download notebook](data8-textbook/chapters/03/1/Expressions.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/03/1/Expressions.ipynb))
	- 03.2.1. Growth ([download notebook](data8-textbook/chapters/03/2/1/Growth.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/03/2/1/Growth.ipynb))
	- 03.2. Names ([download notebook](data8-textbook/chapters/03/2/Names.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/03/2/Names.ipynb))
	- 03.3. Calling a function ([download notebook](data8-textbook/chapters/03/3/Calls.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/03/3/Calls.ipynb))
 - Pre-class quiz in eCampus
 - Class activities
	  - None, see c4

*Data8 Chapter 4: Python Data Types*

- Reading
	- 04. Data Types ([download notebook](data8-textbook/chapters/04/Data_Types.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/04/Data_Types.ipynb))
	- 04.1. Numbers ([download notebook](data8-textbook/chapters/04/1/Numbers.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/04/1/Numbers.ipynb))
	- 04.2.1. String Methods ([download notebook](data8-textbook/chapters/04/2/1/String_Methods.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/04/2/1/String_Methods.ipynb))
	- 04.2. Strings ([download notebook](data8-textbook/chapters/04/2/Strings.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/04/2/Strings.ipynb))
	- 04.3. Comparison ([download notebook](data8-textbook/chapters/04/3/Comparison.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/04/3/Comparison.ipynb))
- Pre-class quiz in eCampus
- Class activities
	- [py01](py01/index.md): Python Basics

*Whirlwind Tour of Python Chapter 6*

- Reading
	- [Whirlwind Tour: Built-in Data Structures](https://jakevdp.github.io/WhirlwindTourOfPython/06-built-in-data-structures.html)
- Class activities
	- [py02](py02/index.md): Python Data

### Week 3 (Sep 1, 2025)

*Whirlwind Tour of Python Chapter 7*

- Reading
	- [Whirlwind Tour: Control Flow](https://jakevdp.github.io/WhirlwindTourOfPython/07-control-flow-statements.html)
- Class activities
	- [py03](py03/index.md): Control flow

*Whirlwind Tour of Python Chapter 8*

- Reading
	- [Whirlwind Tour: Functions](https://jakevdp.github.io/WhirlwindTourOfPython/08-defining-functions.html)
- Class activities
	- [py04](py04/index.md): Functions

### Week 4 (Sep 8, 2025) 

*Handbook: Introduction to NumPy and Pandas*

- Reading
	- [Handbook: Introduction to NumPy](https://jakevdp.github.io/PythonDataScienceHandbook/02.00-introduction-to-numpy.html)
	- [Handbook: Pandas](https://jakevdp.github.io/PythonDataScienceHandbook/03.00-introduction-to-pandas.html)
- Class activities
	- [py05](py05/index.md): Pandas


### Week 5 (Sep 15, 2025) 

- Reading
	- [Handbook: Seaborn](https://jakevdp.github.io/PythonDataScienceHandbook/04.14-visualization-with-seaborn.html)
- Class activities
	- [py06](py06/index.md): Visualization with Seaborn


Exam 1

- **Book Chapters:**
- **Activities:**

- 09. Randomness ([download notebook](data8-textbook/chapters/09/Randomness.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/09/Randomness.ipynb))
- 09.1. Conditional Statements ([download notebook](data8-textbook/chapters/09/1/Conditional_Statements.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/09/1/Conditional_Statements.ipynb))
- 09.2. Iteration ([download notebook](data8-textbook/chapters/09/2/Iteration.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/09/2/Iteration.ipynb))
- 09.3. Simulation ([download notebook](data8-textbook/chapters/09/3/Simulation.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/09/3/Simulation.ipynb))
- 09.4. Monty Hall Problem ([download notebook](data8-textbook/chapters/09/4/Monty_Hall_Problem.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/09/4/Monty_Hall_Problem.ipynb))
- 09.5. Finding Probabilities ([download notebook](data8-textbook/chapters/09/5/Finding_Probabilities.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/09/5/Finding_Probabilities.ipynb))

### Week 6 (Sep 22, 2025) 

- **Book Chapters:**
- **Activities:**
- 10. Sampling And Empirical Distributions ([download notebook](data8-textbook/chapters/10/Sampling_and_Empirical_Distributions.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/10/Sampling_and_Empirical_Distributions.ipynb))
- 10.1. Empirical Distributions ([download notebook](data8-textbook/chapters/10/1/Empirical_Distributions.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/10/1/Empirical_Distributions.ipynb))
- 10.2. Sampling From A Population ([download notebook](data8-textbook/chapters/10/2/Sampling_from_a_Population.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/10/2/Sampling_from_a_Population.ipynb))
- 10.3. Empirical Distribution Of A Statistic ([download notebook](data8-textbook/chapters/10/3/Empirical_Distribution_of_a_Statistic.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/10/3/Empirical_Distribution_of_a_Statistic.ipynb))
- 10.4. Random Sampling In Python ([download notebook](data8-textbook/chapters/10/4/Random_Sampling_in_Python.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/10/4/Random_Sampling_in_Python.ipynb))


- **Book Chapters:**
- **Activities:**
- 11. Testing Hypotheses ([download notebook](data8-textbook/chapters/11/Testing_Hypotheses.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/11/Testing_Hypotheses.ipynb))
- 11.1. Assessing A Model ([download notebook](data8-textbook/chapters/11/1/Assessing_a_Model.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/11/1/Assessing_a_Model.ipynb))
- 11.2. Multiple Categories ([download notebook](data8-textbook/chapters/11/2/Multiple_Categories.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/11/2/Multiple_Categories.ipynb))
- 11.3. Decisions And Uncertainty ([download notebook](data8-textbook/chapters/11/3/Decisions_and_Uncertainty.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/11/3/Decisions_and_Uncertainty.ipynb))
- 11.4. Error Probabilities ([download notebook](data8-textbook/chapters/11/4/Error_Probabilities.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/11/4/Error_Probabilities.ipynb))

- **Book Chapters:**
- **Activities:**
- 12. Comparing Two Samples ([download notebook](data8-textbook/chapters/12/Comparing_Two_Samples.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/12/Comparing_Two_Samples.ipynb))
- 12.1. Ab Testing ([download notebook](data8-textbook/chapters/12/1/AB_Testing.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/12/1/AB_Testing.ipynb))
- 12.2. Causality ([download notebook](data8-textbook/chapters/12/2/Causality.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/12/2/Causality.ipynb))
- 12.3. Deflategate ([download notebook](data8-textbook/chapters/12/3/Deflategate.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/12/3/Deflategate.ipynb))


### Week 7 (Sep 29, 2025) 

*Chapter 13: Estimates*
- *Reading
- 13. Estimation ([download notebook](data8-textbook/chapters/13/Estimation.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/13/Estimation.ipynb))
- 13.1. Percentiles ([download notebook](data8-textbook/chapters/13/1/Percentiles.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/13/1/Percentiles.ipynb))
- 13.2. Bootstrap ([download notebook](data8-textbook/chapters/13/2/Bootstrap.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/13/2/Bootstrap.ipynb))
- 13.3. Confidence Intervals ([download notebook](data8-textbook/chapters/13/3/Confidence_Intervals.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/13/3/Confidence_Intervals.ipynb))
- 13.4. Using Confidence Intervals ([download notebook](data8-textbook/chapters/13/4/Using_Confidence_Intervals.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/13/4/Using_Confidence_Intervals.ipynb))


*Chapter 14: Central Measures*
- 14. Why The Mean Matters ([download notebook](data8-textbook/chapters/14/Why_the_Mean_Matters.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/14/Why_the_Mean_Matters.ipynb))
- 14.1. Properties Of The Mean ([download notebook](data8-textbook/chapters/14/1/Properties_of_the_Mean.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/14/1/Properties_of_the_Mean.ipynb))
- 14.2. Variability ([download notebook](data8-textbook/chapters/14/2/Variability.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/14/2/Variability.ipynb))
- 14.3. Sd And The Normal Curve ([download notebook](data8-textbook/chapters/14/3/SD_and_the_Normal_Curve.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/14/3/SD_and_the_Normal_Curve.ipynb))
- 14.4. Central Limit Theorem ([download notebook](data8-textbook/chapters/14/4/Central_Limit_Theorem.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/14/4/Central_Limit_Theorem.ipynb))
- 14.5. Variability Of The Sample Mean ([download notebook](data8-textbook/chapters/14/5/Variability_of_the_Sample_Mean.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/14/5/Variability_of_the_Sample_Mean.ipynb))
- 14.6. Choosing A Sample Size ([download notebook](data8-textbook/chapters/14/6/Choosing_a_Sample_Size.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/14/6/Choosing_a_Sample_Size.ipynb))

Chapter 15: Regression

- 15. Prediction ([download notebook](data8-textbook/chapters/15/Prediction.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/15/Prediction.ipynb))
- 15.1. Correlation ([download notebook](data8-textbook/chapters/15/1/Correlation.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/15/1/Correlation.ipynb))
- 15.2. Regression Line ([download notebook](data8-textbook/chapters/15/2/Regression_Line.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/15/2/Regression_Line.ipynb))
- 15.3. Method Of Least Squares ([download notebook](data8-textbook/chapters/15/3/Method_of_Least_Squares.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/15/3/Method_of_Least_Squares.ipynb))
- 15.4. Least Squares Regression ([download notebook](data8-textbook/chapters/15/4/Least_Squares_Regression.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/15/4/Least_Squares_Regression.ipynb))
- 15.5. Visual Diagnostics ([download notebook](data8-textbook/chapters/15/5/Visual_Diagnostics.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/15/5/Visual_Diagnostics.ipynb))
- 15.6. Numerical Diagnostics ([download notebook](data8-textbook/chapters/15/6/Numerical_Diagnostics.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/15/6/Numerical_Diagnostics.ipynb))
### Week 8 (Oct 6, 2025) 

- **Book Chapters:**
- **Activities:**
- 16. Inference For Regression ([download notebook](data8-textbook/chapters/16/Inference_for_Regression.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/16/Inference_for_Regression.ipynb))
- 16.1. Regression Model ([download notebook](data8-textbook/chapters/16/1/Regression_Model.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/16/1/Regression_Model.ipynb))
- 16.2. Inference For The True Slope ([download notebook](data8-textbook/chapters/16/2/Inference_for_the_True_Slope.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/16/2/Inference_for_the_True_Slope.ipynb))
- 16.3. Prediction Intervals ([download notebook](data8-textbook/chapters/16/3/Prediction_Intervals.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/16/3/Prediction_Intervals.ipynb))

### Week 9 (Oct 13, 2025) 

Exam 2

### Week 10 (Oct 20, 2025) 


- **Book Chapters:**
- **Activities:**
- 17. Classification ([download notebook](data8-textbook/chapters/17/Classification.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/17/Classification.ipynb))
- 17.1. Nearest Neighbors ([download notebook](data8-textbook/chapters/17/1/Nearest_Neighbors.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/17/1/Nearest_Neighbors.ipynb))
- 17.2. Training And Testing ([download notebook](data8-textbook/chapters/17/2/Training_and_Testing.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/17/2/Training_and_Testing.ipynb))
- 17.3. Rows Of Tables ([download notebook](data8-textbook/chapters/17/3/Rows_of_Tables.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/17/3/Rows_of_Tables.ipynb))
- 17.4. Implementing The Classifier ([download notebook](data8-textbook/chapters/17/4/Implementing_the_Classifier.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/17/4/Implementing_the_Classifier.ipynb))
- 17.5. Accuracy Of The Classifier ([download notebook](data8-textbook/chapters/17/5/Accuracy_of_the_Classifier.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/17/5/Accuracy_of_the_Classifier.ipynb))
- 17.6. Multiple Regression ([download notebook](data8-textbook/chapters/17/6/Multiple_Regression.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/17/6/Multiple_Regression.ipynb))
- 18. Updating Predictions ([download notebook](data8-textbook/chapters/18/Updating_Predictions.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/18/Updating_Predictions.ipynb))
- 18.1. More Likely Than Not Binary Classifier ([download notebook](data8-textbook/chapters/18/1/More_Likely_than_Not_Binary_Classifier.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/18/1/More_Likely_than_Not_Binary_Classifier.ipynb))
- 18.2. Making Decisions ([download notebook](data8-textbook/chapters/18/2/Making_Decisions.ipynb)) ([view online](https://nbviewer.org/github/profgarrett/course_model/blob/main/data8-textbook/chapters/18/2/Making_Decisions.ipynb))

### Week 11 (Oct 27, 2025) 


### Week 13 (Nov 10, 2025) 



### Week 14 (Nov 17, 2025) 

- **Book Chapters:**
- **Activities:**

### Week 15 (Nov 24, 2025) 

No activities due to Fall Break.

### Week 16 (Dec 1, 2025) 

- **Book Chapters:**
- **Activities:**

### Week 17 (Dec 8, 2025) 

December 11, last day of classes.

- **Activities:**
  - Exam 3

### Week 18 (Dec 15-19, 2025)  Finals!

Finals week
