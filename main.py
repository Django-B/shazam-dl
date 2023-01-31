#!env/bin/python
import requests
import youtube_dl
import sys

def get_id(url: str):
    id = url.partition('track/')[2]\
            .partition('/')[0]
    return id

def get_yt_link(track_id: str):
    template_url = "https://www.shazam.com/discovery/v5/ru/RU/web/-/track/{}?shazamapiversion=v3&video=v3"
    url = template_url.format(track_id)

    res = requests.get(url)
    data = res.json()
    json_url = data['sections'][1]['youtubeurl']
    
    res = requests.get(json_url)
    yt_link = res.json()['actions'][0]['uri']

    return yt_link

'''
def download_music(link: str):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
'''

def main():
    if len(sys.argv) != 2:
        exit('not link')
    track_id = get_id(sys.argv[1])
    # url = 'https://www.shazam.com/ru/track/616490430/neon-blade'
    yt_link = get_yt_link(track_id)
    print(yt_link)
    # download_music(yt_link)

if __name__=='__main__':
    main()

