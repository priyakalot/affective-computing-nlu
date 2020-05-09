Steps to run:
1. `pip install rasa` (or `pip install -r requirements.txt`)
2. `cd betterlistener`
3. Every time you change nlu.md, make sure your domain.yml is up to date and then `rasa train nlu`
4. To test your model, run `rasa shell nlu` and enter some input text