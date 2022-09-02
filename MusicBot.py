import os
import openai
import ast

openai.api_key = open("apikey.txt","r").read()

songTheme = generateStuff("Write the theme of a new, unique, never head before, particular song", .5, 4000)
songTitle = generateStuff("Write the title of a song which is about: "+songTheme,.5, 20)
songMood = generateStuff("Write the mood of a song about: " +songTheme,.5, 30)
songVideo = generateStuff("Write the type of video for a song about: " + songTheme,.5, 30)

def generateStuff(inPrompt, inTemp, maxToxens):
    response = openai.Completion.create(
      engine="text-davinci-002",
      prompt=inPrompt,
      temperature=inTemp,
      max_tokens=maxToxens,
      top_p=1.0,
      frequency_penalty=0.0,
      presence_penalty=0.0
    )
    try:
        result = ast.literal_eval(response["choices"][0]["text"].strip())
        result = result.replace("\\n", "\n")
    except:
        result = response["choices"][0]["text"].strip()
    return result