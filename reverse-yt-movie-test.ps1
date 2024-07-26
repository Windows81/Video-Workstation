rm $PSScriptRoot\test -Force -Recurse -ErrorAction Ignore
$new_args = @($args[0], 'test') + $args[1..666]
. "$PSScriptRoot\reverse-yt-movie.ps1" @new_args
