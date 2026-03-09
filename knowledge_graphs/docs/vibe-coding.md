## Vibe-Coding manim animations

I have used github copilot with `gpt-5.3-codex` to generate around 80% of the code for this animation.
here are few observations on what worked and what didn't
 - simple prompts with vague requirements gives a gap between expected vs generated animation, so explain each scene in detail such as where objects should be placed and how they move resolved most of the problems
 - since `from manim import *` is a common pattern, copilot tries to fix unwanted linting issues, ignoring the rule in `pyproject.toml` helps
 - planning the scene for 5-10 mins before prompting helps to give clear instruction

This is my first time animating with manim and it takes less than 10 hours to make this video
[Knowledge graphs vs Vector Stores](https://youtu.be/3EFr8hdGN1k?si=9S2Ec120NV7m2RcE)

## Sample Conversation

![alt text](./img/convo1.png)
![alt text](./img/convo2.png)
![alt text](./img/convo3.png)

## Why I choose manim
There are many ways to create a animation video such as using animation softwares like blender or using a text to video gen-ai model, I picked manim because
- easy to tweak the generated animations with code changes
- once we pick a domain and style to create animations, we can create utilities to ease the process
- lightweight, the generated animation resolution is `1920*1080` but the size is just 10mb
- I want to tryout vibe coding to see the potential of state-of-the-art gen-ai models (i am impressed)
- I am a big fan of [Grant Sanderson](https://www.youtube.com/@3blue1brown) and wanted to tryout his cool tool for a long time