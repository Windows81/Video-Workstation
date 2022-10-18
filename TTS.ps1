param([Parameter(Mandatory=$true)][string]$voice,[Parameter(Mandatory=$true)][string]$text,[Parameter(Mandatory=$true)][string]$file)
node "C:\Users\USERNAME\Documents\Projects\tts\main.js" $voice $text "$file.mp3"
ffmpeg -i "$file.mp3" -y -filter:a "volume=10dB" $file -loglevel panic
Remove-Item -Path "$file.mp3"
ffprobe $file -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 -hide_banner -loglevel panic