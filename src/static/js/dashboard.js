// Ficheiro: src/static/js/dashboard.js

/**
 * Dashboard Interativo para ARQV30 Enhanced
 * Gerencia a exibição e interação com os resultados da análise psicológica
 */
class DashboardManager {
    constructor() {
        this.currentAnalysis = null;
        this.charts = {};
        this.init();
    }

    init() {
        console.log("Dashboard Manager inicializado.");
        this.setupEventListeners();
    }

    setupEventListeners() {
        // Event listeners para interações do dashboard
        document.addEventListener('click', (e) => {
            if (e.target.matches('.expand-card')) {
                this.toggleCardExpansion(e.target);
            }
            if (e.target.matches('.copy-script')) {
                this.copyToClipboard(e.target);
            }
        });
    }

    /**
     * Renderiza o dashboard completo com os dados da análise
     */
    renderDashboard(analysisData) {
        console.log("Renderizando dashboard com dados:", analysisData);
        this.currentAnalysis = analysisData;

        const container = document.getElementById('resultsContent');
        if (!container) {
            console.error("Container de resultados não encontrado");
            return;
        }

        // Limpa conteúdo anterior
        container.innerHTML = '';

        // Cria estrutura do dashboard
        const dashboardHTML = this.createDashboardStructure(analysisData);
        container.innerHTML = dashboardHTML;

        // Inicializa componentes interativos
        this.initializeInteractiveComponents();
        
        // Anima entrada dos cards
        this.animateCardsEntrance();
    }

    /**
     * Cria a estrutura HTML completa do dashboard
     */
    createDashboardStructure(data) {
        return `
            <div class="dashboard-container">
                ${this.createDashboardHeader(data)}
                ${this.createExecutiveSummary(data)}
                ${this.createAvatarSection(data)}
                ${this.createDriversSection(data)}
                ${this.createObjectionsSection(data)}
                ${this.createVisualProofsSection(data)}
                ${this.createMarketAnalysisSection(data)}
                ${this.createCompetitionSection(data)}
                ${this.createActionPlanSection(data)}
                ${this.createImplementationSection(data)}
                ${this.createDashboardActions()}
            </div>
        `;
    }

    createDashboardHeader(data) {
        const segmento = data.segmento || 'Análise de Mercado';
        const produto = data.produto || '';
        
        return `
            <div class="dashboard-header">
                <h1 class="dashboard-title">
                    <i class="fas fa-brain"></i>
                    Análise Psicológica Profunda
                </h1>
                <p class="dashboard-subtitle">
                    Relatório completo para <strong>${segmento}</strong>
                    ${produto ? ` - ${produto}` : ''}
                </p>
                <div class="analysis-meta">
                    <span class="meta-item">
                        <i class="fas fa-calendar"></i>
                        ${new Date().toLocaleDateString('pt-BR')}
                    </span>
                    <span class="meta-item">
                        <i class="fas fa-clock"></i>
                        ${new Date().toLocaleTimeString('pt-BR', {hour: '2-digit', minute: '2-digit'})}
                    </span>
                </div>
            </div>
        `;
    }

    createExecutiveSummary(data) {
        const resumo = data.resumo_executivo || 'Resumo executivo não disponível.';
        
        return `
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-chart-line"></i>
                    </div>
                    <h2 class="card-title">Resumo Executivo</h2>
                </div>
                <div class="card-content">
                    <p>${resumo}</p>
                </div>
            </div>
        `;
    }

    createAvatarSection(data) {
        const avatar = data.avatar_psicologico_profundo || data.avatar_psicologico || {};
        
        return `
            <div class="dashboard-card avatar-section">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-user-circle"></i>
                    </div>
                    <h2 class="card-title">Avatar Psicológico Profundo</h2>
                </div>
                <div class="card-content">
                    <div class="avatar-grid">
                        ${this.createAvatarItem('Perfil Demográfico', avatar.perfil_demografico, 'fas fa-users')}
                        ${this.createAvatarItem('Perfil Psicográfico', avatar.perfil_psicografico, 'fas fa-brain')}
                        ${this.createAvatarItem('Dores Viscerais', avatar.dores_viscerais || avatar.dores_secretas, 'fas fa-heart-broken')}
                        ${this.createAvatarItem('Desejos Secretos', avatar.desejos_secretos || avatar.desejos_ardentes, 'fas fa-star')}
                        ${this.createAvatarItem('Medos Paralisantes', avatar.medos_paralisantes, 'fas fa-exclamation-triangle')}
                        ${this.createAvatarItem('Objeções Reais', avatar.objecoes_reais, 'fas fa-shield-alt')}
                    </div>
                </div>
            </div>
        `;
    }

