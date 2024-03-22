from pytube import YouTube

def download_video(url: str):
    video = YouTube(url)
    video = video.streams.filter(progressive=True, file_extension='mp4')
    video = video.order_by('resolution').desc().first()
    video.download()

if __name__ == '__main__':
    video_urls = []
    ARRAY_SIZE = len(video_urls)
    COUNT = 1

    for video_url in video_urls:
        print('Baixando vídeo ' + str(COUNT) + ' de ' + str(ARRAY_SIZE) + '...')
        download_video(video_url)
        COUNT += 1
    print('Downloads concluídos!')
