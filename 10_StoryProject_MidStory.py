name : str = input('Enter the name of Hero (e.g. Safdar):')
age: str = input ("Enter the age of Hero (e.g. 22):")
likes : list[str] = input('Enter his/her likes (e.g. [\'cooking\',\'swiming\'])')
achievement : str = input('Enter his/her Great Achivements (e.g. Won a race alone)')
now : str = input('Enter his/her current position (e.g. he is serving in army)')
end: str = input ('Enter the end of story (e.g. now he is enjoying his/her retirement)')

story : str = f""" 
Once upon a time, there was a smart man, his name was {name},
and {age} years old his likes to {likes} and he has greate
achivements like {achievement}. Now {now} and at last, {end}
"""

print(story)