    createAvatarItem(title, data, icon) {
        if (!data) return '';
        
        let content = '';
        if (Array.isArray(data)) {
            content = `<ul>${data.map(item => `<li>${item}</li>`).join('')}</ul>`;
        } else if (typeof data === 'object') {
            content = `<ul>${Object.entries(data).map(([key, value]) => 
                `<li><strong>${key.replace(/_/g, ' ').toUpperCase()}:</strong> ${value}</li>`
            ).join('')}</ul>`;
        } else {
            content = `<p>${data}</p>`;
        }

        return `
            <div class="avatar-item">
                <h4><i class="${icon}"></i> ${title}</h4>
                ${content}
            </div>
        `;
    }

    createDriversSection(data) {
        const drivers = data.drivers_mentais_customizados || data.drivers_mentais || [];
        
        return `
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-cogs"></i>
                    </div>
                    <h2 class="card-title">Drivers Mentais Customizados</h2>
                </div>
                <div class="card-content">
                    <div class="drivers-grid">
                        ${drivers.map(driver => this.createDriverCard(driver)).join('')}
                    </div>
                </div>
            </div>
        `;
    }

    createDriverCard(driver) {
        return `
            <div class="driver-card">
                <div class="driver-name">${driver.nome}</div>
                <div class="driver-category">${driver.categoria || 'Mental'}</div>
                
                <div class="driver-details">
                    <div class="driver-detail">
                        <strong>Gatilho Central:</strong>
                        <p>${driver.gatilho_central}</p>
                    </div>
                    
                    ${driver.mecanica_psicologica ? `
                        <div class="driver-detail">
                            <strong>Mecânica Psicológica:</strong>
                            <p>${driver.mecanica_psicologica}</p>
                        </div>
                    ` : ''}
                    
                    ${driver.roteiro_ativacao ? `
                        <div class="driver-detail">
                            <strong>Roteiro de Ativação:</strong>
                            ${this.formatRoteiro(driver.roteiro_ativacao)}
                        </div>
                    ` : ''}
                    
                    ${driver.frases_ancoragem ? `
                        <div class="driver-detail">
                            <strong>Frases de Ancoragem:</strong>
                            <ul>${driver.frases_ancoragem.map(frase => `<li>"${frase}"</li>`).join('')}</ul>
                        </div>
                    ` : ''}
                </div>
                
                <button class="copy-script" data-script="${this.escapeHtml(JSON.stringify(driver))}">
                    <i class="fas fa-copy"></i> Copiar Script
                </button>
            </div>
        `;
    }

    formatRoteiro(roteiro) {
        if (typeof roteiro === 'string') {
            return `<p>${roteiro}</p>`;
        }
        
        if (typeof roteiro === 'object') {
            return `
                <div class="roteiro-details">
                    ${roteiro.pergunta_abertura ? `<p><strong>Pergunta:</strong> "${roteiro.pergunta_abertura}"</p>` : ''}
                    ${roteiro.historia_analogia ? `<p><strong>História:</strong> ${roteiro.historia_analogia}</p>` : ''}
                    ${roteiro.metafora_visual ? `<p><strong>Metáfora:</strong> ${roteiro.metafora_visual}</p>` : ''}
                    ${roteiro.comando_acao ? `<p><strong>Comando:</strong> ${roteiro.comando_acao}</p>` : ''}
                </div>
            `;
        }
        
        return '<p>Roteiro não disponível</p>';
    }

    createObjectionsSection(data) {
        const objecoes = data.mapeamento_objecoes || {};
        
        return `
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-shield-alt"></i>
                    </div>
                    <h2 class="card-title">Mapeamento de Objeções</h2>
                </div>
                <div class="card-content">
                    ${this.createObjectionsContent(objecoes)}
                </div>
            </div>
        `;
    }

