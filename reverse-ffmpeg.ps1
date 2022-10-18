$pn = $args[0]
$pf = $PSScriptRoot
if ($pn -eq "test") {
	rm -Recurse "$pf/$pn" -ErrorAction Ignore
}
$args = $args[1..($args.Length-1)]
mkdir "$pf/$pn" -ErrorAction Ignore > $null
ffmpeg -v error -stats @args -an "$pf/$pn/.v.mp4" "$pf/$pn/.a.mp3"
py "$pf/Reverse.py" $pn "v.mp4" "a.mp3"
