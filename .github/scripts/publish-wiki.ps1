# ==============================================================================
# OWASP TriSuElla — GitHub Wiki Publisher (PowerShell)
# Publishes wiki documentation to both target GitHub Wiki repositories
# ==============================================================================

param (
    [string]$Target = "both" # "both", "owasp", or "origin"
)

$ErrorActionPreference = "Continue"
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$ProjectRoot = Split-Path -Parent $ScriptDir
$WikiSourceDir = Join-Path $ProjectRoot "wiki"

$WikiRemotes = @{
    "origin" = "https://github.com/thundel/TriSuElla-AIDLCA-Framework.wiki.git"
    "owasp"  = "https://github.com/OWASP/TriSuElla-AIDLCA-Framework.wiki.git"
}

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  OWASP TriSuElla GitHub Wiki Publisher v3.4.0" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "Source Wiki Directory: $WikiSourceDir"

if (-not (Test-Path $WikiSourceDir)) {
    Write-Error "Wiki directory not found at $WikiSourceDir"
}

function Publish-To-Wiki {
    param (
        [string]$Name,
        [string]$Url
    )

    Write-Host "`n[*] Processing remote: $Name ($Url)..." -ForegroundColor Yellow

    # Test if remote wiki repo is provisioned on GitHub
    $null = & git ls-remote $Url 2>$null
    if ($LASTEXITCODE -ne 0) {
        Write-Host "[-] Wiki repository is not yet initialized on GitHub for $Name." -ForegroundColor Magenta
        Write-Host "    GitHub creates the .wiki.git repository only after the first page is created."
        Write-Host "    Action required: Visit $($Url.Replace('.wiki.git', '/wiki')) and click 'Create the first page'." -ForegroundColor Cyan
        return
    }

    $TempDir = Join-Path $ProjectRoot "scratch\wiki-publish-$Name"
    if (Test-Path $TempDir) {
        Remove-Item -Recurse -Force $TempDir
    }

    try {
        Write-Host "[+] Cloning wiki repository..." -ForegroundColor Green
        & git clone $Url $TempDir
        if ($LASTEXITCODE -ne 0) {
            Write-Warning "Clone failed. Retrying with shallow clone..."
            & git clone --depth 1 $Url $TempDir
        }

        Write-Host "[+] Copying wiki markdown files..." -ForegroundColor Green
        Copy-Item -Path "$WikiSourceDir\*" -Destination $TempDir -Recurse -Force

        Push-Location $TempDir
        & git config user.name "Bhaskar Puppala (PATEL)"
        & git config user.email "bhaskar@trisuella.org"
        & git add .
        $status = & git status --porcelain
        if (-not $status) {
            Write-Host "[OK] Wiki for $Name is already up to date." -ForegroundColor Green
        } else {
            & git commit -m "docs(wiki): update TriSuElla-AIDLCA-Framework v3.4.0 documentation suite"
            Write-Host "[+] Pushing to GitHub Wiki ($Name)..." -ForegroundColor Green
            & git push origin HEAD
            Write-Host "[OK] Successfully published wiki to $Name!" -ForegroundColor Green
        }
    }
    finally {
        Pop-Location
        if (Test-Path $TempDir) {
            Remove-Item -Recurse -Force $TempDir -ErrorAction SilentlyContinue
        }
    }
}

if ($Target -eq "both" -or $Target -eq "origin") {
    Publish-To-Wiki -Name "origin" -Url $WikiRemotes["origin"]
}

if ($Target -eq "both" -or $Target -eq "owasp") {
    Publish-To-Wiki -Name "owasp" -Url $WikiRemotes["owasp"]
}

Write-Host "`n[OK] Finished wiki publishing process." -ForegroundColor Cyan
