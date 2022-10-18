ffplay @args -hide_banner 2>&1 | tail -n 2 | grep -Eo "[0-9\.]+" | head -n 1