    createObjectionsContent(objecoes) {
        let content = '';
        
        if (objecoes.objecoes_universais) {
            content += `
                <div class="objections-section">
                    <h4><i class="fas fa-globe"></i> Objeções Universais</h4>
                    <div class="objections-grid">
                        ${Object.entries(objecoes.objecoes_universais).map(([key, obj]) => `
                            <div class="objection-card">
                                <h5>${key.toUpperCase()}</h5>
                                <p><strong>Probabilidade:</strong> ${obj.probabilidade}</p>
                                <p><strong>Tratamento:</strong> ${obj.tratamento}</p>
                                ${obj.script_neutralizacao ? `
                                    <div class="script-box">
                                        <strong>Script:</strong>
                                        <p>"${obj.script_neutralizacao}"</p>
                                    </div>
                                ` : ''}
                            </div>
                        `).join('')}
                    </div>
                </div>
            `;
        }
        
        if (objecoes.objecoes_ocultas) {
            content += `
                <div class="objections-section">
                    <h4><i class="fas fa-eye-slash"></i> Objeções Ocultas</h4>
                    <div class="objections-grid">
                        ${Object.entries(objecoes.objecoes_ocultas).map(([key, obj]) => `
                            <div class="objection-card">
                                <h5>${key.replace(/_/g, ' ').toUpperCase()}</h5>
                                <p><strong>Probabilidade:</strong> ${obj.probabilidade}</p>
                                ${obj.sinais ? `<p><strong>Sinais:</strong> ${obj.sinais.join(', ')}</p>` : ''}
                                <p><strong>Tratamento:</strong> ${obj.tratamento}</p>
                            </div>
                        `).join('')}
                    </div>
                </div>
            `;
        }
        
        return content || '<p>Mapeamento de objeções não disponível.</p>';
    }

    createVisualProofsSection(data) {
        const provas = data.arsenal_provas_visuais || data.provas_visuais || [];
        
        return `
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-eye"></i>
                    </div>
                    <h2 class="card-title">Arsenal de Provas Visuais</h2>
                </div>
                <div class="card-content">
                    <div class="provas-grid">
                        ${provas.map(prova => this.createProvaCard(prova)).join('')}
                    </div>
                </div>
            </div>
        `;
    }

    createProvaCard(prova) {
        return `
            <div class="prova-card">
                <div class="prova-header">
                    <div class="prova-name">${prova.nome_impactante || prova.nome}</div>
                    <div class="prova-category">${prova.categoria || 'Visual'}</div>
                </div>
                
                <div class="prova-content">
                    <div class="prova-section">
                        <h5><i class="fas fa-target"></i> Conceito Alvo</h5>
                        <p>${prova.conceito_alvo || prova.conceito}</p>
                    </div>
                    
                    ${prova.experimento_fisico || prova.experimento ? `
                        <div class="prova-section">
                            <h5><i class="fas fa-flask"></i> Experimento</h5>
                            ${this.formatExperimento(prova.experimento_fisico || prova.experimento)}
                        </div>
                    ` : ''}
                    
                    ${prova.analogia_perfeita ? `
                        <div class="prova-section">
                            <h5><i class="fas fa-lightbulb"></i> Analogia</h5>
                            <p>${prova.analogia_perfeita}</p>
                        </div>
                    ` : ''}
                    
                    ${prova.momento_ideal ? `
                        <div class="prova-section">
                            <h5><i class="fas fa-clock"></i> Momento Ideal</h5>
                            <p>${prova.momento_ideal}</p>
                        </div>
                    ` : ''}
                </div>
            </div>
        `;
    }

    formatExperimento(experimento) {
        if (typeof experimento === 'string') {
            return `<p>${experimento}</p>`;
        }
        
        if (typeof experimento === 'object') {
            let content = '';
            if (experimento.materiais) {
                content += `<p><strong>Materiais:</strong> ${experimento.materiais.join(', ')}</p>`;
            }
            if (experimento.setup) {
                content += `<p><strong>Setup:</strong> ${experimento.setup}</p>`;
            }
            if (experimento.execucao) {
                content += `<p><strong>Execução:</strong> ${experimento.execucao}</p>`;
            }
            if (experimento.climax) {
                content += `<p><strong>Clímax:</strong> ${experimento.climax}</p>`;
            }
            return content;
        }
        
        return '<p>Experimento não disponível</p>';
    }

