[CmdletBinding()]
param (
	[Parameter(Mandatory = 1)]
	[String]
	$url,
	[Parameter(Mandatory = 1)]
	[String]
	$pn
)
$pf = $PSScriptRoot
if ($pn -eq "test") {
	rm -Recurse "$pf/$pn" -ErrorAction Ignore
}
mkdir "$pf/$pn" -ErrorAction Ignore > $null
ffmpeg -v error -stats -i $url -c copy -an "$pf/$pn/.v.mp4" -vn "$pf/$pn/.a.mp3"
py "$pf/Reverse.py" $pn "v.mp4" "a.mp3"
