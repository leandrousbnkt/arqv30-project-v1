// Ficheiro: src/static/js/analysis.js

/**
 * Gerenciador de Análise para ARQV30 Enhanced
 * Controla o processo de análise psicológica e exibição dos resultados
 */
class AnalysisManager {
    constructor() {
        this.isAnalyzing = false;
        this.currentStep = 0;
        this.totalSteps = 6;
        this.progressInterval = null;
        this.init();
    }

    init() {
        console.log("Analysis Manager inicializado.");
        this.setupEventListeners();
    }

    setupEventListeners() {
        // Event listener para o formulário de análise
        const form = document.getElementById('analysisForm');
        if (form) {
            form.addEventListener('submit', (e) => {
                e.preventDefault();
                this.startAnalysis();
            });
        }
    }

    /**
     * Inicia o processo de análise psicológica
     */
    async startAnalysis() {
        if (this.isAnalyzing) {
            window.app.showAlert('Uma análise já está em andamento.', 'info');
            return;
        }

        // Valida dados do formulário
        const formData = this.collectFormData();
        if (!this.validateFormData(formData)) {
            return;
        }

        this.isAnalyzing = true;
        this.currentStep = 0;

        // Configura interface para modo de análise
        this.setupAnalysisUI();
        
        try {
            // Inicia animação de progresso
            this.startProgressAnimation();
            
            // Chama API de análise
            const result = await this.performAnalysis(formData);
            
            // Processa resultado
            this.handleAnalysisResult(result);
            
        } catch (error) {
            console.error('Erro na análise:', error);
            this.handleAnalysisError(error);
        } finally {
            this.isAnalyzing = false;
            this.stopProgressAnimation();
        }
    }

    /**
     * Coleta dados do formulário
     */
    collectFormData() {
        const form = document.getElementById('analysisForm');
        const formData = new FormData(form);
        
        const data = {};
        for (let [key, value] of formData.entries()) {
            data[key] = value.trim();
        }
        
        // Converte preço para número se fornecido
        if (data.preco && data.preco !== '') {
            data.preco = parseFloat(data.preco);
        }
        
        return data;
    }

    /**
     * Valida dados do formulário
     */
    validateFormData(data) {
        if (!data.segmento || data.segmento.length < 3) {
            window.app.showAlert('Por favor, informe o segmento de mercado (mínimo 3 caracteres).', 'error');
            document.getElementById('segmento').focus();
            return false;
        }

        if (data.preco && (isNaN(data.preco) || data.preco < 0)) {
            window.app.showAlert('Por favor, informe um preço válido.', 'error');
            document.getElementById('preco').focus();
            return false;
        }

        return true;
    }

    /**
     * Configura interface para modo de análise
     */
    setupAnalysisUI() {
        // Esconde formulário e mostra área de progresso
        const formSection = document.querySelector('.analysis-section');
        const progressSection = document.getElementById('progressArea');
        const resultsSection = document.getElementById('resultsArea');
        
        if (formSection) formSection.style.display = 'none';
        if (progressSection) progressSection.style.display = 'block';
        if (resultsSection) resultsSection.style.display = 'none';
        
        // Configura botão de análise
        const analyzeBtn = document.getElementById('analyzeBtn');
        if (analyzeBtn) {
            window.app.setButtonLoading(analyzeBtn, true);
        }
        
        // Scroll para área de progresso
        if (progressSection) {
            progressSection.scrollIntoView({ behavior: 'smooth' });
        }
    }

    /**
     * Inicia animação de progresso
     */
    startProgressAnimation() {
        const progressFill = document.getElementById('progressBarFill');
        const statusText = document.getElementById('progressStatusText');
        
        const steps = [
            { progress: 15, text: '🧠 Analisando perfil psicológico do avatar...' },
            { progress: 30, text: '🔍 Realizando pesquisa web contextual...' },
            { progress: 45, text: '⚡ Criando drivers mentais customizados...' },
            { progress: 60, text: '🛡️ Mapeando objeções e resistências...' },
            { progress: 80, text: '👁️ Gerando arsenal de provas visuais...' },
            { progress: 95, text: '📊 Finalizando relatório integrado...' }
        ];
        
        let currentStepIndex = 0;
        
        this.progressInterval = setInterval(() => {
            if (currentStepIndex < steps.length) {
                const step = steps[currentStepIndex];
                
                if (progressFill) {
                    progressFill.style.width = `${step.progress}%`;
                }
                
                if (statusText) {
                    statusText.textContent = step.text;
                }
                
                currentStepIndex++;
            }
        }, 3000); // Muda a cada 3 segundos
    }

