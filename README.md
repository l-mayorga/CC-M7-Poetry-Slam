# CC-M7-Poetry-Slam

BanaN-Grams uses n-grams generated from about ten thousand poems to generate and present poetry. After generating a poem, it will be read aloud to you and displayed in front of a suitable background image. If the system cannot find a suitable image for the generated poem, it will use one of a banana.

Although n-grams are known to produce grammatically correct yet incoherent output, BanaN-Grams strives to keep the poem on topic.

## Usage

_NOTE: Must use your own Unsplash API key inside of `unsplash.py` for the system to work. See Dependencies._

`python perform_poem.py`

## Dependencies

- [spaCy](https://spacy.io/usage) - Natural language processing
- [PIL](https://pillow.readthedocs.io/en/stable/installation/basic-installation.html) - Working with PNGs
- [text-to-image](https://pypi.org/project/text-to-image/) - PNG editing via PIL
- [pandas](https://pypi.org/project/text-to-image/) - Data processing
- [Unsplash Developer API Key](https://pypi.org/project/text-to-image/) - Image sourcing

## Resources

Kaggle [Poetry Foundation Poems Datasaet](https://www.kaggle.com/datasets/tgdivy/poetry-foundation-poems?resource=download)

## Scholarly Citations

[Computational Modelling of Poetry Generation](http://nil.fdi.ucm.es/sites/default/files/GervasAISB2013CRC.pdf)

- This review considers strengths and weaknesses of approaching to computational poetry generation. It introduces n-grams as a form of stochastic language modeling and considers the coherence of the poetry it generates. This inspired my evaluation to address coherence via similarity.

[AI-generated poetry is indistinguishable from human-written poetry and is rated more favorably](https://www.nature.com/articles/s41598-024-76900-1)

- This study indicates that humans prefer AI generated poetry - many times because of its simplicity. It states that AI generated poetry passes the turing test. This made me consider using a more AI approach like an LLM.

[Text And Image – The Relationship Between Text And Image In Research](https://pressbooks.pub/academischevaardigheden/chapter/hoofdstuk-7-2-text-and-image-the-relationship-between-text-and-image-in-research/)

- This study argues that neither words nor images alone are the most medium to convey information or to tell a story. Instead, it is best to combine both. In my system, the background images add to the effect of reading and listening to the poem.

## Challenges

I tackled the front-end and presentation part first, so the first challenge I encountered was working with the Unsplash API to source background images. I had never gone through the process of applying for an API key and using it in the code. I learned that it's best to store sensitive data like API keys in the environment instead of just having it in the code. The other challenge with the front end was working with PNGs. It was my first time using PIL to work with images and forking another repo to use to modified version of someone else's code.

The next challenge was creating n-grams. I knew I wanted to create my own lightweight version instead of using another module's. I remembered the basic concept from the Data Structures lab, but I had a couple difficulties ironing out the fine detail.
