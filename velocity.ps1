$c=0;$t=6;$l=((1..60)|%{"tanh($($t-1)*(T-$(($t*$_)-2*(++$c)+1)))"})-join '+'
ffmpeg -i C:\Users\USERNAME\Videos\OBS\20211127T235730.mp4 -an -vf "setpts=(PTS-STARTPTS+($l+$c)/TB)/$t" -vsync cfr -y videos/test.mp4 && sleep 1 && ffplay videos/test.mp4