    createMarketAnalysisSection(data) {
        const mercado = data.analise_mercado || {};
        
        return `
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-chart-pie"></i>
                    </div>
                    <h2 class="card-title">Análise de Mercado</h2>
                </div>
                <div class="card-content">
                    <div class="market-stats">
                        <div class="stat-item">
                            <span class="stat-value">${mercado.tamanho_mercado || 'N/A'}</span>
                            <span class="stat-label">Tamanho do Mercado</span>
                        </div>
                        <div class="stat-item">
                            <span class="stat-value">${mercado.nivel_competitividade || 'N/A'}</span>
                            <span class="stat-label">Competitividade</span>
                        </div>
                    </div>
                    
                    ${mercado.principais_tendencias ? `
                        <div class="market-section">
                            <h4><i class="fas fa-trending-up"></i> Principais Tendências</h4>
                            <ul>${mercado.principais_tendencias.map(t => `<li>${t}</li>`).join('')}</ul>
                        </div>
                    ` : ''}
                    
                    ${mercado.oportunidades ? `
                        <div class="market-section">
                            <h4><i class="fas fa-bullseye"></i> Oportunidades</h4>
                            <ul>${mercado.oportunidades.map(o => `<li>${o}</li>`).join('')}</ul>
                        </div>
                    ` : ''}
                    
                    ${mercado.ameacas ? `
                        <div class="market-section">
                            <h4><i class="fas fa-exclamation-triangle"></i> Ameaças</h4>
                            <ul>${mercado.ameacas.map(a => `<li>${a}</li>`).join('')}</ul>
                        </div>
                    ` : ''}
                </div>
            </div>
        `;
    }

    createCompetitionSection(data) {
        const concorrentes = data.analise_concorrencia || [];
        
        return `
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-chess"></i>
                    </div>
                    <h2 class="card-title">Análise da Concorrência</h2>
                </div>
                <div class="card-content">
                    <div class="competitor-grid">
                        ${concorrentes.map(comp => this.createCompetitorCard(comp)).join('')}
                    </div>
                </div>
            </div>
        `;
    }

    createCompetitorCard(competitor) {
        return `
            <div class="competitor-card">
                <div class="competitor-name">${competitor.nome}</div>
                
                ${competitor.pontos_fortes ? `
                    <div class="competitor-section">
                        <h5><i class="fas fa-plus-circle"></i> Pontos Fortes</h5>
                        <ul>${competitor.pontos_fortes.map(p => `<li>${p}</li>`).join('')}</ul>
                    </div>
                ` : ''}
                
                ${competitor.pontos_fracos ? `
                    <div class="competitor-section">
                        <h5><i class="fas fa-minus-circle"></i> Pontos Fracos</h5>
                        <ul>${competitor.pontos_fracos.map(p => `<li>${p}</li>`).join('')}</ul>
                    </div>
                ` : ''}
                
                ${competitor.posicionamento ? `
                    <div class="competitor-section">
                        <h5><i class="fas fa-map-marker-alt"></i> Posicionamento</h5>
                        <p>${competitor.posicionamento}</p>
                    </div>
                ` : ''}
                
                ${competitor.preco_medio ? `
                    <div class="competitor-section">
                        <h5><i class="fas fa-dollar-sign"></i> Preço Médio</h5>
                        <p>${competitor.preco_medio}</p>
                    </div>
                ` : ''}
            </div>
        `;
    }

    createActionPlanSection(data) {
        const plano = data.plano_acao_90_dias || data.plano_acao_inicial || {};
        
        return `
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-tasks"></i>
                    </div>
                    <h2 class="card-title">Plano de Ação (90 Dias)</h2>
                </div>
                <div class="card-content">
                    <div class="action-timeline">
                        ${this.createTimelineItems(plano)}
                    </div>
                </div>
            </div>
        `;
    }

