import ssl
import certifi
import urllib.request

ssl_context = ssl.create_default_context(cafile=certifi.where())

# Use the ssl_context with urllib
opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=ssl_context))
urllib.request.install_opener(opener)

# Now load the dataset using seaborn
import seaborn as sns

tips = sns.load_dataset('tips')
print(tips)
