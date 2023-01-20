# smg-gdt-bi-hiring-challenge 

<a name="readme-top"></a>

<!-- SMG LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/smg-gdt-bi-hiring-challenge">
    <img src="https://swissmarketplace.group/wp-content/uploads/2022/07/smg-logo-green.svg" alt="Logo">
  </a>

<h3 align="center"><b>BI Hiring Challenge</b></h3>

  <p align="center">
    [built by GDT]
    <br />
    <a href="https://swissmarketplace.group/"><strong>Explore the Website »</strong></a>
    <br />
    <br />
    <a href="https://github.com/github_username/smg-gdt-bi-hiring-challenge/issues">Report Bug</a>
    ·
    <a href="https://github.com/github_username/smg-gdt-bi-hiring-challenge/issues">Request Feature</a>
  </p>
</div>


<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About</a>
      <ul>
        <li><a href="#built-with">An SMG BI dev is building with</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#setup">Setup</a></li> 
        <li><a href="#deliverables">Deliverables</a></li> 
      </ul>
    </li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>
<br />


<!-- About -->
## About

<!--[![Product Name Screen Shot][product-screenshot]](https://example.com) -->

The goal of this project is to provide a comprehensive BI hiring challenge to our candidates, offering a standardized and well structured case study while allowing the candidates full autonomy over the approach. This repository contains the standardized raw flat files which can be ingested in any way best suiting the candidate, three different challenges to be tackled in regards to the data provided, and subtleties for extra points for those so inclined. There's no strict time constraint on this case study. We expect candidates to inform us when they are ready and to respect the honor system on the time invested and approaches taken. We're evaluating the knowledge and understanding of core data concepts, BI techniques, quality of work. Each will be addressed in the interview following the completion of the case study. 

We're estimating one full work day (eight working hours) to complete a 100% of what this case study has to offer. Candidates are offered twice as much. In case of investing more (or less) than the estimate, we expect open communication on the context and welcome any approach and efforts invested. 

>*TL:DR - from Excel to a full blown Python environment, any approach is welcome as long as it gets the job done.*



### An SMG BI dev is building with ... 
<br />

* [![Python][Python]][Python-url]
* [![DBT][DBT]][DBT-url]
* [![GoogleCLoud][GoogleCLoud]][GoogleCLoud-url]
* [![Looker][Looker]][Looker-url]
* [![Github][Github]][Github-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Essentially, the approach is open and involves setting up a local environment, processing the provided raw flat files, answering the questions and presenting the thought process behind the whole approach to solving the challenge. Main evaluation criteria is the validity of the SQL queries, followed by the presentation layer of candidate's choosing, and finally the overall quality of the setup, process, and result. We expect a pull request by the candidate, marking the completion of the challenges. The repo structure is as follows: 

```
.
├── README.md
├── candidate
│   ├── answers
│   │   └── placeholder.md
│   ├── data
│   │   ├── dim_date.csv
│   │   ├── dim_platform.csv
│   │   ├── dim_product_type.csv
│   │   ├── dim_status.csv
│   │   ├── dim_user.csv
│   │   └── fct_listings.csv
│   ├── questions
│   │   ├── question_q01.md
│   │   ├── question_q02.md
│   │   └── question_q03.md
│   └── utils
│       └── helper_duckdb.py
└── repo_assets
    └── smg-logo-green.png
```

Resources the candidate requires for a local setup are contained withing the `candidate` folder: 
- `answers` - target location for the main assets used in the PR provided by the candidate; 
- `data` - flat files organized in a star schema, to be consumed and processed in search for answers; 
- `questions` - containing tasks to be tackled; 
- `utils` - a quick helper script to initiate a duckdb instance. Its usage is optional, can be ignored, modified, extended or replaced... candidate's choice. 

<br />

### Prerequisites

To successfully solve all of the tasks presented by the challenges in this case study, one would need a way to ingest and process flat files, write and test SQL queries, visualize the results. 

For a local environment, these are the quickest minimal requirements: 
* Python (3.9.x and newer); 
    * pandas
    * duckdb

Please note these methods and tools can be completely replaced or modified in any way, as long as the end result is correct.


### Setup

1. Python - choose your platform and proceed as per [standard instructions](https://www.python.org/downloads/); 
    * `pandas` and `duckdb`
  ```sh
  pip3 install pandas
  pip3 install duckdb==0.6.1
  ```
2. Clone the repo;
   ```sh
   git clone https://github.com/SMG-Group/smg-gdt-bi-hiring-challenge.git
   ``` 
   * Create your branch: 
   ```sh
   git checkout -b <candidate_firstname_lastname>
   ``` 
3. Instantiate the `duckdb` (example provided in the `./candidate/utils/helper_duckdb.py`);
  
4. That's it! 
   ```sh
   echo 'Good luck & have fun!'
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### <u>Deliverables</u> 

- All your answer-related files should be contained in the `answers` folder. If you extend the utils or do any changes outside of that folder, please document the context before opening a pull request. 

#### <u>Assumptions</u>
* The tasks should be done in a sequential order from #1 to #3;

* The data design is a star schema and the fact table contains periodic snapshots of listings (classifieds);

* The data is in a tabular format and contains separate datasets for product type, date, platform, status and user;

* The data is a fictional dataset created specifically for this case study and does not reflect reality;

* The data might be inaccurate and we will be delighted if you spot something and give us feedback.

#### <u>Evaluation criteria</u> 

* The process matters more than the final result and the goal is to understand how you solve problems;

* The final output should be well-organized and easy to understand;

* The insights provided should be relevant and actionable;

* The data visualizations should be intuitive to use and provide a clear view of the data;

* The explanation of the process should be clear and concise;

* The most important thing is the level of understanding of core BI Development concepts and best practices. 

#### <u>Scoring</u> 

* Task q01 : 3 points;

* Task q02: 5 points (1 point per component);

* Task q03 : 5 points (1 point per component);

<br />

<!-- CONTACT -->
## Contact

Group Data Team - [send us an email at grp.data-team@swissmarketplace.group](grp.data-team@swissmarketplace.group)

Project Link: [https://github.com/SMG-Group/smg-gdt-bi-hiring-challenge](mailto:https://github.com/SMG-Group/smg-gdt-bi-hiring-challenge)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Ileriayo](https://github.com/Ileriayo/markdown-badges) for the badges
* [othneildrew](https://github.com/othneildrew/Best-README-Template/blob/master/README.md) for markdown magic
* GDT for all the fun :) 

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[product-screenshot]: images/screenshot.png 
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Python-url]: https://www.python.org/downloads/
[DBT]: https://img.shields.io/badge/dbt-FF694B?style=for-the-badge&logo=dbt&logoColor=white
[DBT-url]: https://docs.getdbt.com/
[GoogleCloud]: https://img.shields.io/badge/Google_Cloud-4285F4?style=for-the-badge&logo=google-cloud&logoColor=white
[GoogleCloud-url]: https://cloud.google.com/
[Looker]: https://img.shields.io/static/v1?style=for-the-badge&message=Looker&color=4285F4&logo=Looker&logoColor=FFFFFF&label=
[Looker-url]: https://www.looker.com/
[Github]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[Github-url]: https://github.com/