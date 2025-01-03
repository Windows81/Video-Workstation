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
yt-dlp $url -f $vf -o "$pf/$pn/.v.`"%%(ext)s`"" # Pyenv forwards its commands to `.bat` shims for windows, so we must escape `"%%(ext)s`".
yt-dlp $url -f $af -o "$pf/$pn/.a.`"%%(ext)s`""
$ext_v = (Get-ChildItem "$pf/$pn/.v.*")[0].Name.Substring(1)
$ext_a = (Get-ChildItem "$pf/$pn/.a.*")[0].Name.Substring(1)
python "$pf/Reverse.py" $pn $ext_v $ext_a @others
