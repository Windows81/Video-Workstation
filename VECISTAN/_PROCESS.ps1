$p = Join-Path $PSScriptRoot VECISTAN "Untitled%08d.tif"
$a = Join-Path $PSScriptRoot VECISTAN HUM.mp3
$f = @"
[0:v]scale=1920:1080[0_v];
[0_v][1:v]overlay=alpha=premultiplied:shortest=1,chromashift=cbh=7,eq=1:0:1.417,boxblur=cr=5:lr=0;
[0:a][2:a]amix=duration=shortest:normalize=false:dropout_transition=666:weights=1 0.37
"@
echo $a
ffmpeg -i $args[0] -loop 1 -i $p -stream_loop -1 -i $a -filter_complex $f $args[1] -y