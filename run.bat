@echo off
REM =================================================================
REM Script de Execução para o projeto ARQV30 Enhanced v2.0
REM Ativa o ambiente virtual e inicia o servidor da aplicação.
REM =================================================================
setlocal

echo.
echo    ========================================
echo      ARQV30 Enhanced v2.0 - A Iniciar
echo    ========================================
echo.

REM --- Passo 1: Verificar se o ambiente virtual existe ---
echo [1/3] A verificar o ambiente virtual...
if not exist venv\Scripts\activate.bat (
    echo   [ERRO] Ambiente virtual 'venv' nao encontrado.
    echo   Por favor, execute o ficheiro 'install.bat' primeiro para configurar o ambiente.
    pause
    exit /b 1
)
echo   [OK] Ambiente virtual encontrado.
echo.

REM --- Passo 2: Ativar o Ambiente Virtual ---
echo [2/3] A ativar o ambiente virtual...
call venv\Scripts\activate.bat
if errorlevel 1 (
    echo   [ERRO] Falha ao ativar o ambiente virtual.
    pause
    exit /b 1
)
echo   [OK] Ambiente virtual ativado.
echo.

REM --- Passo 3: Iniciar a Aplicação ---
echo [3/3] A iniciar o servidor da aplicacao Flask...
echo      A aplicacao estara disponivel em http://localhost:5000
echo      Pressione CTRL+C na janela do terminal para parar o servidor.
echo.
echo    =================================================================
echo.

REM Executa o script principal da aplicação Python
python src/run.py

echo.
echo    =================================================================
echo      Servidor encerrado.
echo    =================================================================
echo.
pause
