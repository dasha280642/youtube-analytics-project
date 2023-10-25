from src.channel import Channel
from src.channel import print_info
if __name__ == '__main__':
    channel_id = 'UC-OVMPlMA3-YCIeg4z5z23A'  # MoscowPython
    channel = Channel(channel_id)
    channel_info = channel.get_channel_info()
    print_info(channel_info)

    playlists = channel.get_playlists()
    print_info(playlists)

    playlist_id = 'PLH-XmS0lSi_zdhYvcwUfv0N88LQRt6UZn'
    playlist_videos = channel.get_playlist_videos(playlist_id)
    print(playlist_videos)

    video_id = 'gaoc9MPZ4bw'
    video_duration = channel.get_video_duration(video_id)
    print(video_duration)

    video_title, view_count, like_count, comment_count = channel.get_video_stats(video_id)
    print(video_title)
    print(view_count)
    print(like_count)
    print(comment_count)
    """
{
  "kind": "youtube#channelListResponse",
  "etag": "uAdmwT0aDhY9LmAzJzIafD6ATRw",
  "pageInfo": {
    "totalResults": 1,
    "resultsPerPage": 5
  },
  "items": [
    {
      "kind": "youtube#channel",
      "etag": "cPh7A8SKcZxxs_UPCiBaXP1wNDk",
      "id": "UC-OVMPlMA3-YCIeg4z5z23A",
      "snippet": {
        "title": "MoscowPython",
        "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)",
        "customUrl": "@moscowdjangoru",
        "publishedAt": "2012-07-13T09:48:44Z",
        "thumbnails": {
          "default": {
            "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s88-c-k-c0x00ffffff-no-rj",
            "width": 88,
            "height": 88
          },
          "medium": {
            "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s240-c-k-c0x00ffffff-no-rj",
            "width": 240,
            "height": 240
          },
          "high": {
            "url": "https://yt3.ggpht.com/ytc/AGIKgqNv2rZ6mOSuXvJLYhmTc0nd-LtI5RiDtsEBpguJXA=s800-c-k-c0x00ffffff-no-rj",
            "width": 800,
            "height": 800
          }
        },
        "localized": {
          "title": "MoscowPython",
          "description": "Видеозаписи со встреч питонистов и джангистов в Москве и не только. :)\nПрисоединяйтесь: https://www.facebook.com/groups/MoscowDjango! :)"
        },
        "country": "RU"
      },
      "statistics": {
        "viewCount": "2303120",
        "subscriberCount": "25900",
        "hiddenSubscriberCount": false,
        "videoCount": "685"
      }
    }
  ]
}

    """