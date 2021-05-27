import spacy
nlp = spacy.load('en_core_web_sm')
	 
	 
text = nlp(
	    'Jim bought 300 shares of Acme Corp. in 2006. And producing an annotated block of text that \
	    highlights the names of entities: [Jim]Person bought 300 shares of \
	    [Acme Corp.]Organization in [2006]Time. In this example, a person name consisting \
	    of one token, a two-token company name and a temporal expression have been detected \
	    and classified.State-of-the-art NER systems for English produce near-human performance. \
	    For example, the best system entering MUC-7 scored 93.39% of F-measure while human \
	    annotators scored 97.60% and 96.95%.[1][2]')
	 
for w in text.ents:
	print(w.text, w.label_)