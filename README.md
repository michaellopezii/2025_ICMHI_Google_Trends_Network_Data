# Overview

This is the repository for the Jupyter notebook and dataset used for the following conference paper:

Michael T. Lopez, Cheska Elise Hung, and Maria Regina Justina E. Estuar.\
**Network Density Analysis of Health Seeking Behavior in Metro Manila: A Retrospective Analysis on COVID-19 Google Trends Data**\
In Proceedings of the 9th International Conference on Medical and Health Informatics (ICMHI 2025)\
Link: https://doi.org/10.48550/arXiv.2503.21162 (currently available as a pre-print on arXiv)

It was the first part of the undergraduate thesis of Michael T. Lopez II and Cheska Elise Hung from the Ateneo de Manila University, Philippines. Our supervisor for this work is Dr. Maria Regina Justine E. Estuar, PhD. 

This paper's goal is to determine the online health-seeking behavior of those residing in Metro Manila (National Capital Region) on how they utilized Google for searching terms related to the COVID-19 pandemic. However, instead of investigating each term individually, we converted them into a network graph using correlation and adjacency matrices.

## Requirements

The following code was ran on an Apple Macbook Air M1 (2020). Here are the specifications of the hardware:

| Hardware | Specification |
|----------|---------------|
| Model | MacBook Air (M1, 2020) |
| Processor | Apple M1 chip with 8-core CPU |
| Memory | 8GB unified memory |
| Storage | 256GB SSD |

We then used the `python` programming language (version 3.12.2) on Jupyter notebook.

# How to Cite

If you will use or build upon on top of the code materials, please use the following BibTeX entry below to cite the concerned paper depending on the purpose of what code you will be using. Take note that you should *not* be citing this Github repository directly.

## Google Trends Scraper

If you will be using the Google Trends scraper using the `pytrends` API, the scripts are located at the `gt_scraper` directory. This code was originated from as referenced in ACM format: 

Amanda M Y Chu, Andy C Y Chong, Nick H T Lai, Agnes Tiwari, and Mike K P So. 2023. Enhancing the Predictive Power of Google Trends Data Through Network Analysis: Infodemiology Study of COVID-19. *JMIR Public Health Surveill.* 9, (September 2023). https://doi.org/10.2196/42446

Below is the BibTeX entry of the article:

```bibtex
@article{chuEnhancing2023,
  title = {Enhancing the {{Predictive Power}} of {{Google Trends Data Through Network Analysis}}: {{Infodemiology Study}} of {{COVID-19}}},
  shorttitle = {Enhancing the {{Predictive Power}} of {{Google Trends Data Through Network Analysis}}},
  author = {Chu, Amanda M Y and Chong, Andy C Y and Lai, Nick H T and Tiwari, Agnes and So, Mike K P},
  year = {2023},
  month = sep,
  journal = {JMIR Public Health and Surveillance},
  volume = {9},
  issn = {2369-2960},
  doi = {10.2196/42446},
}
```

## Google Trends Preprocessing and Network Analysis Conversion

For the remainder of the other code and all datasets used, these were all original work from our team. Please use the following BibTeX entry to cite our paper if you have used any part of the code or dataset (besides the Google Trends scraper script):

```bibtex
@misc{lopezNetwork2025,
  title = {Network {{Density Analysis}} of {{Health Seeking Behavior}} in {{Metro Manila}}: {{A Retrospective Analysis}} on {{COVID-19 Google Trends Data}}},
  shorttitle = {Network {{Density Analysis}} of {{Health Seeking Behavior}} in {{Metro Manila}}},
  author = {Lopez, Michael T. II and Hung, Cheska Elise and Estuar, Maria Regina Justina E.},
  year = {2025},
  month = mar,
  number = {arXiv:2503.21162},
  eprint = {2503.21162},
  primaryclass = {cs},
  publisher = {arXiv},
  doi = {10.48550/arXiv.2503.21162},
}
```

This will be updated accordingly in the future once we have received the official DOI when the conference indexed our work. For now, the pre-print version could be viewed at arXiv.



