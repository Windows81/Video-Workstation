param (
	[Parameter(Mandatory=$true)]
	[string]
	$project
)

$d = Join-Path $PSScriptRoot $project
$t = Join-Path $d "$project.txt"
$v = Join-Path $d "$project.mp4"
$a = Join-Path $d "$project.mp3"
$rn = Join-Path $d "$project.r.n.mp4"
$ra = Join-Path $d "$project.r.mp4"
$root = $PSScriptRoot -Replace "\\", "/"

if(-not (Test-Path $rn)) {
	ffmpeg -i $v -f segment -vcodec copy -an -loglevel panic -reset_timestamps 1 -segment_time 69.0 -n (Join-Path $d %d.ts) # Nice.
	Set-Content $t $null
	$l = (Get-ChildItem $d -filter *.ts).length -
	(Get-ChildItem $d -filter *.r.ts).length - 1
	for ($c = $l; $c -ge 0; $c--) {
		$i = Join-Path $d $c
		Write-Output $c
		Add-Content $t "file $root/$project/$c.r.ts"
		ffmpeg -i "$i.ts" -vf reverse -q 7 -loglevel error "$i.r.ts" -n
	}
	ffmpeg -safe 0 -f concat -i $t -vcodec copy $rn
}
#ffmpeg -i $v -vn -af areverse $a -n
while(($o=read-host "Enter AV offset (q to finalise)")-ne'q'){
	ffmpeg -i $rn -itsoffset "$o" -i $a -codec copy $ra -y
	ffplay $ra -loglevel panic
}

Remove-Item $rn
Remove-Item (Join-Path $d *.ts)
Remove-Item $t