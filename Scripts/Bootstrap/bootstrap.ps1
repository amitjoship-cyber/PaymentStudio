# ===================================================================
# Payment Studio Bootstrap
# Version : 0.1.0-alpha
# Author  : Payment Studio
# ===================================================================

$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path

Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "     PAYMENT STUDIO BOOTSTRAP"
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""

$Folders = @(
    ".github",
    ".github\workflows",
    ".vscode",

    "App",
    "App\core",
    "App\Modules",
    "App\Modules\Repository",
    "App\Modules\Explorer",
    "App\Modules\Generator",
    "App\Modules\Validator",
    "App\Modules\Comparison",
    "App\Modules\AI",
    "App\Modules\Reporting",
    "App\Shared",
    "App\UI",
    "App\Database",
    "App\Config",
    "App\Assets",

    "Repository",
    "Repository\ISO20022",
    "Repository\ISO20022\ACMT",
    "Repository\ISO20022\ADMI",
    "Repository\ISO20022\AUTH",
    "Repository\ISO20022\CAMT",
    "Repository\ISO20022\HEAD",
    "Repository\ISO20022\PACS",
    "Repository\ISO20022\PAIN",
    "Repository\ISO20022\REDA",
    "Repository\ISO20022\SEEV",
    "Repository\ISO20022\SEMT",
    "Repository\ISO20022\SESE",
    "Repository\ISO20022\TSIN",
    "Repository\ISO20022\XSD",

    "Repository\CBPR",
    "Repository\MT",
    "Repository\NPCI",
    "Repository\SEPA",
    "Repository\UPI",
    "Repository\Custom",

    "Documentation",
    "Documentation\Architecture",
    "Documentation\UserGuide",
    "Documentation\DeveloperGuide",
    "Documentation\API",
    "Documentation\Images",
    "Documentation\Decisions",

    "Database",
    "Config",
    "Cache",
    "Exports",
    "Logs",
    "Reports",
    "Scripts",
    "Scripts\Bootstrap",
    "Templates",
    "Tests",
    "Tools"
)

foreach($Folder in $Folders)
{
    $Path = Join-Path $ProjectRoot $Folder

    if(!(Test-Path $Path))
    {
        New-Item -ItemType Directory -Path $Path | Out-Null
        Write-Host "[CREATED] $Folder" -ForegroundColor Green
    }
    else
    {
        Write-Host "[EXISTS ] $Folder" -ForegroundColor Yellow
    }

    $GitKeep = Join-Path $Path ".gitkeep"

    if(!(Test-Path $GitKeep))
    {
        New-Item -ItemType File -Path $GitKeep | Out-Null
    }
}

$Files = @(
    "README.md",
    "CHANGELOG.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "ROADMAP.md",
    "PROJECT_CHARTER.md",
    "ARCHITECTURE.md",
    "DECISIONS.md",
    ".gitignore",
    "requirements.txt",
    "pyproject.toml"
)

foreach($File in $Files)
{
    $FilePath = Join-Path $ProjectRoot $File

    if(!(Test-Path $FilePath))
    {
        New-Item -ItemType File -Path $FilePath | Out-Null
        Write-Host "[FILE   ] $File" -ForegroundColor Cyan
    }
}

Write-Host ""
Write-Host "==========================================" -ForegroundColor Green
Write-Host " Payment Studio Structure Created"
Write-Host "==========================================" -ForegroundColor Green