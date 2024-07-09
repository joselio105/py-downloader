from pytube import YouTube

def download_video(url: str):
    video = YouTube(url)
    video = video.streams.filter(progressive=True, file_extension='mp4')
    video = video.order_by('resolution').desc().first()
    video.download()

    # Para baixar as URLs digite na linha de comando:
    # .venv\Scripts\activate
    # python run.py

if __name__ == '__main__':
    # Lista de URLs a serem baixadas
    video_urls = [
        # 'https://www.youtube.com/live/qbZsaBMxCJI'
    ]

    ARRAY_SIZE = len(video_urls)
    COUNT = 1

    for video_url in video_urls:
        print('Baixando vídeo ' + str(COUNT) + ' de ' + str(ARRAY_SIZE) + '...')
        download_video(video_url)
        COUNT += 1
    print('Downloads concluídos!')
