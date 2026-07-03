<p align="center">
  <img src="logo.png" alt="TidyMind Logo" width="180px">
</p>

# <p align="center">TidyMind — Automação Inteligente de Arquivos</p>

<p align="center">
  O <b>TidyMind</b> é um automatizador leve e moderno para Windows, projetado para eliminar o caos digital e trazer clareza mental para o seu dia a dia. Ele monitora e organiza pastas bagunçadas (como a sua pasta de Downloads ou Área de Trabalho) em tempo real, movendo cada arquivo para a sua respectiva categoria de forma 100% automatizada.
</p>

<p align="center">
  <a href="https://github.com/sueh0/TidyMind/releases/download/TidyMind/TidyMind.exe">
    <img src="https://img.shields.io/badge/DOWNLOAD-TidyMind%20(.EXE)-success?style=for-the-badge&logo=windows&logoColor=white&color=2ecc71" alt="Botão de Download TidyMind" height="50px">
  </a>
</p>

---

## Funcionalidades Principais

* **Organização em Tempo Real:** O TidyMind fica de "cão de guarda" na pasta escolhida. Assim que um arquivo entra nela, ele é movido instantaneamente.
* **Seleção Dinâmica de Pasta:** Escolha qualquer diretório do seu computador (Downloads, Área de Trabalho, Pendrives, pastas de rede) para ser limpo com apenas um clique.
* **Trava de Segurança Anticorrupção:** O software monitora o tamanho do arquivo bit a bit e só realiza a movimentação quando o navegador ou sistema terminar completamente o download ou cópia, garantindo que nenhum arquivo suma ou quebre.
* **Interface Moderna e Limpa:** Desenvolvido com uma interface gráfica elegante que se adapta automaticamente ao Modo Escuro ou Modo Claro do seu Windows.
* **Painel de Histórico Vivo:** Acompanhe em tempo real exatamente o que a automação está fazendo através do painel de logs integrado.

### Como os arquivos são categorizados?
O TidyMind lê a extensão do arquivo e o envia para pastas específicas criadas automaticamente:
* **Documentos:** `.pdf`, `.docx`, `.txt`, `.rtf`, etc.
* **Planilhas:** `.xlsx`, `.xls`, `.csv`, `.ods`
* **Imagens:** `.jpg`, `.png`, `.gif`, `.webp`, `.ico`, etc.
* **Compactados:** `.zip`, `.rar`, `.7z`, `.tar.gz`
* **Códigos e Web:** `.html`, `.css`, `.js`, `.py`, `.json`, `.md`
* **Áudio e Vídeo:** `.mp3`, `.wav`, `.mp4`, `.mkv`, `.avi`
* **Executáveis:** `.exe`, `.msi`, `.dmg`
* **Outros:** Qualquer extensão desconhecida vai para esta pasta para não poluir o sistema.

---

## Como Usar (Passo a Passo)

1. **Baixe o executável** clicando no grande botão verde de Download no topo desta página.
2. Mova o arquivo `TidyMind.exe` para onde preferir (ex: sua Área de Trabalho).
3. Dê **dois cliques** para abrir o aplicativo.
   > ⚠️ **Nota na primeira execução:** Como o TidyMind é um software independente, o Windows SmartScreen pode exibir um aviso azul. Basta clicar em **"Mais informações"** e depois em **"Executar assim mesmo"**. Isso só acontece na primeira vez!
4. O app iniciará apontando para a sua pasta padrão de *Downloads*. Se quiser mudar, clique em **"Alterar Pasta de Destino"** e escolha a pasta desejada.
5. Clique em **"Ativar Monitoramento"**.
6. Pronto! O TidyMind vai organizar tudo o que já estava solto na pasta e ficará vigiando o diretório em segundo plano. Você pode minimizar a janela e continuar trabalhando normalmente.

---

## Stack

* [Python](https://www.python.org/)
* [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) (Interface Gráfica)
* [Watchdog](https://github.com/gorakhargosh/watchdog) (Monitoramento do Sistema de Arquivos)
* [PyInstaller](https://pyinstaller.org/) (Compilação)

---

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