    /**
     * Para animação de progresso
     */
    stopProgressAnimation() {
        if (this.progressInterval) {
            clearInterval(this.progressInterval);
            this.progressInterval = null;
        }
        
        // Completa barra de progresso
        const progressFill = document.getElementById('progressBarFill');
        const statusText = document.getElementById('progressStatusText');
        
        if (progressFill) {
            progressFill.style.width = '100%';
        }
        
        if (statusText) {
            statusText.textContent = '✅ Análise concluída com sucesso!';
        }
    }

    /**
     * Executa a análise via API
     */
    async performAnalysis(formData) {
        const response = await fetch('/api/analyze', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.error || `Erro HTTP: ${response.status}`);
        }

        return await response.json();
    }

    /**
     * Processa resultado da análise
     */
    handleAnalysisResult(result) {
        console.log('Resultado da análise recebido:', result);
        
        // Aguarda um pouco para mostrar progresso completo
        setTimeout(() => {
            // Esconde área de progresso
            const progressSection = document.getElementById('progressArea');
            if (progressSection) {
                progressSection.style.display = 'none';
            }
            
            // Mostra área de resultados
            const resultsSection = document.getElementById('resultsArea');
            if (resultsSection) {
                resultsSection.style.display = 'block';
                resultsSection.scrollIntoView({ behavior: 'smooth' });
            }
            
            // Renderiza dashboard com os resultados
            if (window.dashboardManager) {
                window.dashboardManager.renderDashboard(result);
            } else {
                console.error('Dashboard Manager não encontrado');
                this.renderFallbackResults(result);
            }
            
            // Mostra botão de PDF se disponível
            const pdfBtn = document.getElementById('downloadPdfBtn');
            if (pdfBtn) {
                pdfBtn.style.display = 'inline-flex';
            }
            
            // Notifica sucesso
            window.app.showAlert('Análise psicológica concluída com sucesso!', 'success');
            
        }, 1500);
    }

    /**
     * Renderiza resultados em formato simples (fallback)
     */
    renderFallbackResults(result) {
        const container = document.getElementById('resultsContent');
        if (!container) return;
        
        let html = '<div class="fallback-results">';
        
        // Resumo Executivo
        if (result.resumo_executivo) {
            html += `
                <div class="result-section">
                    <div class="section-header">
                        <i class="fas fa-chart-line"></i>
                        Resumo Executivo
                    </div>
                    <div class="section-content">
                        <p>${result.resumo_executivo}</p>
                    </div>
                </div>
            `;
        }
        
        // Avatar Psicológico
        if (result.avatar_psicologico_profundo || result.avatar_psicologico) {
            const avatar = result.avatar_psicologico_profundo || result.avatar_psicologico;
            html += `
                <div class="result-section">
                    <div class="section-header">
                        <i class="fas fa-user-circle"></i>
                        Avatar Psicológico
                    </div>
                    <div class="section-content">
                        ${this.formatAvatarContent(avatar)}
                    </div>
                </div>
            `;
        }
        
        // Drivers Mentais
        if (result.drivers_mentais_customizados || result.drivers_mentais) {
            const drivers = result.drivers_mentais_customizados || result.drivers_mentais;
            html += `
                <div class="result-section">
                    <div class="section-header">
                        <i class="fas fa-cogs"></i>
                        Drivers Mentais
                    </div>
                    <div class="section-content">
                        ${this.formatDriversContent(drivers)}
                    </div>
                </div>
            `;
        }
        
        // Análise de Mercado
        if (result.analise_mercado) {
            html += `
                <div class="result-section">
                    <div class="section-header">
                        <i class="fas fa-chart-pie"></i>
                        Análise de Mercado
                    </div>
                    <div class="section-content">
                        ${this.formatMarketContent(result.analise_mercado)}
                    </div>
                </div>
            `;
        }
        
        html += '</div>';
        container.innerHTML = html;
    }

    formatAvatarContent(avatar) {
        let content = '';
        
        if (avatar.dores_viscerais || avatar.dores_secretas) {
            const dores = avatar.dores_viscerais || avatar.dores_secretas;
            content += `
                <h4>Dores Viscerais</h4>
                <ul>${dores.map(dor => `<li>${dor}</li>`).join('')}</ul>
            `;
        }
        
        if (avatar.desejos_secretos || avatar.desejos_ardentes) {
            const desejos = avatar.desejos_secretos || avatar.desejos_ardentes;
            content += `
                <h4>Desejos Secretos</h4>
                <ul>${desejos.map(desejo => `<li>${desejo}</li>`).join('')}</ul>
            `;
        }
        
        if (avatar.medos_paralisantes) {
            content += `
                <h4>Medos Paralisantes</h4>
                <ul>${avatar.medos_paralisantes.map(medo => `<li>${medo}</li>`).join('')}</ul>
            `;
        }
        
        return content;
    }

    formatDriversContent(drivers) {
        if (!Array.isArray(drivers)) return '<p>Drivers não disponíveis.</p>';
        
        return drivers.map(driver => `
            <div class="driver-item">
                <h4>${driver.nome}</h4>
                <p><strong>Gatilho:</strong> ${driver.gatilho_central}</p>
                ${driver.roteiro_ativacao ? `<p><strong>Ativação:</strong> ${driver.roteiro_ativacao}</p>` : ''}
            </div>
        `).join('');
    }

    formatMarketContent(mercado) {
        let content = '';
        
        if (mercado.tamanho_mercado) {
            content += `<p><strong>Tamanho do Mercado:</strong> ${mercado.tamanho_mercado}</p>`;
        }
        
        if (mercado.principais_tendencias) {
            content += `
                <h4>Principais Tendências</h4>
                <ul>${mercado.principais_tendencias.map(t => `<li>${t}</li>`).join('')}</ul>
            `;
        }
        
        if (mercado.oportunidades) {
            content += `
                <h4>Oportunidades</h4>
                <ul>${mercado.oportunidades.map(o => `<li>${o}</li>`).join('')}</ul>
            `;
        }
        
        return content;
    }

    /**
     * Trata erros na análise
     */
    handleAnalysisError(error) {
        console.error('Erro na análise:', error);
        
        // Esconde área de progresso
        const progressSection = document.getElementById('progressArea');
        if (progressSection) {
            progressSection.style.display = 'none';
        }
        
        // Mostra formulário novamente
        const formSection = document.querySelector('.analysis-section');
        if (formSection) {
            formSection.style.display = 'block';
        }
        
        // Restaura botão
        const analyzeBtn = document.getElementById('analyzeBtn');
        if (analyzeBtn) {
            window.app.setButtonLoading(analyzeBtn, false);
        }
        
        // Mostra erro
        const errorMessage = error.message || 'Erro desconhecido na análise';
        window.app.showAlert(`Erro na análise: ${errorMessage}`, 'error');
    }

    /**
     * Reseta o estado da análise
     */
    resetAnalysis() {
        this.isAnalyzing = false;
        this.currentStep = 0;
        this.stopProgressAnimation();
        
        // Mostra formulário
        const formSection = document.querySelector('.analysis-section');
        if (formSection) {
            formSection.style.display = 'block';
        }
        
        // Esconde outras seções
        const progressSection = document.getElementById('progressArea');
        const resultsSection = document.getElementById('resultsArea');
        
        if (progressSection) progressSection.style.display = 'none';
        if (resultsSection) resultsSection.style.display = 'none';
        
        // Restaura botão
        const analyzeBtn = document.getElementById('analyzeBtn');
        if (analyzeBtn) {
            window.app.setButtonLoading(analyzeBtn, false);
        }
    }
}

// Instância global do gerenciador de análise
window.analysisManager = new AnalysisManager();
