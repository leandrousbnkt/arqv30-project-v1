// Ficheiro: src/static/js/upload.js

/**
 * Gestor de Upload de Ficheiros para o ARQV30.
 * * NOTA: Na versão atual refatorizada, a funcionalidade de upload de ficheiros
 * está desativada na interface principal para simplificar o fluxo.
 * Este ficheiro serve como uma base para a futura reativação desta funcionalidade.
 */
class FileUploadManager {
    constructor() {
        // Seletores para os elementos de upload (atualmente comentados no HTML)
        this.uploadArea = document.getElementById('uploadArea');
        this.fileInput = document.getElementById('fileInput');
        this.uploadedFilesContainer = document.getElementById('uploadedFiles');
        
        // Limites e tipos de ficheiros permitidos
        this.maxFileSize = 16 * 1024 * 1024; // 16MB
        this.allowedExtensions = ['.pdf', '.doc', '.docx', '.xlsx', '.csv', '.txt', '.json'];

        this.init();
    }

    /**
     * Inicializa os event listeners se os elementos existirem na página.
     */
    init() {
        if (this.uploadArea && this.fileInput) {
            console.log("FileUploadManager a inicializar eventos.");
            this.setupDragAndDrop();
            this.setupFileInput();
        } else {
            console.log("Elementos de upload não encontrados. A funcionalidade de upload está inativa.");
        }
    }

    /**
     * Configura a funcionalidade de arrastar e largar (drag and drop).
     */
    setupDragAndDrop() {
        // Previne os comportamentos padrão do navegador
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            this.uploadArea.addEventListener(eventName, e => {
                e.preventDefault();
                e.stopPropagation();
            }, false);
        });

        // Adiciona um destaque visual quando um ficheiro é arrastado sobre a área
        ['dragenter', 'dragover'].forEach(eventName => {
            this.uploadArea.addEventListener(eventName, () => {
                this.uploadArea.classList.add('dragover');
            }, false);
        });

        ['dragleave', 'drop'].forEach(eventName => {
            this.uploadArea.addEventListener(eventName, () => {
                this.uploadArea.classList.remove('dragover');
            }, false);
        });

        // Lida com os ficheiros quando são largados
        this.uploadArea.addEventListener('drop', e => {
            const files = e.dataTransfer.files;
            this.handleFiles(Array.from(files));
        }, false);
    }

    /**
     * Configura o input de ficheiro tradicional.
     */
    setupFileInput() {
        this.fileInput.addEventListener('change', e => {
            const files = e.target.files;
            this.handleFiles(Array.from(files));
        });
    }

    /**
     * Processa uma lista de ficheiros selecionados ou largados.
     * @param {File[]} files - A lista de ficheiros a processar.
     */
    handleFiles(files) {
        // Na versão atual, apenas mostra um alerta
        window.app.showAlert('A funcionalidade de upload de ficheiros será ativada numa futura versão.', 'info');
        
        // A lógica de validação e upload seria chamada aqui.
        // Exemplo:
        // files.forEach(file => {
        //     if (this.validateFile(file)) {
        //         this.addFileToUI(file);
        //         this.uploadFile(file);
        //     }
        // });
    }

    /**
     * Valida um ficheiro com base no tamanho e extensão.
     * @param {File} file - O ficheiro a validar.
     * @returns {boolean} - True se o ficheiro for válido.
     */
    validateFile(file) {
        const fileExtension = '.' + file.name.split('.').pop().toLowerCase();
        
        if (file.size > this.maxFileSize) {
            window.app.showAlert(`O ficheiro "${file.name}" é demasiado grande (Máx: 16MB).`, 'error');
            return false;
        }

        if (!this.allowedExtensions.includes(fileExtension)) {
            window.app.showAlert(`O tipo de ficheiro "${file.name}" não é suportado.`, 'error');
            return false;
        }

        return true;
    }

    /**
     * (Função Futura) Adiciona o ficheiro à interface do utilizador com uma barra de progresso.
     */
    addFileToUI(file) {
        // Lógica para criar o elemento HTML do ficheiro
        console.log(`(Simulação) A adicionar ${file.name} à UI.`);
    }

    /**
     * (Função Futura) Envia o ficheiro para o endpoint da API.
     */
    async uploadFile(file) {
        // Lógica para enviar o ficheiro para /api/upload_attachment
        console.log(`(Simulação) A fazer upload de ${file.name}.`);
    }
}

// --- Instância Global ---
// Cria a instância do gestor de uploads.
window.uploadManager = new FileUploadManager();
