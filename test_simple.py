# Ficheiro: test_simple.py

import sys
import os
import logging

# --- Configuração Inicial ---
# Adiciona o diretório 'src' ao path do Python para que possamos importar os nossos módulos.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Configura o logging para vermos as mensagens de status dos serviços
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Tenta importar os serviços principais. Se isto falhar, a estrutura de pastas está incorreta.
try:
    from database import db_manager
    from services.search_manager import search_manager
    from services.ai_manager import ai_manager
except ImportError as e:
    print(f"\n[ERRO CRÍTICO] Falha ao importar os módulos. Verifique a estrutura do projeto.")
    print(f"Detalhe: {e}")
    sys.exit(1)

def run_test(test_name, test_function):
    """Função auxiliar para executar um teste e imprimir o resultado."""
    print(f"--- A executar teste: {test_name} ---")
    try:
        success = test_function()
        if success:
            print(f"[SUCESSO] {test_name} passou.")
        else:
            print(f"[FALHA] {test_name} falhou. Verifique as configurações e logs.")
        print("-" * (len(test_name) + 25))
        return success
    except Exception as e:
        print(f"[ERRO] Ocorreu uma exceção durante o teste '{test_name}': {e}")
        print("-" * (len(test_name) + 25))
        return False

# --- Definições dos Testes ---

def test_database_connection():
    """Testa se a aplicação consegue conectar-se ao banco de dados Supabase."""
    return db_manager.test_connection()

def test_search_services():
    """Testa o SearchManager para garantir que as APIs de busca estão a funcionar."""
    results = search_manager.multi_search("tendências de IA no Brasil", max_results=5)
    # O teste passa se recebermos uma lista (mesmo que vazia, indica que não houve erro)
    return isinstance(results, list) and len(results) > 0

def test_ai_services():
    """Testa o AIManager para garantir que as APIs de IA (Gemini/HuggingFace) estão a funcionar."""
    # Usamos um prompt muito simples e curto para um teste rápido
    response = ai_manager.generate_analysis("Diga apenas 'Olá, mundo!' em português.", max_tokens=20)
    return response is not None and "olá, mundo" in response.lower()

# --- Orquestrador Principal dos Testes ---

def run_all_tests():
    """Executa todos os testes definidos e apresenta um relatório final."""
    print("\n=================================================")
    print("  INICIANDO TESTES DE DIAGNÓSTICO DO ARQV30")
    print("=================================================\n")

    # Lista de todos os testes a serem executados
    tests_to_run = {
        "Conexão com Banco de Dados (Supabase)": test_database_connection,
        "Serviços de Busca (Jina, Google, ScrapingAnt)": test_search_services,
        "Serviços de IA (Gemini, HuggingFace)": test_ai_services,
    }

    results = {}
    for name, func in tests_to_run.items():
        results[name] = run_test(name, func)

    print("\n=================================================")
    print("              RELATÓRIO FINAL")
    print("=================================================\n")

    passed_count = sum(1 for result in results.values() if result)
    total_count = len(results)

    for name, success in results.items():
        status = "[SUCESSO]" if success else "[FALHA]"
        print(f"{status:<10} - {name}")

    print(f"\nResumo: {passed_count} de {total_count} testes passaram.")

    if passed_count == total_count:
        print("\n🎉 Todos os sistemas estão operacionais! A aplicação está pronta para ser executada.")
    else:
        print("\n⚠️ Alguns sistemas falharam. Verifique as suas chaves de API no ficheiro .env e os logs acima.")

    print("\n=================================================\n")
    return passed_count == total_count

if __name__ == "__main__":
    # Este bloco é executado quando o script é chamado diretamente
    run_all_tests()
