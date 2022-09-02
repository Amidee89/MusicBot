import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST")) # GET: requests data from server - POST: submit data to server.
def index():
    if request.method == "POST":
        prompt_result = run_openai("text-davinci-002", default_sentence(),1).choices[0].text
        prompt = generate_prompt_lyrics(prompt_result)
        print("result:", prompt)
        response = run_openai("text-davinci-002", prompt,1)
        result = response.choices[0].text
        return redirect(url_for("index", result=result, prompt = prompt_result))

    result = request.args.get("result")
    prompt = request.args.get("prompt")
    return render_template("index.html", result=result, prompt = prompt)

def run_openai (model, prompt, temperature):
    """
    Given a prompt, the model will return one or more predicted completions,
    and can also return the probabilities of alternative tokens at each position.

    args:
        model: ID of the model to use.
        prompt: The prompt(s) to generate completions for, encoded as a string, array of strings, array of tokens, or array of token arrays.
        temperature: [0:1], bigger more creative applications, smaller for ones with a well-defined answer.
    """
    return openai.Completion.create(
            model= model,
            prompt= prompt,
            max_tokens = 128,
            temperature= temperature,
            )

def default_sentence ():
    return """ write a good idea for a song, what mood it is, the genre and bpm """

def generate_prompt_lyrics(result):
    return """Lyrics for {}""".format(result)
