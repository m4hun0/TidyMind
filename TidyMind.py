import os
import time
import shutil
import threading
from pathlib import Path
import customtkinter as ctk
from tkinter import filedialog
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue")

REGRAS_ORGANIZACAO = {
    "Documentos": [".pdf", ".docx", ".doc", ".txt", ".odt", ".rtf"],
    "Planilhas": [".xlsx", ".xls", ".csv", ".ods"],
    "Imagens": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".ico"],
    "Compactados": [".zip", ".rar", ".7z", ".tar.gz", ".gz"],
    "Codigos_e_Web": [".html", ".css", ".js", ".py", ".json", ".xml", ".md"],
    "Audio_e_Video": [".mp3", ".wav", ".m4a", ".mp4", ".mkv", ".avi"],
    "Executaveis": [".exe", ".msi", ".dmg"],
}

class AppTidyMind(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("TidyMind — Organizador Inteligente")
        self.geometry("700x580")
        self.minsize(600, 500)

        if os.path.exists("logo.ico"):
            self.iconbitmap("logo.ico")

        self.observer = None
        self.monitorando = False
        self.total_organizados = 0
        self.pasta_alvo = Path(os.environ["USERPROFILE"]) / "Downloads"

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(3, weight=1)

        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, padx=30, pady=(20, 10), sticky="ew")
        
        self.titulo = ctk.CTkLabel(self.header_frame, text="🧠 TidyMind", font=ctk.CTkFont(family="Segoe UI", size=28, weight="bold"))
        self.titulo.pack(anchor="w")
        
        self.slogan = ctk.CTkLabel(self.header_frame, text="Sua mente limpa, seu ecossistema digital organizado.", font=ctk.CTkFont(family="Segoe UI", size=13, slant="italic"), text_color="#3498DB")
        self.slogan.pack(anchor="w", pady=(2, 0))

        self.card_caminho = ctk.CTkFrame(self, corner_radius=12)
        self.card_caminho.grid(row=1, column=0, padx=30, pady=10, sticky="ew")
        
        self.subtitulo = ctk.CTkLabel(self.card_caminho, text=f"📂 Diretório Alvo: {self.pasta_alvo}", font=ctk.CTkFont(size=13, weight="normal"))
        self.subtitulo.pack(side="left", padx=20, pady=15)
        
        self.btn_selecionar = ctk.CTkButton(self.card_caminho, text="Alterar Pasta", width=110, command=self.selecionar_pasta, fg_color="#34495E", hover_color="#2C3E50", font=ctk.CTkFont(weight="bold"))
        self.btn_selecionar.pack(side="right", padx=20, pady=15)

        self.dash_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.dash_frame.grid(row=2, column=0, padx=30, pady=10, sticky="ew")
        self.dash_frame.grid_columnconfigure((0, 1), weight=1)

        self.card_status = ctk.CTkFrame(self.dash_frame, height=70, corner_radius=10)
        self.card_status.grid(row=0, column=0, padx=(0, 10), sticky="ew")
        self.status_label = ctk.CTkLabel(self.card_status, text="⚙️ SISTEMA PAUSADO", font=ctk.CTkFont(size=14, weight="bold"), text_color="#E74C3C")
        self.status_label.place(relx=0.5, rely=0.5, anchor="center")

        self.card_contador = ctk.CTkFrame(self.dash_frame, height=70, corner_radius=10)
        self.card_contador.grid(row=0, column=1, padx=(10, 0), sticky="ew")
        self.contador_label = ctk.CTkLabel(self.card_contador, text="✨ Organizados hoje: 0", font=ctk.CTkFont(size=14, weight="bold"), text_color="#2ECC71")
        self.contador_label.place(relx=0.5, rely=0.5, anchor="center")

        self.log_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.log_frame.grid(row=3, column=0, padx=30, pady=10, sticky="nsew")
        self.log_frame.grid_columnconfigure(0, weight=1)
        self.log_frame.grid_rowconfigure(1, weight=1)

        self.log_label = ctk.CTkLabel(self.log_frame, text="Histórico de Atividades", font=ctk.CTkFont(size=12, weight="bold"), text_color="gray")
        self.log_label.grid(row=0, column=0, sticky="w", pady=(0, 5))

        self.log_textbox = ctk.CTkTextbox(self.log_frame, activate_scrollbars=True, corner_radius=10, border_width=1, border_color="#2C3E50")
        self.log_textbox.grid(row=1, column=0, sticky="nsew")
        self.log_textbox.configure(state="disabled")

        self.progresso = ctk.CTkProgressBar(self, height=4, progress_color="#3498DB")
        self.progresso.grid(row=4, column=0, padx=30, pady=(5, 0), sticky="ew")
        self.progresso.set(0)

        self.footer_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.footer_frame.grid(row=5, column=0, padx=30, pady=(15, 20), sticky="ew")
        
        self.btn_iniciar = ctk.CTkButton(self.footer_frame, text="ATIVAR MONITORAMENTO", height=45, command=self.alternar_monitoramento, fg_color="#2ECC71", hover_color="#27AE60", font=ctk.CTkFont(size=14, weight="bold"))
        self.btn_iniciar.pack(fill="x")

    def selecionar_pasta(self):
        pasta_escolhida = filedialog.askdirectory(initialdir=self.pasta_alvo)
        if pasta_escolhida:
            if self.monitorando:
                self.alternar_monitoramento()
            self.pasta_alvo = Path(pasta_escolhida)
            self.subtitulo.configure(text=f"📂 Diretório Alvo: {self.pasta_alvo}")
            self.adicionar_log(f"📁 Diretório de monitoramento alterado para: {self.pasta_alvo}")

    def adicionar_log(self, mensagem):
        self.log_textbox.configure(state="normal")
        timestamp = time.strftime("[%H:%M:%S]")
        self.log_textbox.insert("end", f"{timestamp} {mensagem}\n")
        self.log_textbox.see("end")
        self.log_textbox.configure(state="disabled")

    def atualizar_contador(self):
        self.total_organizados += 1
        self.contador_label.configure(text=f"✨ Organizados hoje: {self.total_organizados}")

    def mover_arquivo_interface(self, caminho_arquivo):
        arquivo = Path(caminho_arquivo)
        if not arquivo.is_file() or arquivo.name.startswith(".") or arquivo.suffix.endswith(".tmp") or arquivo.suffix == ".crdownload":
            return
        
        tamanho_antigo = -1
        tentativas = 0
        while tentativas < 20:
            try:
                tamanho_atual = arquivo.stat().st_size
                if tamanho_atual == tamanho_antigo and tamanho_atual > 0:
                    break
                tamanho_antigo = tamanho_atual
                time.sleep(0.5)
            except FileNotFoundError:
                return
            tentativas += 1

        extensao = arquivo.suffix.lower()
        movido = False
        
        for pasta_destino, extensoes in REGRAS_ORGANIZACAO.items():
            if extensao in extensoes:
                nova_pasta = self.pasta_alvo / pasta_destino
                nova_pasta.mkdir(exist_ok=True)
                caminho_final = nova_pasta / arquivo.name
                try:
                    shutil.move(str(arquivo), str(caminho_final))
                    self.adicionar_log(f"✔️ {arquivo.name} -> {pasta_destino}/")
                    self.atualizar_contador()
                    movido = True
                except Exception:
                    self.adicionar_log(f"⚠️ Falha de acesso ao mover {arquivo.name}")
                break
        
        if not movido:
            pasta_outros = self.pasta_alvo / "Outros"
            pasta_outros.mkdir(exist_ok=True)
            try:
                shutil.move(str(arquivo), str(pasta_outros / arquivo.name))
                self.adicionar_log(f"📦 Desconhecido enviado para 'Outros' -> {arquivo.name}")
                self.atualizar_contador()
            except Exception:
                pass

    def alternar_monitoramento(self):
        if not self.monitorando:
            self.monitorando = True
            self.status_label.configure(text="🚀 TIDYMIND VIGIANDO", text_color="#2ECC71")
            self.btn_iniciar.configure(text="PAUSAR AUTOMAÇÃO", fg_color="#E74C3C", hover_color="#C0392B")
            self.btn_selecionar.configure(state="disabled")
            
            self.progresso.start()
            self.adicionar_log("🛡️ Varredura inteligente iniciada com sucesso.")
            
            self.thread_monitor = threading.Thread(target=self.rodar_watchdog, daemon=True)
            self.thread_monitor.start()
        else:
            self.monitorando = False
            if self.observer:
                self.observer.stop()
            self.status_label.configure(text="⚙️ SISTEMA PAUSADO", text_color="#E74C3C")
            self.btn_iniciar.configure(text="ATIVAR MONITORAMENTO", fg_color="#2ECC71", hover_color="#27AE60")
            self.btn_selecionar.configure(state="normal")
            
            self.progresso.stop()
            self.progresso.set(0)
            self.adicionar_log("🛑 Automação colocada em espera.")

    def rodar_watchdog(self):
        try:
            for item in self.pasta_alvo.iterdir():
                if item.is_file() and self.monitorando:
                    self.mover_arquivo_interface(item)
        except Exception as e:
            self.adicionar_log(f"⚠️ Erro ao varrer arquivos iniciais: {e}")

        class Handler(FileSystemEventHandler):
            def __init__(self, app): self.app = app
            def on_created(self, event): 
                if not event.is_directory: self.app.mover_arquivo_interface(event.src_path)
            def on_moved(self, event): 
                if not event.is_directory: self.app.mover_arquivo_interface(event.dest_path)

        self.observer = Observer()
        self.observer.schedule(Handler(self), str(self.pasta_alvo), recursive=False)
        self.observer.start()
        
        while self.monitorando:
            time.sleep(1)
        self.observer.join()

if __name__ == "__main__":
    app = AppTidyMind()
    app.mainloop()