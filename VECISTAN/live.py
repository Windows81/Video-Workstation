import ffmpeg

stream = ffmpeg.InputNode(
    ffmpeg.input.__name__,
    args=['re'],
    kwargs={
        'stream_loop': -1,
        'thread_queue_size': 32,
        'filename': 'rtmp://localhost:1935/_'
    }).stream()
background = ffmpeg.input('./BackgroundLoop/_.concat', f='concat')
_0v = ffmpeg.filter(stream, 'scale', '1920:1080')
ffmpeg.overlay(_0v, background)
