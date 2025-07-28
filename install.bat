@echo off
REM =================================================================
REM Script de Instalação para o projeto ARQV30 Enhanced v2.0
REM Este script configura o ambiente e instala todas as dependências.
REM =================================================================
setlocal

echo.
echo    ========================================
echo      ARQV30 Enhanced v2.0 - Instalação
echo    ========================================
echo.

REM --- Passo 1: Verificar se o Python está instalado ---
echo [1/5] A verificar a instalação do Python...
python --version >nul 2>&1
if errorlevel 1 (
    echo   [ERRO] Python nao encontrado no PATH.
    echo   Por favor, instale o Python 3.8+ a partir de python.org
    echo   e certifique-se de que marca a opcao "Add Python to PATH" durante a instalacao.
    pause
    exit /b 1
)
echo   [OK] Python encontrado:
for /f "delims=" %%i in ('python --version') do echo   %%i
echo.

REM --- Passo 2: Criar o Ambiente Virtual ---
echo [2/5] A criar o ambiente virtual na pasta 'venv'...
if not exist venv (
    python -m venv venv
    if errorlevel 1 (
        echo   [ERRO] Falha ao criar o ambiente virtual.
        pause
        exit /b 1
    )
    echo   [OK] Ambiente virtual criado com sucesso.
) else (
    echo   [INFO] A pasta 'venv' ja existe. A saltar este passo.
)
echo.

REM --- Passo 3: Ativar o Ambiente Virtual ---
echo [3/5] A ativar o ambiente virtual...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo   [ERRO] Falha ao ativar o ambiente virtual.
    pause
    exit /b 1
)
echo   [OK] Ambiente virtual ativado.
echo.

REM --- Passo 4: Atualizar o Pip ---
echo [4/5] A atualizar o gestor de pacotes (pip)...
python -m pip install --upgrade pip >nul
echo   [OK] Pip atualizado para a versao mais recente.
echo.

REM --- Passo 5: Instalar as Dependências ---
echo [5/5] A instalar todas as dependencias do ficheiro requirements.txt...
echo      Isto pode demorar alguns minutos. Por favor, aguarde.
echo.
pip install -r requirements.txt
if errorlevel 1 (
    echo   [ERRO] Falha ao instalar as dependencias.
    echo   Verifique a sua conexao com a internet e o conteudo do ficheiro requirements.txt.
    pause
    exit /b 1
)
echo.
echo   [OK] Todas as dependencias foram instaladas com sucesso!
echo.
echo    =================================================================
echo      🎉 Instalacao Concluida! O seu ambiente esta pronto.
echo    =================================================================
echo.
echo    Proximos Passos:
echo    1. Certifique-se de que o seu ficheiro .env esta preenchido com as chaves de API.
echo    2. Execute o ficheiro 'run.bat' para iniciar a aplicacao.
echo.
pause
