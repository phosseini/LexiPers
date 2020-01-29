# LexiPers: A Sentiment Analysis Lexicon for Persian

[![DOI:10.29007/f4j4](https://zenodo.org/badge/DOI/10.29007/f4j4.svg)](https://doi.org/10.29007/f4j4)

LexiPers is an ontology based sentiment lexicon for Persian. As part of building LexiPers, we manually annotated over 4,000 Persian adjective synonym sets from [FarsNet](http://farsnet.nlp.sbu.ac.ir/Site3/Modules/Public/Default.jsp) as our seed set.

We are making this seed set publicly available (previously it was only available upon request via email.) LexiPers is in maintenance mode and we are not actively developing or expanding its entries. However, we would definitely be interested to receive feedback and hear from you on how potentially we can improve LexiPers and make it a better resource for the Natural Language Processing community.

### Instructions for API
We have provided a minimal API which contains some helper methods to make working with LexiPers easier. You can find these methods in `lexipy.py`. We have also included a jupyter notebook, `demo.ipynb`, to show how these methods can be used.

Before using the methods, make sure LexiPers's file exists in the following path:

`data/adj-final.xml`

You also need to install `pandas` to use the API methods. 

When creating a new object of **LexiPy** from the `lexipy.py`, a local copy in `data` folder will be created to make sure all the updates you may potentially have, will not change the original LexiPers file. For now, the only method we included for updating information in LexiPers is for the synsets' label.


### Collaboration/Contribution
We encourage you to submit issues or enhancement suggestions here in this repository so that we can better track them. Also, if you have any helper method in mind, feel free to submit a pull request, we will be more than happy to review them. We highly value and appreciate your contributions to the API.

Feel free to reach out to [Pedram Hosseini](mailto:pdr.hosseini@gmail.com) with any questions.

### Citation Information
If you found LexiPers interesting or used it in your work, please use the following information for citation:

```
@inproceedings{sabeti2016lexipers,
  title={LexiPers: An ontology based sentiment lexicon for Persian},
  author={Sabeti, Behnam and Hosseini, Pedram and Ghassem-Sani, Gholamreza and Mirroshandel, Seyed Abolghasem},
  booktitle={2nd Global Conference on Artificial Intelligence (GCAI)},
  volume={41},
  pages={329--339},
  year={2016},
  organization={EasyChair}
}
```
