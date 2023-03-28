# Text to speech conversion

When your PC stops giving image but still gives sound, this is a good approach to have some files that you can listen to. It will speed up your study.

### How to make it work

Place the Python file in the same directory with your pdf that you want to convert to mp3.

Replace Pandas with your pdf name:
```python
pdfreader = PyPDF2.PdfFileReader(open('Pandas.pdf', 'rb'))
```

Replace ResidentSleeper with your mp3 desired name:
```python
speaker.save_to_file(clean_text, 'ResidentSleeper.mp3')
```

If you desire to have it save automatically to a specific folder, just use the shutil module to move the generated mp3 to your desired location.