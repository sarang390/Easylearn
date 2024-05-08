from pipelines import pipeline

# import nltk
# nltk.download('punkt')


##transfromers==3.0.0

##nltk

##torch
#
qa = pipeline("question-generation")


qapair=qa("""  A shepherd boy in a village used to take his herd of sheep across the fields near the forest. He felt this job was very dull and wanted to have some fun. One day while grazing the sheep, he shouted, "Wolf! Wolf! The wolf is carrying away a lamb!" Farmers working in the nearby fields came running for help but didn’t find any wolf. The boy laughed and replied, "It was just fun. There is no wolf here".

The boy played a similar trick repeatedly for many days. After some days, while the shepherd boy was in the field with the herd of sheep, suddenly, a wolf came out from the nearby forest and attacked one of the lambs. The boy was frightened and cried loudly, "Wolf! Wolf! The wolf is carrying a lamb away!" The farmers thought the boy was playing mischief again. So, no one paid attention to him and didn’t come to his help.  """)

print(qapair)
#
