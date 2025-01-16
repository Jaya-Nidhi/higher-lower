from flask import Flask
import random
number =  random.randint(0,9)
print(number)

app = Flask(__name__)

@app.route('/')
def game():
    return '<h1 style="text-align:center">Guess the number between 0 and 9<h1>'\
    '<img src="https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGp4Ymh2b2k4eGk5aDlmanNkZmRyNnVnMjh5bGxpNmNvd2JsYzVnYiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VE4InmieSgVqM/giphy.gif" width=300>'

@app.route('/<int:guess>')
def guess_number(guess):

  if guess==number:
      return '<h1>You guess the right number!</h1>'\
      '<img src =https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif>'
  elif guess > number:
      return '<h1>Your guess is too high, try again</h1>' \
             '<img src =https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif>'
  else:
      return '<h1>You guess is too low try again</h1>' \
             '<img src =https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif>'

if __name__=="__main__":
      app.run(debug=True)