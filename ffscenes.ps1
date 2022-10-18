ffmpeg @args -vf scdet=11:1,metadata=mode=print:key=lavfi.scd.score:file=- -f null -loglevel 0 -|awk '!(NR%2){printf(\"%9.2f %9.2f\n\",substr(p,index(p,\"pts_time\")+9),substr($0,17))}{p=$0}'
