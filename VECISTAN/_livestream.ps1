$p = Join-Path $PSScriptRoot BackgroundLoop "_.concat"
$a = Join-Path $PSScriptRoot HUM.mp3
$f = @"
[0:v]scale=1920:1080[0_v];
[0_v][1:v]overlay=alpha=premultiplied,chromashift=cbh=7,eq=1:0:1.417,boxblur=cr=5:lr=0;
[0:a][2:a]amix=duration=shortest:normalize=false:dropout_transition=666:weights=1 0.37
"@

Start-Process -WorkingDirectory "C:\Program Files\mediamtx\"  "C:\Program Files\mediamtx\mediamtx.exe" -NoNewWindow
Start-Sleep 5
ffmpeg -stream_loop -1 -re -thread_queue_size 2097152 -rtmp_live live -i rtmp://localhost:1935/_ -stream_loop -1 -f concat -i $p -thread_queue_size 128 -stream_loop -1 -i $a -vb 2300k -maxrate 2300k -minrate 2300k -bufsize 2300k -ab 128k -ar 44100 -acodec aac -vcodec libx264 -preset medium -threads 4 -f flv -filter_complex $f $args[0]
Stop-Process -Name mediamtx