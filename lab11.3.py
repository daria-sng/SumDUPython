import nltk
from nltk.corpus import stopwords
from nltk.probability import FreqDist
import matplotlib.pyplot as plt
import string

hamlet = nltk.corpus.gutenberg.words("shakespeare-hamlet.txt")

# Визначення кількості слів у тексті
print(f"Number of words in \"shakespeare-hamlet.txt\": {len(hamlet)}")

# Визначення 10 найбільш вживаних слів у тексті
fdist = FreqDist(hamlet)
top10 = fdist.most_common(10)
print(f"10 most used words in the text:\n{top10}")

# Побудова стовпчастої діаграми ( 10 найбільш вживаних слів у тексті )
words = [item[0] for item in top10]
frequency = [value[1] for value in top10]

fig, ax = plt.subplots()
ax.bar(words, frequency, label = "Word count", color = "#FEAE00")
fig.set_figwidth(11)
fig.set_figheight(5)

plt.title("10 most used words in the text", fontsize = 15)
plt.xlabel("Item", fontsize = 10, color = "#198280")
plt.ylabel("Frequency", fontsize = 10, color = "#1A828D")
plt.legend()

plt.show()

# Видалення стоп-слів ( з архаїчними словами ) та пунктуації з тексту
stop_words = set(word.lower() for word in stopwords.words("english"))
arch_words = {"thou", "thy", "thee", "ye"}
stop_words.update(arch_words)

withoutstop = [word for word in hamlet if word.lower() not in stop_words]

table = str.maketrans("", "", string.punctuation)
withoutpunctuation = [word.translate(table) for word in withoutstop if word.translate(table)!= ""]

# Визначення 10 найбільш вживаних слів у тексті 
fdist = FreqDist(withoutpunctuation)
top10 = fdist.most_common(10)
print(f"\n10 most used words in the text (without stop-words and punctuation):\n{top10}")

# Побудова стовпчастої діаграми ( 10 найбільш вживаних слів у тексті (без стоп-слів та пунктуації) )
words = [item[0] for item in top10]
frequency = [value[1] for value in top10]

fig, ax = plt.subplots()
ax.bar(words, frequency, label = "Word count", color = "#3AD407")
fig.set_figwidth(11)
fig.set_figheight(5)

plt.title("10 most used words in the text (without stop-words and punctuation)", fontsize = 15)
plt.xlabel("Item", fontsize = 10, color = "#191E82")
plt.ylabel("Frequency", fontsize = 10, color = "#1A1E8D")
plt.legend()

plt.show()