import os
import openai
import ast
import random
import replicate


openai.api_key = open("apikey.txt","r").read()
## for setting replicate's api token os.environ["REPLICATE_API_TOKEN"] =

songTheme = generateStuff("Write the theme of a new, unique, never head before, particular song", .5, 4000)
songTitle = generateStuff("Write the title of a song which is about: "+songTheme,.5, 20)
songMood = generateStuff("Write the mood of a song about: " +songTheme,.5, 30)
songVideo = generateStuff("Write the type of video for a song about: " + songTheme,.5, 30)
songBPM = random.randint(60,240)
songIntroDuration = random.randint(1,30)
songOutroDuration = random.randint(1,30)
firstVerse = generateStuff("Write the first verse for a song about: " + songTheme,.5, 50)
songLyrics = firstVerse
secondVerse = generateStuff("Write the second verse for a song about: " + songTheme + " that has this first verse: " + firstVerse,.5, 60)
songLyrics += secondVerse
firstChorus = generateStuff("Write the first chorus for a song about: " + songTheme + " that has this second verse: " + secondVerse,.5, 60)
songLyrics += firstChorus
thirdVerse = generateStuff("Write the third verse for a song about: " + songTheme + " that has this second verse: " + secondVerse,.5, 60)
songLyrics += thirdVerse
fourthVerse = generateStuff("Write the fourth verse for a song about: " + songTheme + " that has this third verse: " + thirdVerse,.5, 60)
songLyrics += fourthVerse
secondChorus = generateStuff("Write the second chorus for a song about: " + songTheme + " that has this first chorus: " + firstChorus,.5, 60)
songLyrics += secondChorus
bridge = generateStuff("Write the bridge for a song about: " + songTheme + " that has these lyrics: " + songLyrics,.5, 60)
songLyrics += bridge
finalChorus = generateStuff("Write the final chorus for a song about: " + songTheme + " that has this second chorus: " + secondChorus,.5, 60)
songLyrics += finalChorus
verses = songLyrics.split("\n")

model = replicate.models.get("andreasjansson/stable-diffusion-animation")

output = model.predict(prompt_start=verses[0],prompt_end=verses[1],width=512,height=512,num_inference_steps=50,prompt_strength=0.9,num_animation_frames=25,num_interpolation_steps=25,output_format="mp4")


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
    print(response)
    try:
        result = ast.literal_eval(response["choices"][0]["text"].strip())
        result = result.replace("\\n", "\n")
    except:
        result = response["choices"][0]["text"].strip()
    return result