    createTimelineItems(plano) {
        const periods = ['primeiros_30_dias', 'segundos_30_dias', 'terceiros_30_dias'];
        const labels = ['Primeiros 30 Dias', 'Segundos 30 Dias', 'Terceiros 30 Dias'];
        
        return periods.map((period, index) => {
            const data = plano[period];
            if (!data) return '';
            
            return `
                <div class="timeline-item">
                    <div class="timeline-header">
                        <div class="timeline-title">${labels[index]}</div>
                        <div class="timeline-duration">30 dias</div>
                    </div>
                    <div class="timeline-content">
                        ${data.foco ? `
                            <div class="timeline-section">
                                <h5>Foco Principal</h5>
                                <p>${data.foco}</p>
                            </div>
                        ` : ''}
                        
                        ${data.objetivos ? `
                            <div class="timeline-section">
                                <h5>Objetivos</h5>
                                <ul>${data.objetivos.map(obj => `<li>${obj}</li>`).join('')}</ul>
                            </div>
                        ` : ''}
                        
                        ${data.acoes_especificas || data.passos ? `
                            <div class="timeline-section">
                                <h5>Ações Específicas</h5>
                                <ul>${(data.acoes_especificas || data.passos).map(acao => `<li>${acao}</li>`).join('')}</ul>
                            </div>
                        ` : ''}
                        
                        ${data.metricas ? `
                            <div class="timeline-section">
                                <h5>Métricas</h5>
                                <ul>${data.metricas.map(metrica => `<li>${metrica}</li>`).join('')}</ul>
                            </div>
                        ` : ''}
                    </div>
                </div>
            `;
        }).join('');
    }

    createImplementationSection(data) {
        const implementacao = data.plano_implementacao || {};
        
        return `
            <div class="dashboard-card">
                <div class="card-header">
                    <div class="card-icon">
                        <i class="fas fa-rocket"></i>
                    </div>
                    <h2 class="card-title">Plano de Implementação</h2>
                </div>
                <div class="card-content">
                    ${this.createImplementationContent(implementacao)}
                </div>
            </div>
        `;
    }

    createImplementationContent(implementacao) {
        let content = '';
        
        if (implementacao.cronograma_preparacao) {
            content += `
                <div class="implementation-section">
                    <h4><i class="fas fa-calendar-check"></i> Cronograma de Preparação</h4>
                    ${Object.entries(implementacao.cronograma_preparacao).map(([periodo, atividades]) => `
                        <div class="prep-period">
                            <h5>${periodo.replace(/_/g, ' ').toUpperCase()}</h5>
                            <ul>${atividades.map(ativ => `<li>${ativ}</li>`).join('')}</ul>
                        </div>
                    `).join('')}
                </div>
            `;
        }
        
        if (implementacao.checkpoints_execucao) {
            content += `
                <div class="implementation-section">
                    <h4><i class="fas fa-flag-checkered"></i> Checkpoints de Execução</h4>
                    <div class="checkpoints-grid">
                        ${Object.entries(implementacao.checkpoints_execucao).map(([momento, acao]) => `
                            <div class="checkpoint-item">
                                <strong>${momento.replace(/_/g, ' ').toUpperCase()}:</strong>
                                <p>${acao}</p>
                            </div>
                        `).join('')}
                    </div>
                </div>
            `;
        }
        
        if (implementacao.metricas_sucesso) {
            content += `
                <div class="implementation-section">
                    <h4><i class="fas fa-chart-bar"></i> Métricas de Sucesso</h4>
                    ${Object.entries(implementacao.metricas_sucesso).map(([fase, metricas]) => `
                        <div class="metrics-group">
                            <h5>${fase.replace(/_/g, ' ').toUpperCase()}</h5>
                            <ul>${metricas.map(metrica => `<li>${metrica}</li>`).join('')}</ul>
                        </div>
                    `).join('')}
                </div>
            `;
        }
        
        return content || '<p>Plano de implementação não disponível.</p>';
    }

    createDashboardActions() {
        return `
            <div class="dashboard-actions">
                <button class="action-btn primary" id="downloadPdfBtn">
                    <i class="fas fa-file-pdf"></i>
                    Download PDF Completo
                </button>
                <button class="action-btn secondary" onclick="window.print()">
                    <i class="fas fa-print"></i>
                    Imprimir Relatório
                </button>
                <button class="action-btn secondary" onclick="window.location.reload()">
                    <i class="fas fa-plus"></i>
                    Nova Análise
                </button>
            </div>
        `;
    }

    /**
     * Inicializa componentes interativos do dashboard
     */
    initializeInteractiveComponents() {
        // Configura botão de download PDF
        const pdfBtn = document.getElementById('downloadPdfBtn');
        if (pdfBtn) {
            pdfBtn.addEventListener('click', () => this.downloadPDF());
        }

        // Configura tooltips
        this.initializeTooltips();
        
        // Configura expansão de cards
        this.initializeCardExpansion();
    }

    initializeTooltips() {
        // Adiciona tooltips para elementos com data-tooltip
        document.querySelectorAll('[data-tooltip]').forEach(element => {
            element.classList.add('tooltip');
        });
    }

