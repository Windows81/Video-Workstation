[CmdletBinding()]
param (
	[Parameter(Mandatory = 1)]
	#[String]
	$url,
	[Parameter(Mandatory = 1)]
	[String]
	$pn,
	[Parameter()]
	[String]
	$vf = '22/136/311/bestvideo/b',
	[Parameter()]
	[String]
	$af = 'bestaudio/b',
	[Parameter()]
	[String[]]
	$others
)
$pf = $PSScriptRoot
if ($pn -eq "test") {
	rm -Recurse "$pf/$pn" -ErrorAction Ignore
}
mkdir "$pf/$pn" -ErrorAction Ignore > $null
yt-dlp -o "subtitle:$pf/$pn/.srt" --no-download --write-subs --write-auto-subs --convert-subs srt $url
yt-dlp -f $vf -o "$pf/$pn/.v.%(ext)s" $url
yt-dlp -f $af -o "$pf/$pn/.a.%(ext)s" $url
$ext_v = (Get-ChildItem "$pf/$pn/.v.*")[0].Name.Substring(1)
$ext_a = (Get-ChildItem "$pf/$pn/.a.*")[0].Name.Substring(1)
py "$pf/Reverse.py" $pn $ext_v $ext_a @others
