# url2png
### Get a screenshot of a url or many screenshots from a file contining urls.

Generate a screenshot of a single url:
```
python url2png.py -u xenome.io -o outfile.png

```

Generate screenshots from a list of urls:
```
python url2png.py -f infile.txt
```
Images generated from a file will be created in the same directory as the script and named with the pattern `{url}.png`
