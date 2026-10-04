# meine_app_git_actions

## Was macht das Projekt?
Dieses Python-Projekt bietet Funktionen für Addition, Subtraktion, Multiplikation und Prozentberechnung. Eine Githaub-Actions Pipeline überprüft die Funktionen mit automatisierten Tests und erstellt eine ZIP-Datei (app.zip). Bei Änderungen im Hauptbranch main wird ein Release veröffentlicht.

## Pipeline im Überblick
1. test läuft zuerst: Richtet Python ein, installiert Abhängigkeiten, führt Tests aus und erstellt das ZIP-Paket als Artefakt.
2. deploy läuft nach erfolgreichem test, nur bei einem Push auf main: Lädt das Paket herunter und veröffentlicht es als GitHub-Release.
Bei Pull Requests läuft nur test. Bei fehlgeschlagenen Tests wird deploy übersprungen.
## Trigger
Push auf main: Startet test und danach bei Erfolg deploy.
Pull Request auf jeden Zielbranch: Beim Öffnen, erneuten Öffnen oder bei neuen Commits startet nur test.
Push auf andere Branches: Löst allein keinen Lauf aus.
Manuelle oder zeitgesteuerte Starts sind nicht konfiguriert.
## Secrets und Environment
Welche Secrets und Variablen werden verwendet (nur Namen, niemals Werte!)?
Secret: DEPLOY_TOKEN
Token: github.token, verwendet als GH_TOKEN
Eigene Variablen: PYTHON_VERSION, APP_ENV, DEPLOY_TOKEN, GH_TOKEN
GitHub-Variablen: GITHUB_OUTPUT, GITHUB_REPOSITORY, GITHUB_REF_NAME, GITHUB_EVENT_NAME, RUNNER_OS, GITHUB_SHA

Welche Umgebung mit welcher Schutzregel?
Die Umgebung heißt production. Deployment läuft nur nach erfolgreichen Tests bei einem Push auf main.

## Deployment
Was passiert beim Deployment, wie prüfe ich es (z. B. Releases-Seite)?
Dloyment-Job veröffentlicht ein GitHub-Release mit dem Tag v1.0.<Laufnummer> und hängt app.zip an.
Unter Releases müssen Tag und Commit zum Pipeline-Lauf passen.

Unter Assets muss app.zip verfügbar sein und den Anwendungscode enthalten.

## Lokal ausführen
Setup, Tests, Build – als Befehlsliste.

python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m pytest -v
mkdir -p build
python -m zipfile -c build/app.zip src/
python -m zipfile -l build/app.zip
deactivate