# LexiPers: A Sentiment Analysis Lexicon for Persian

[![DOI:10.29007/f4j4](https://zenodo.org/badge/DOI/10.29007/f4j4.svg)](https://doi.org/10.29007/f4j4)

<p dir='rtl' align='right'>
لغت‌نامهٔ احساس لِکسی‌پِرس، شامل زیرمجموعه‌ای از واژگان نسخهٔ دوم فارس‌نت است که با روشی خودکار و با دسته بندی مثبت، منفی و خنثی برچسب‌گذاری شده‌اند. طی فاز اول این پروژه، به عنوان بخشی از فرایند ابتدایی، کلیه مجموعه‌های ترادف دارای نقش صفت، تعداد ۴۲۶۱ مجموعه، به صورت دستی و با هوش انسانی تحت عنوان مجموعه دانه برچسب‌گذاری شدند. دلیل انتخاب مجموعه‌های صفت احتمال بالاتر آنها برای داشتن بار معنایی مشخص تر، نسبت به سایر نقشهای دستوری نظیر اسم، بود. این مجموعه دانه می‌تواند به عنوان یک استاندارد طلایی و حتی یک مجموعه دانه اولیه برای توسعه و یا آزمودن سیستم‌های برچسب‌گذاری لغات، دسته‌بندی اسناد و مدلهای مرتبط با تحلیل احساس مورد استفاده قرار گیرد. ذکر این نکته نیز ضروری است که هر ورودی در این مجموعه، شناسه متناظر در مجموعه فارس‌نت را نیز به همراه خود دارد، بنابراین به راحتی می‌توان مجموعه متناظر هر ورودی در این مجموعه دانه در فارس‌نت را یافت.
</p>

<p dir='rtl' align='right'>
این لغتنامه در دوره کارشناسی ارشد بهنام ثابتی، از آزمایشگاه پردازش زبان طبیعی دانشگاه صنعتی شریف تحت سرپرسی دکتر غلامرضا قاسم ثانی، و پدرام حسینی، از گروه پردازش زبان طبیعی دانشگاه گیلان به سرپرستی دکتر سید ابوالقاسم میرروشندل، و به عنوان بخشی از پایان نامه ایشان توسعه داده شد.
</p>

<p dir='rtl' align='right'>
لطفا در صورت استفاده از این مجموعه به شکلی که در ادامه آمده به آن ارجاع دهید. این مجموعه در حال حاضر در مرحله نگهداری است و توسعه جدیدی بروی آن صورت نخواهد گرفت، هرچند از تمامی علاقمندان جهت بهتر و کامل تر کردن آن دعوت بعمل می آید.
</p>

LexiPers is an ontology based sentiment lexicon for Persian. As part of building LexiPers, we manually annotated over 4,000 Persian adjective synonym sets from [FarsNet](http://farsnet.nlp.sbu.ac.ir/Site3/Modules/Public/Default.jsp), as an initial seed set.

We are making this seed set publicly available (it was available upon request via email before.) LexiPers is in maintenance mode and we are not actively developing or expanding its entries. However, we would be interested to receive feedback and hear from you on how potentially we can improve LexiPers and make it a better resource for the Persian Natural Language Processing community.

### Instructions for API
We have provided a minimal API which contains some helper methods to make working with LexiPers a bit easier. You can find these methods in `lexipy.py`. We have also included a jupyter notebook, `demo.ipynb`, to show how these methods can be used.

Before using the methods, make sure LexiPers's file exists in the following path:

`data/adj-final.xml`

You also need to install `pandas` to use the API methods. `pandas` can be installed using the following command (more details can be found [here](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)):

`pip install pandas`

When creating a new object of **LexiPy** from the `lexipy.py`, a local copy in `data` folder will be created to make sure all the updates you may potentially have, will not change the original LexiPers file. For now, the only method we included for updating information in LexiPers is for the synsets' label. So if you think an assigned label needs to be updated or modified, this method can be handy.


### Collaboration/Contributions
We encourage you to submit issues or enhancement suggestions here in this repository so that we can better keep track of them. If you have any helper method in mind, feel free to submit a pull request, we will be more than happy to review them. We highly value and appreciate your contributions to the API.

Feel free to reach out to [Pedram Hosseini](mailto:pdr.hosseini@gmail.com) with any questions.

### Citation Information
LexiPers was developed as part of a collaboration between Sharif University of Technology's NLP Lab and University of Guilan's NLP group. If you found LexiPers interesting or used it in your work, please use the following information for citation:

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
