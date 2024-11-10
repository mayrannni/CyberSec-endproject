#======================================
#function that displays hidden files :D
#======================================

function Show-HiddenFiles {

    <#

    .synopsis
    Script that displays a list of hidden files.

    .description
    This script shows you all existing hidden files in a given folder path.
    Use a function called Show-HiddenFiles.

    .parameter FolderPath
    This is the path to the folder (it contains hidden files).

    .example
    PS C:\Users\PCName> Show-HiddenFiles -FolderPath "C:\this\is\the\folder\path"
    With this example you can access the module.

    .inputs
    This script requires the $FolderPath parameter to show the information.

    .outputs
    This script shows you in terminal any results before execute it.

    .notes
    Version 1.0
    Authors: Estrella D., Fernanda R.
    Created 07/09/2024

    #>

    param (
        [Parameter(Mandatory=$true)][string]$FolderPath
    )

    function Log-Message {
        param (
            [string]$Message,
            [string]$Level = "INFO"
        )
        $datetime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        $logmsg = "$datetime >> $level, MESSAGE: $Message"
        $ReportLog = "$PSScriptRoot\ps-reports\Show-HiddenFiles.log"
        $logmsg | Out-File -FilePath $ReportLog -Append
    }

    Log-Message -Message "Starting Show-HiddenFiles script"
    Log-Message -Message "Receiving input parameters..."

    try {
        Log-Message -Message "Checking if the given path exists"
        if (-Not(Test-Path -Path $FolderPath)) {
            Log-Message -Message "Please select a path that does exist" -Level "ERROR"
            Write-Host -ForegroundColor Red "The folder path $FolderPath was not found."
            return
        }
        
        #check the hidden files and save them in $HiddenFiles
        Log-Message -Message "Searching for hidden files in the folder"
        $HiddenFiles = Get-ChildItem -Path $FolderPath -Hidden -Recurse

        if ($HiddenFiles.Count -eq 0){
            #validates that the folder contains hidden files
            Log-Message -Message "Please select a folder with files" -Level "ERROR"
            Write-Host -ForegroundColor Red "There are no hidden files in $FolderPath."
        } else {
            #obtains the info from hidden files
            "Information about hidden files" | Out-File "$PSScriptRoot\ps-reports\Results-HiddenFiles.txt"
            $HiddenFiles | Select-Object -Property @{Name = "HiddenFile"; Expression = {$_.Name}}, 
            LastAccessTime, LastWriteTime, @{Name = "Length (Bytes)"; Expression = {$_.Length}}, 
            Mode, IsReadOnly | Format-Table -AutoSize >> "$PSScriptRoot\ps-reports\Results-HiddenFiles.txt"
            Log-Message -Message "The file is located at $PSScriptRoot\ps-reports\Results-HiddenFiles.txt"
        }

    } catch {
        #catch any unexpected errors
        Log-Message -Message "An unexpected error has ocurred" -Level "ERROR"
        Write-Host -ForegroundColor Red "Something went wrong..." $($_.Exception.Message)
    }
}

#call the function
sShow-HiddenFiles