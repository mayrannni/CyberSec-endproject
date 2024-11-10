#==================================================
#function to check the use of computer resources :D
#==================================================

function Get-PCInformation {

    <#

    .synopsis
    Script to check detailed information about the use of computer resources.

    .description
    This script gives you a review about the usage of differents resources such as Memory, Disk, CPU and Network.
    With this script you can monitor the use of your computer in different aspects.

    .example
    PS C:\Users\PCName> Get-PCInformation
    With this example you can access the module.

    .inputs
    This script contains a function that does not require input parameters.
    Just select an option from menu!

    .outputs
    This script shows you in terminal any results before execute it.

    .notes
    Version 1.0
    Authors: Estrella D., Fernanda R.
    Created 07/09/2024

    #>

    function Add-ContentToHtml {
        param (
            [string]$HtmlFilePath = "$PSScriptRoot\ps-reports\Get-PCInformation.html",
            [string]$Title,
            [string]$Subtitle,
            [switch]$Timestamp,
            [string[]]$Lines = @(),
            [PSObject[]]$Table
        )

        # html base structure
        if (-not (Test-Path -Path $HtmlFilePath)) {
            "<!DOCTYPE html>
            <html lang='en'>
            <head>
                <meta charset='UTF-8'>
                <title>Computer Resources</title>
                <style>
                    body { font-family: sans-serif; margin: 20px; }
                    h1 { color: #af4c72; text-align: center; }
                    h2 { color: #6b2e45; margin-top: 20px; }
                    p { margin: 5px 0; }
                    table { width: 100%; border-collapse: collapse; margin-top: 10px; }
                    th, td { padding: 6px 10px; border: 2px solid #dbccd2; text-align: left; }
                    th { background-color: #e8acc3; color: black; }
                    .timestamp { color: #63575e; font-size: 14px; margin-top: 2px; }
                </style>
            </head>
            <body>
                <h1>Get-PCInformation Generated Report</h1>
            </body>
            </html>" | Out-File -FilePath $HtmlFilePath -Encoding UTF8
        }

        # adding content
        $content = ""


        if ($Title) {
            $content += "<h2>$Title</h2>"
        }

        if ($Timestamp -eq $True) {
            $datetime = (Get-Date).ToString("yyyy-MM-dd HH:mm:ss")
            $content += "<p class='timestamp'>Added: $datetime</p>"
        }

        if ($Subtitle) {
            $content += "<h3>$Subtitle</h3>"
        }

        if ($Lines.Count -gt 0) {
            foreach ($ln in $Lines) {
                $content += "<p>$ln</p>"
            }
        }

        if ($Table) {
            $content += "<table><tr>"

            foreach ($element in $Table[0].PSObject.Properties.Name) {
                $content += "<th>$element</th>"
            }
            $content += "</tr>"

            foreach ($row in $Table) {
                $content += "<tr>"
                foreach ($element in $row.PSObject.Properties) {
                    $content += "<td>$($element.Value)</td>"
                }
                $content += "</tr>"
            }
            $content += "</table>"
        }

        (Get-Content -Path $HtmlFilePath -Raw) -replace '</body>', "$content</body>" | 
            Set-Content -Path $HtmlFilePath -Encoding UTF8
    }



    Write-Host "Hi! there is a function to check the use of computer resources."
    do {

        Write-Host -ForegroundColor Magenta "--------------------------------------"
        Write-Host "Select a computer resource"
        Write-Host "1. Memory"
        Write-Host "2. Disk"
        Write-Host "3. CPU"
        Write-Host "4. Network"
        Write-Host "0. Exit"
        Write-Host -ForegroundColor Magenta "--------------------------------------"

        $userChoice = Read-Host ">> Your choice"

        switch ($userChoice) {
            1 {
                Add-ContentToHtml -Title "Computer resource: Memory" -Timestamp

                #returns the info in bytes, converts to mb
                Add-ContentToHtml -Subtitle "Process memory usage"
                $GetMemoryUsage = Get-Process | Sort-Object WorkingSet -Descending | Select-Object @{Name = "Process"; Expression = {$_.Name}}, `
                @{Name = "Memory (MB)"; Expression = {[math]::round($_.WorkingSet / 1MB, 1)}}

                Add-ContentToHtml -Table $GetMemoryUsage

                #Common Information Model (kilobytes), converts to gb
                $osInfo = Get-CimInstance -ClassName Win32_OperatingSystem
                $totalMem = [math]::round(($osInfo.TotalVisibleMemorySize / 1MB), 2)
                $freeMem = [math]::round(($osInfo.FreePhysicalMemory / 1MB), 2)
                $usedMem = ($totalMem - $freeMem)

                Add-ContentToHtml -Subtitle "System memory details"
                Add-ContentToHtml -Lines @(
                    "Total memory system: $totalMem GB"
                    "Free memory system: $freeMem GB"
                    "Total used memory system: $usedMem GB"
                )
            }

            2 {
                Add-ContentToHtml -Title "Computer resource: Disk" -Timestamp
                Add-ContentToHtml -Subtitle "System disk details"
                
                $GetDiskInfo = Get-CimInstance -ClassName Win32_LogicalDisk | Select-Object @{Name = "Disk drive"; Expression = {$_.DeviceID}}, `
                @{Name = "Size (GB)";Expression = {[math]::round($_.Size/1GB, 2)}}, @{Name = "FreeSpace (GB)"; `
                Expression={[math]::round($_.FreeSpace/1GB, 2)}}

                Add-ContentToHtml -Table $GetDiskInfo
            }

            3 {
                Add-ContentToHtml -Title "Computer resource: CPU" -Timestamp
                Add-ContentToHtml -Subtitle "System processor usage (total)"
                
                $GetCPUInfo = Get-CimInstance -ClassName Win32_Processor | Select-Object @{Name = "Processor Name"; Expression = {$_.Name}}, `
                @{Name = "CPU usage (%)"; Expression={[math]::round($_.LoadPercentage, 2)}}

                Add-ContentToHtml -Table $GetCPUInfo

                Add-ContentToHtml -Subtitle "CPU uptime per process"
                #'CPU' property: cpu time consumed by each process in seconds
                $CPUTimeConsumed = Get-Process | Select-Object @{Name = "Process"; Expression = {$_.Name}}, @{Name="CPU Time (sec)"; Expression={[math]::round($_.CPU, 2)}}
                
                Add-ContentToHtml -Table $CPUTimeConsumed
            }

            4 {
                Add-ContentToHtml -Title "Computer resource: Network" -Timestamp
                Add-ContentToHtml -Subtitle "Received and sent bytes per net adapter"
                $NetAdapterStats = Get-NetAdapterStatistics | Select-Object @{Name = "NetAdapter"; Expression = {$_.Name}}, ReceivedBytes, SentBytes

                Add-ContentToHtml -Table $NetAdapterStats

                Add-ContentToHtml -Subtitle "Detailed info about net adapters"
                $NetAdapterInfo = Get-NetAdapter | Select-Object @{Name = "NetAdapter"; Expression = {$_.Name}}, DriverName, DriverDescription, Status, `
                @{Name = "DataTransfer Speed"; Expression = {$_.LinkSpeed}}

                Add-ContentToHtml -Table $NetAdapterInfo
            }

            0 {
                Write-Host -ForegroundColor DarkCyan "Finishing checking your pc resources..."
                return
            }

            default {
                Write-Host -ForegroundColor Red "Sorry you must select one of the options indicated."
            }
        }
    
    } while ($userChoice -ne 0)
}

Export-ModuleMember -Function Get-PCInformation
