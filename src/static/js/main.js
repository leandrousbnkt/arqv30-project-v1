// Ficheiro: src/static/js/main.js

/**
 * Classe principal da aplicação ARQV30.
 * Gere o estado geral da interface e as interações do utilizador.
 */
class ARQVApp {
    constructor() {
        // Inicializa a aplicação quando o DOM estiver completamente carregado.
        document.addEventListener('DOMContentLoaded', () => this.init());
    }

    /**
     * Método de inicialização. Configura os event listeners e a interface.
     */
    init() {
        console.log("ARQV30 App inicializada.");
        this.setupEventListeners();
    }

    /**
     * Configura os event listeners globais da página.
     */
    setupEventListeners() {
        // Adiciona um efeito de scroll suave para links internos (âncoras).
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    target.scrollIntoView({
                        behavior: 'smooth',
                        block: 'start'
                    });
                }
            });
        });
    }

    /**
     * Exibe uma notificação dinâmica no ecrã.
     * @param {string} message - A mensagem a ser exibida.
     * @param {string} type - O tipo de alerta ('success', 'error', 'info').
     */
    showAlert(message, type = 'info') {
        // Remove qualquer alerta existente para evitar sobreposição.
        const existingAlert = document.querySelector('.alert-popup');
        if (existingAlert) {
            existingAlert.remove();
        }

        const alert = document.createElement('div');
        alert.className = `alert-popup alert-${type}`;

        const iconClass = {
            success: 'fas fa-check-circle',
            error: 'fas fa-exclamation-triangle',
            info: 'fas fa-info-circle'
        }[type];

        alert.innerHTML = `
            <i class="${iconClass}"></i>
            <span>${message}</span>
            <button class="close-btn" onclick="this.parentElement.remove()">&times;</button>
        `;

        document.body.appendChild(alert);

        // O alerta desaparece automaticamente após 5 segundos.
        setTimeout(() => {
            alert.remove();
        }, 5000);
    }

    /**
     * Ativa ou desativa o estado de "loading" de um botão.
     * @param {HTMLElement} button - O elemento do botão a ser modificado.
     * @param {boolean} isLoading - True para ativar o loading, false para desativar.
     */
    setButtonLoading(button, isLoading) {
        if (!button) return;

        if (isLoading) {
            button.disabled = true;
            // Guarda o texto original do botão para o restaurar mais tarde.
            button.dataset.originalText = button.innerHTML;
            button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> A Processar...';
        } else {
            button.disabled = false;
            // Restaura o texto original do botão.
            if (button.dataset.originalText) {
                button.innerHTML = button.dataset.originalText;
            }
        }
    }
}

// --- Instância Global ---
// Cria uma única instância da aplicação que será acessível globalmente.
window.app = new ARQVApp();
