yt-dlp -q --playlist-reverse $@ --flat-playlist --include-ads --print "%(id)s %(duration)d" 2>/dev/null | sed 's/^/https:\/\/youtu.be\//' | xargs -P 1 -r -n 1 -i sh -c "v=\$(yt-dlp {} -g -f bestaudio --no-colors); s='{}'; echo ${s% *} >&2; [ -n \"\$v\" ] && ffmpeg -i \$v -v error -stats -af areverse -hide_banner -f ogg pipe:1" | vlc -
