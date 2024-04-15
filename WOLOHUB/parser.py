import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

def parse_video_links(num_episodes):
    base_url = "https://jut.su/bookofd/episode-{}.html"
    video_links = []
    ua = UserAgent()

    for i in range(1, num_episodes + 1):
        url = base_url.format(i)
        headers = {'User-Agent': ua.random}
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            links = soup.find_all('a', id='vjs-logobrand-image-destination', href=True)
            for link in links:
                href = link['href']
                video_id_start = href.find('/')
                video_id_end = href.find('?')
                if video_id_start != -1 and video_id_end != -1:
                    video_links.append(href[video_id_start:video_id_end])
        else:
            print(f"Failed to fetch episode {i}")

    return video_links

num_episodes = int(input("Введите количество серий для парсинга: "))
video_links = parse_video_links(num_episodes)

print("Ссылки на видео:")
for link in video_links:
    print(link)
