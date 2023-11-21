# Original File Input name
$directory = Read-Host -Prompt 'Enter the directory'
$files = Get-ChildItem -Path $directory
$input = $files | Out-GridView -Title "Select a file" -PassThru

# Extract the base name without the extension.
$basename = [System.IO.Path]::GetFileNameWithoutExtension($input)

# Construct the new attributes string.
$attributes = "2K_HEVC"

# Construct the output filename with new attributes and extension.
$output = "$basename" + "_" + "$attributes" + "_" + "powershell" + ".mp4"

# Construct the output path with directory, filename and extension.
$outputPath = "C:\Users\gangs\Videos\ffmpeg_powershell\" + $output

# FFMPEG command to process the video.
ffmpeg -i "`"$($input.FullName)`"" -c:v hevc_nvenc -cq 28 -preset medium -vf "scale=2560:1440" "`"$outputPath`""


# Output the file name to the console (optional).
Write-Host "Output file is: $outputPath"

Write-Host "input is $($input.FullName)"

pause
