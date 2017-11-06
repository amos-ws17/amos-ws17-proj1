
## Collection of publicly available data sets

The more data the better, so if anyone finds a data set can put it here, so we dont lose any knowledge. The scale for the Integration Complexity is the following:

Easy - Either completely integratable or requires very little work

Medium - Integratable, but will require building a parser or doing it by hand

Hard - Almost impossible to integrate

| Topic  | Data format  | Integration Complexity  | Link |
|---|---|---|---|
| book a hotel (Frames) | JSON | Medium | https://datasets.maluuba.com/Frames/dl|
| Restaurant search | JSON | Easy | https://github.com/RasaHQ/rasa_nlu/blob/master/data/examples/rasa/demo-rasa.json |
| Collection of data sets | Similar to CSV | Medium | https://research.fb.com/downloads/babi/ |
| Q/A from CNN/Daily Mail articles | Txt | Medium | https://github.com/deepmind/rc-data |
| Q/A Wikipedia | JSON | Medium | https://www.kaggle.com/stanfordu/stanford-question-answering-dataset/data |
| Q/A Popular websites (StackOverflow) | JSON | Medium | http://curtis.ml.cmu.edu/datasets/quasar/ |
| Q/A Trivia | XML | Medium | http://trec.nist.gov/data/qa.html |
| Q/A Different (e.g. Weather) | JSON | Easy/Medium | https://github.com/snipsco/nlu-benchmark |
| Other popular data sets (Movie dialogues etc.) | - | Hard | https://www.reddit.com/r/MachineLearning/comments/3ukvc6/datasets_of_one_to_one_conversations/ |
|   |   |   |   |

*) Q/A - Question Answer


**Collection of data sets:** (Maybe) 
It contain multiple datasets
*"WikiMovies Dataset":* It contain many categories such as (language of movie, director of movie, rate ,etc.) we can make this category as an intent.

**Q/A from CNN/Daily Mail articles:**

**Q/A Wikipedia:**

**Q/A Popular websites (StackOverflow):** 

**Q/A Trivia:**
 It contains texts as question only, there is no type of conversation

**Q/A Different :** 
It is a good candidate. We can pick one of the Q/A domain and use it. It is almost structured as RSA NLU need.

**Other popular data sets (Movie dialogues etc):** 
It contains a metadata-rich collection of fictional conversations extracted from raw movie scripts, and we can not structure it in a useful way that train Rasa NLU model. Although consist of  rich knowledge, but we can not extract one topic from it!
