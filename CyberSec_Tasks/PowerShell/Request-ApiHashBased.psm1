#==========================================
#function to query api based on the hash :D
#==========================================

function Request-ApiHashBased {

    <#

        .synopsis
        Script that request an API based on file hashes.

        .description
        This script use VirusTotal API to get information about files from a local folder.
        Use a function called Request-ApiHashBased.

        .parameter FolderPath
        This is the path to the local folder (the folder should be "popular").

        .parameter ReportPath
        This is the path to save the results in a ".txt" file.

        .parameter prints
        This parameter contains the maximum number of queries the user wants to make.
        -Maximum number of queries must be less than the number of files in the folder.

        .example
        PS C:\Users\PCName> Request-ApiHashBased -FolderPath "C:\this\is\the\folder\path" -$ReportPath "C:\this\is\the\report\path" -prints 5
        With this example you get the analysis from Virus Total of the first 5 files in $FolderPath.

        .inputs
        This script requires the $FolderPath parameter to analyze the files by hash. Also the path to save the report and the number of queries to make.

        .outputs
        This script saves the results in a text file. Review it at the end of the execution.

        .notes
        Version 1.0
        Authors: Estrella D., Fernanda R.
        Created 05/09/2024

    #>

    param (
        [string]$FolderPath,
        [string]$ReportPath = "$PSScriptRoot\ps-reports",
        [int]$prints
    )

    $FolderPath = Read-Host "Enter the folder path you want to scan"

    function Log-Message {
        param (
            [string]$Message,
            [string]$Level = "INFO"
        )

        $datetime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        $logmsg = "$datetime >> $level, MESSAGE: $Message"
        $ReportLog = Join-Path $ReportPath "Request-ApiHashBased.log"
        $logmsg | Out-File -FilePath $ReportLog -Append
    }

    Log-Message -Message "Starting Request-ApiHashBased script"
    Log-Message -Message "Receiving input parameters..."

    #saves files recursively and count them
    Log-Message -Message "Checking folder files"
    $files = Get-ChildItem -Path $FolderPath -File -Recurse
    $FilesCount = $files.Count

    if ($FilesCount -eq 0) {
        Log-Message -Message "Please select a folder with files" -Level "ERROR"
        Write-Host -ForegroundColor Red "Review Logs file for any questions."
        exit
    }

    #request the maximum number of requests to the api
    Log-Message -Message "The given folder contains $FilesCount files" -Level "WARNING"
    Write-Host -ForegroundColor DarkYellow "Notes: Folder contains $FilesCount files."
    $prints = Read-Host "Maximum number of queries to Virus Total API (max. $FilesCount)"

    #parsing $prints value and validate it
    if (-not [int]::TryParse($prints, [ref]$null) -or [int]$prints -gt $FilesCount -or [int]$prints -lt 1) {
        Log-Message -Message "Enter a valid number  that does not exceed $FilesCount and greather than 0..." -Level "ERROR"
        return
    }

    #flag for found hashes
    $flag = $false

    $LocalFiles = Get-ChildItem -Path $FolderPath -File -Recurse

    #api config
    $apiKey = "56d0f6faabfb9da4015174d17544ef665c9b0d650148dbbddb189457b81f0be7"
    $Headers = @{
    "x-apikey" = $apiKey
    "User-Agent" = "Powershell Script"
    }

    for ($i = 0; $i -lt $prints; $i++) {

        $file = $LocalFiles[$i]
        $GetHashes = $null

        try {
            $GetHashes = Get-FileHash -Path $file.FullName -Algorithm SHA256
        } catch {
            Log-Message -Message "Failed to obtain the hash of $($file.FullName)" -Level "WARNING"
            continue
        }

        $hash = $GetHashes.Hash
        $url = "https://www.virustotal.com/api/v3/files/$hash"

        if ($GetHashes -and $GetHashes.Hash) {
            try {
                Log-Message -Message "Querying Virus Total API..."
                $response = Invoke-RestMethod -Uri $url -Headers $Headers -Method Get
            } catch {
                continue
            }

            if ($response -and $response.data) {
                #if the api response is valid, flag changes to $true
                $flag = $true
                
                Log-Message -Message "File found while querying api $($file.FullName)"

                #generate the report and save it in the given path
                $ReportFile = Join-Path $ReportPath "ReportVT.txt"

                #appends each line with json compress formatting
                Log-Message -Message "Adding data to queries report..."
                $jsonres = $response | ConvertTo-Json -Compress
                "FilePath >> $($file.FullName) with Hash >> $($hash)`n>>Virus Total SCAN`n$jsonres`n"`
                | Out-File -FilePath $ReportFile -Append
            } 
        }

    }

    if (-not $flag) {
        Log-Message -Message "Try with a better-known folder please" -Level "ERROR"
    } else {
        if (Test-Path $ReportFile) {
            $ReportFileInfo = Get-Item $ReportFile
            if ($ReportFileInfo.Length -gt 0) {
                #indicates whether the report was created correctly for review it
                Log-Message -Message "Report saved in $ReportFile"
                Write-Host -ForegroundColor Magenta ">> Verify results in $ReportFile"
            }
        }
    }
}

Export-ModuleMember -Function Request-ApiHashBased