    initializeCardExpansion() {
        // Permite expandir/colapsar seções do dashboard
        document.querySelectorAll('.card-header').forEach(header => {
            header.style.cursor = 'pointer';
            header.addEventListener('click', (e) => {
                const card = e.target.closest('.dashboard-card');
                const content = card.querySelector('.card-content');
                
                if (content.style.display === 'none') {
                    content.style.display = 'block';
                    card.classList.remove('collapsed');
                } else {
                    content.style.display = 'none';
                    card.classList.add('collapsed');
                }
            });
        });
    }

    /**
     * Anima a entrada dos cards do dashboard
     */
    animateCardsEntrance() {
        const cards = document.querySelectorAll('.dashboard-card');
        cards.forEach((card, index) => {
            card.style.opacity = '0';
            card.style.transform = 'translateY(30px)';
            
            setTimeout(() => {
                card.style.transition = 'all 0.6s ease-out';
                card.style.opacity = '1';
                card.style.transform = 'translateY(0)';
            }, index * 100);
        });
    }

    /**
     * Copia texto para a área de transferência
     */
    copyToClipboard(button) {
        const script = button.getAttribute('data-script');
        
        if (navigator.clipboard) {
            navigator.clipboard.writeText(script).then(() => {
                this.showCopyFeedback(button);
            });
        } else {
            // Fallback para navegadores mais antigos
            const textArea = document.createElement('textarea');
            textArea.value = script;
            document.body.appendChild(textArea);
            textArea.select();
            document.execCommand('copy');
            document.body.removeChild(textArea);
            this.showCopyFeedback(button);
        }
    }

    showCopyFeedback(button) {
        const originalText = button.innerHTML;
        button.innerHTML = '<i class="fas fa-check"></i> Copiado!';
        button.style.background = '#06ffa5';
        
        setTimeout(() => {
            button.innerHTML = originalText;
            button.style.background = '';
        }, 2000);
    }

    /**
     * Gera e baixa o PDF do relatório
     */
    async downloadPDF() {
        if (!this.currentAnalysis) {
            window.app.showAlert('Nenhuma análise disponível para download.', 'error');
            return;
        }

        const pdfBtn = document.getElementById('downloadPdfBtn');
        window.app.setButtonLoading(pdfBtn, true);

        try {
            const response = await fetch('/api/generate_pdf', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(this.currentAnalysis)
            });

            if (response.ok) {
                const blob = await response.blob();
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = `Analise_Psicologica_${new Date().toISOString().split('T')[0]}.pdf`;
                document.body.appendChild(a);
                a.click();
                window.URL.revokeObjectURL(url);
                document.body.removeChild(a);
                
                window.app.showAlert('PDF gerado com sucesso!', 'success');
            } else {
                throw new Error('Erro ao gerar PDF');
            }
        } catch (error) {
            console.error('Erro ao gerar PDF:', error);
            window.app.showAlert('Erro ao gerar PDF. Tente novamente.', 'error');
        } finally {
            window.app.setButtonLoading(pdfBtn, false);
        }
    }

    /**
     * Utilitário para escapar HTML
     */
    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    /**
     * Atualiza uma seção específica do dashboard
     */
    updateSection(sectionId, newData) {
        const section = document.getElementById(sectionId);
        if (section && newData) {
            // Implementar lógica de atualização específica
            console.log(`Atualizando seção ${sectionId} com:`, newData);
        }
    }

    /**
     * Exporta dados do dashboard em formato JSON
     */
    exportData() {
        if (!this.currentAnalysis) {
            window.app.showAlert('Nenhuma análise disponível para exportar.', 'error');
            return;
        }

        const dataStr = JSON.stringify(this.currentAnalysis, null, 2);
        const dataBlob = new Blob([dataStr], {type: 'application/json'});
        const url = URL.createObjectURL(dataBlob);
        
        const a = document.createElement('a');
        a.href = url;
        a.download = `analise_dados_${new Date().toISOString().split('T')[0]}.json`;
        document.body.appendChild(a);
        a.click();
        document.body.removeChild(a);
        URL.revokeObjectURL(url);
        
        window.app.showAlert('Dados exportados com sucesso!', 'success');
    }
}

// Instância global do dashboard
window.dashboardManager = new DashboardManager();