#=============================================
#function to show info about latest logins :D
#=============================================

function Show-LogsLogin {

    <#
    .synopsis
    Script that checks if logins on a device were successful.

    .description
    The script lists the logins depending on the number of sessions given by the user.
    The admin permissions are required in order to get results.

    .example
    PS C:\Users\PCName> Get-PCInformation -numLogins 3
    With this example the function shows you the information about 3 recents access sessions.

    .inputs
    TThis script requires the $numLogins parameter to know how many recent logins to display.

    .outputs
    This script shows you in terminal any results before execute it.

    .notes
    Version 1.0
    Authors: Estrella D., Fernanda R.
    Created 07/09/2024
    - Lines 28 to 39 based on https://github.com/Bert-JanP/Incident-Response-Powershell/blob/3d91389447d02b481e65675daeb5f49a1f1393e6/Scripts/LastLogons.ps1
    #>

    param(
        [Parameter(Mandatory=$true)][int]$numLogins
    )

    function Log-Message {
        param (
            [string]$Message,
            [string]$Level = "INFO"
        )
        $datetime = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
        $logmsg = "$datetime >> $level, MESSAGE: $Message"
        $ReportLog = "$PSScriptRoot\ps-reports\Show-LogsLogin.log"
        $logmsg | Out-File -FilePath $ReportLog -Append
    }

    Log-Message -Message "Starting Show-LogsLogin script"
    Log-Message -Message "Receiving input parameters..."

    try {
        #get $numLogins of security logs and filter them by ID
        Log-Message -Message "Searching for system logins"
        $AccessSessions = Get-WinEvent -LogName 'Security' -FilterXPath "*[System[EventID = 4624 or EventID = 4648]]" `
        | Select-Object -First $numLogins

        #extract the info for earch login and prints it
        Log-Message -Message "Searching for information about each of the sessions"
        foreach ($session in $AccessSessions) {
            $date = $session.TimeCreated
            $message = $session.Message
            $SessionType = if ($session.Id -eq 4648) {"Explicit"} else {"Interactive"}

            ">> Date (Time created): $date" | Out-File "$PSScriptRoot\ps-reports\Show-LogsLogins.txt"
            ">> Session Type: $SessionType" >> "$PSScriptRoot\ps-reports\Show-LogsLogins.txt"
            ">> Message." >> "$PSScriptRoot\ps-reports\Show-LogsLogins.txt"
            "$message" >> "$PSScriptRoot\ps-reports\Show-LogsLogins.txt"
            }

        Log-Message -Message "The analysis has been carried out successfully"
        Log-Message -Message "Your file has been created in $PSScriptRoot\ps-reports\Show-LogsLogins.txt"
        
        } catch {
        #checks for administrator permissions by identify the users role
        if (-not ([Security.Principal.WindowsPrincipal] [Security.Principal.WindowsIdentity]::`
        GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole] "Administrator")) {
            Write-Host -ForegroundColor Green "Enables administrator permissions."
            Log-Message -Message "You do not have administrator permissions." -Level "ERROR"
        }
    }
}

#calling
Show-LogsLogin
