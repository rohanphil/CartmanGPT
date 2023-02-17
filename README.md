Fun Side project to fine tune a gpt model to respond to prompts in the voice of Eric Cartman. No clue how far I will get with this. I guess we'll see.

Update: I took a lot of inspiration from this very informative tutorial on generating a bot that was capable of discourse. https://towardsdatascience.com/make-your-own-rick-sanchez-bot-with-transformers-and-dialogpt-fine-tuning-f85e6d1f4e30
Although, I did change up a few things here and there. On my dataset, it took around 2.5 hours to train on Google Colab. (EDIT: I made large scale changes to the data collection to now only use Cartman's lines as the responses. While this did go a long way towards reducing the compute required, it did considerably hamper the size of the training set. If anyone has any South Park fan fiction or links to seasons 8-26, please let me know.)

The code itself lives in the ipynb checkpoint folder for some reason (It is rescued now). You can generate the dataset by running the ScriptEx.py file. While the training procedure is rather verbose, it is actually quite simple if you stare at it long enough. 

PSA: Eric Cartman is a horrible child, and a Chatbot made to immitate him is also bound to be incredibly rude. Proceed at your own caution.

There is now a WebApp that can be used once the model is trained and saved in the output-small folder.

![image](https://user-images.githubusercontent.com/44194916/219517883-0ec10ade-98c2-4037-8280-3106aa8996e5.png)
