
MSR_Xray Assignment 3
=====================

Note This is a reproduction project as part of the MSR course 2021/22 at UniKo, CS department, SoftLang Team
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Names of team/students Team: Xray
----------------------------------------------------------------------------------------------------------------------------

Members:
-------------------------------------------------------------------------

-   Karan Jagad 
-   Disha Hegde 
-   Allwin Noble

Baseline study:
---------------------------------------------------------------------------------------

RQ: Can we predict (non-) implication probabilistically by using just POM dependencies?

### Input data:

repositories_with_dependencies.csv 
ref : https://github.com/gorjatschev/applying-apis/tree/main/output 

### Output data:
 
- The CSV files containing list of coloums as mentioned below:
  - api_a	
  - api_b	
  - count_a	
  - count_b	
  - count_pair	
  - pom(a)	
  - pom(b)	
  - p(a)	
  - p(b)	
  - p(c_pair)	
  - p(a)*p(b)	
  - Percentage difference

Findings for the RQ
--------------------------------------------------------------------------------------------------------

### Process delta:

Collecting all the repositories based on above input data criteria and then Parsing the csv files under */process/repositories_with_dependencies folder* and finding the count_a, count_b,	count_pair, pom(a), pom(b), p(a), p(b), p(c_pair), p(a)*p(b), Percentage difference

### Output delta:

The output file mcr_assignment3_analyse.csv was generated.
The columns of the csv file contains.
Names of API dependency pairs.
The individual and combined occurence count for each API.
The corresponding  propabilities of each API .
The product of propabilities of each API.
The percent difference in the propabilities of combined occurence and product of individual occurences

### Implementation of running the code:

-   Hardware requirements:
    -   OS: Windows, Linux or MacOS
    -   Memory: 16 GB RAM recommended
    -   Processor : Ryzen 7 Core(TM) i7
-   Software requirements
-   -   Intellij
    -   Java 11 (Maven project) -only required if main thesis has to be executed
    -   Python 3.9.6 (pandas)
-   Validation
    -   To apply the simple probability we parsed ???repositories_with_dependencies.csv??? file available in the git repo of the thesis
    -   We could not find a direct probabilistic approach to show the dependency,Hence we came up with??an approach to show probabilistically that they are not independent
    -   To answer the research question,??our approach may not be the best fit to find out the implication, however this approach gives us a good idea of APIs not being independent hence suggesting implication between them.

