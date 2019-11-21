---
permalink: /
title: "About"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Hello, I'm Boxiang, a research scientist at [Baidu Research Institute](http://research.baidu.com/Index). I am a computational biologist and a statistician by training, with a deep interest in the intersection between genetics, medicine and machine learning. My research investigates the genetic underpinnings of complex diseases. Most of my work have focused on coronary artery disease, the No. 1 killer of US adults, and on age-related macular degeneration, the leading cause of blindness in adults > 50 years of age. To pick out key genes that influence the risk of these diseases among the vast number of genes in the human genome, I developed methods to prioritze and visualize signals from [genetic associations studies](https://en.wikipedia.org/wiki/Genetic_association). Selected areas of my research include:

How does genetic variants influence the risk of complex human diseases?
----

An individual's risk towards complex diseases is influenced by his/her genetic makeup. A notable example is that certain mutations in the *BRCA* genes greatly increase women's susceptibility towards breast cancer. Thus far, we understand little about the underlying mechanisms for all but a handful of risk variants. 

The quest for disease mechanisms requires a fundamental understanding of genetic regulation in humans. I am a avid contributor to the Genome-Type Tissue Expression project [[GTEx Consortium 2017](https://www.nature.com/articles/nature24277)], aimed at identifying genetic effects on gene expression across many human tissues. Knowing genetic regulation in a health population is not enough. To understand a particular disease, we need to sample tissue types and even cell types specific to the pathological microenvironment (see review by [Liu and Montgomery 2019](https://link.springer.com/article/10.1007%2Fs00439-019-02044-2)).

Using data from [genome-wide association studies](https://en.wikipedia.org/wiki/Genome-wide_association_study) and [expression quantitative trait loci](https://en.wikipedia.org/wiki/Expression_quantitative_trait_loci), I built statistical models to jointly infer the causal variants and the effector gene. My work have uncovered key risk genes for coronary artery disease [[Liu et al 2018](https://www.cell.com/ajhg/fulltext/S0002-9297%2818%2930267-2)] and age-related macular degeneration [[Liu et al 2019](https://www.nature.com/articles/s42003-019-0430-6)].


Which genetic mutations drive cancer? Can we use these mutations as diagnostic biomarkers? 
----
Certain somatic mutations occurs frequently in given types of cancers. We estimate the frequency of each somatic coding mutation using whole-exome data from patient cohorts. We correlate them with gold-standard clinical diagnosis with the goal of identifying diagnostic biomarkers to enhance the diagnostic toolkit. In collaboration with with [the Gephart lab](http://www.gephartlab.com/), we study the recurrent mutations in leptomeningeal carcinomatosis. [example](https://www.biorxiv.org/content/early/2017/11/20/222349).
 
Can we model complex gene regulatory relationship with deep neural networks? What novel regulatory patterns can we extract from these networks? 
----
Genetic regulation involves nonlinear interactions between transcription factor molecules (trans-effects) and DNA sequences (cis-effects). Such interactions are often governed by the interplay by multiple molecule (think epistasis). The combinatorial complexity in these systems are difficult to capture using hand-engineered networks. In collaboration with [Kundaje lab](https://sites.google.com/site/anshulkundaje/), we use a data-driven approach to model regulatory networks using deep neural networks. Further, we try to extract novel regulatory relationship using *in silico* perturbation and backpropagation-based approaches. [example](http://stanford.edu/~bliu2/pubs/multi-modal-neural.pdf).

To answer these questions, I developed several statistical tools such as [sinib](https://github.com/boxiangliu/sinib) and [VSEA](https://github.com/boxiangliu/vsea), as well as visualization tools such as [manhattan](https://github.com/boxiangliu/manhattan) and locuscompare. 

Previously, I obtained a Master degree in Statistics from Stanford. Before that, I studied Biology and Physics at Illinois Wesleyan University. I had a great time working with [Thushara Perera](http://sun.iwu.edu/~tperera/research.html) on [biopotential measurement device](https://digitalcommons.iwu.edu/cgi/viewcontent.cgi?referer=https://scholar.google.com/&httpsredir=1&article=2888&context=jwprc), and on [special relativity](https://arxiv.org/abs/1508.01968). I also enjoyed working with [Gabe Spalding](http://sun.iwu.edu/~gspaldin/Site/Overview.html) on building a [confocal microsope](https://digitalcommons.iwu.edu/jwprc/2012/posters2/11/) and [optical tweezers](https://digitalcommons.iwu.edu/jwprc/2013/posters2/21/).

I maintain active collaborations with several PIs. Some of them are:

- [Douglas Vollrath](http://vollrathlab.stanford.edu/), Stanford University
- [Audrey Fu](http://webpages.uidaho.edu/audreyf/), University of Idaho
- [Anshul Kundaje](https://sites.google.com/site/anshulkundaje/), Stanford University
