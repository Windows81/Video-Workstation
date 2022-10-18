param (
        [Parameter(Mandatory = 1)]
        [String]
        $url,
        [Parameter()]
        [String]
        $vf = '136/22/bestvideo[ext=mp4]/bestvideo',
        [Parameter()]
        [String]
        $af = 'bestaudio'
)
rm $PSScriptRoot\test -Force -Recurse -ErrorAction Ignore
$PSScriptRoot\reverse-yt-movie.ps1 $url test $vf $af
