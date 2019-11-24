---
layout: archive
title: "Research"
permalink: /research/
author_profile: true
---

My past research investigates the genetic underpinnings of complex diseases. Most of my previous work have focused on coronary artery disease, the No. 1 killer of US adults, and on age-related macular degeneration, the leading cause of blindness in adults > 50 years of age. To pick out key genes that influence the risk of these diseases among the vast number of genes in the human genome, I developed methods to prioritze and visualize signals from [genetic associations studies](https://en.wikipedia.org/wiki/Genetic_association). Selected areas of my research include:

How does genetic variants influence the risk of complex human diseases?
----

An individual's risk towards complex diseases is influenced by his/her genetic makeup. A notable example is that certain mutations in the *BRCA* genes greatly increase women's susceptibility towards breast cancer. Thus far, we understand little about the underlying mechanisms for all but a handful of risk variants. 

The quest for disease mechanisms requires a fundamental understanding of genetic regulation in humans. I am a avid contributor to the Genome-Type Tissue Expression project [[GTEx Consortium 2017, Nature](https://www.nature.com/articles/nature24277)], aimed at identifying genetic effects on gene expression across many human tissues. Knowing genetic regulation in a health population is not enough. To understand a particular disease, we need to sample tissue types and even cell types specific to the pathological microenvironment (see review by [Liu and Montgomery 2019, Human Genetics](https://link.springer.com/article/10.1007%2Fs00439-019-02044-2)).

Using data from [genome-wide association studies](https://en.wikipedia.org/wiki/Genome-wide_association_study) and [expression quantitative trait loci](https://en.wikipedia.org/wiki/Expression_quantitative_trait_loci), I built statistical models to jointly infer the causal variants and the effector gene. My work have uncovered key risk genes for coronary artery disease [[Liu et al 2018, AJHG](https://www.cell.com/ajhg/fulltext/S0002-9297%2818%2930267-2)] and age-related macular degeneration [[Liu et al 2019, Communications Biology](https://www.nature.com/articles/s42003-019-0430-6)].


Which genetic mutations drive cancer? Can we use these mutations as diagnostic biomarkers? 
----
Cancer is a group of diseases in which genetic mutations drive abnormal growth of malignant cells. The genetic underpinnings of cancer dictate that key mutations will occur frequently in a given type of cancer. To discover these driver mutations, numerous efforts have assembled cohorts of patients with the same type of cancer and find mutations that occur high than expected statistically (see [TCGA 2013, Nature](https://www.nature.com/articles/ng.2764)). These key mutations can then be used to 1) accurately diagnose patients with a specific type of cancer, and 2) to act as biomarkers for drug development. In collaboration with the [the Gephart lab](http://www.gephartlab.com/), who has deep expertise in [leptomeningeal disease](https://en.wikipedia.org/wiki/Leptomeningeal_cancer), we estimate frequencies of somatic mutations using whole-exome data from patients with lung-metastasized leptomeningeal disease to identify driver mutations and correlate them with gold-standard clinical diagnosis to build a set of biomarkers to enhance the diagnostic toolkit [[Li et al 2018, JTO](https://www.sciencedirect.com/science/article/pii/S1556086418302223)].

My research interest in cancer diagnosis led me to briefly serve as the CTO of [Genenenux](http://www.genenexus.com/), a Shanghai-based startup that develops cancer diagnostic reagent kits. My team designed and updated the backend of [GeneReader®](http://genereader.cn/) to deliever high-accuracy variant calls and to integrate RNA and epigenomic processing capabilities. I currently serve on the company's scientific advisory board and continue to help improve its bioinformatics pipelines. 


Algorithms and software for bioinformatics and medical research
----
My research frequently requires the design and implementation of new software to iterate through experiments faster, obtain results with higher accuracy, or simply to fulfill unmet needs. For [Liu e al 2018, AJHG](https://www.cell.com/ajhg/fulltext/S0002-9297%2818%2930267-2), I wrote software to approximate sum of non-identical binomial random variables [[Liu and Quertermous 2017, R Journal](https://journal.r-project.org/archive/2018/RJ-2018-011/RJ-2018-011.pdf)]. Further, I wrote a number of tools for [Liu et al 2019, Communications Biology](https://www.nature.com/articles/s42003-019-0430-6). To select the population for this study, I designed the [ANTseq](https://github.com/boxiangliu/ANTseq) pipeline to reduce the cost of ancestry determination [[Liu et al 2016](http://stanford.edu/~bliu2/pubs/ANTseq.pdf)]. I also developed [Manhattan](https://github.com/boxiangliu/manhattan) to visualize single genetic association studies. To visualize and compare multiple genetic association studies, I released LocusCompare both as a [web service](http://locuscompare.com/) and an [R package](https://github.com/boxiangliu/locuscomparer) [[Liu et al 2019, Nature Genetics](https://www.nature.com/articles/s41588-019-0404-0)]. 

Other software are inspired by needs other than my own. In collaboration with the [Kundaje lab](https://sites.google.com/site/anshulkundaje/), we developed a deep learning architecture to jointly model the cis- and trans-regulators of gene expression. Genetic regulation involves nonlinear interactions between transcription factor molecules (trans-effects) and DNA sequences (cis-effects). Such interactions involve the interplay across multiple molecules, whose combinatorial relationships are difficult to capture through feature-engineered networks. We use a data-driven approach to model regulatory relationship using a deep neural network. Our method outperformed the previous state-of-the-art by as much as 20% [[Liu et al 2017, NIPS](https://arxiv.org/abs/1908.09426)].


Earlier research
----
I studied biophysics at Illinois Wesleyan University and had a great time working with [Thushara Perera](http://sun.iwu.edu/~tperera/research.html) on [biopotential measurement device](https://digitalcommons.iwu.edu/cgi/viewcontent.cgi?referer=https://scholar.google.com/&httpsredir=1&article=2888&context=jwprc), and on [special relativity](https://arxiv.org/abs/1508.01968). I also enjoyed working with [Gabe Spalding](http://sun.iwu.edu/~gspaldin/Site/Overview.html) on building a [confocal microsope](https://digitalcommons.iwu.edu/jwprc/2012/posters2/11/) and [optical tweezers](https://digitalcommons.iwu.edu/jwprc/2013/posters2/21/).