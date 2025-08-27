# LSJ — Sistema de Gestão Financeira

## Sobre o Projeto

O Sistema de Gestão Financeira LSJ é uma solução completa para a administração financeira do Lar de São José, oferecendo funcionalidades de conciliação bancária e geração de relatórios oficiais. Esta plataforma foi desenvolvida para otimizar processos financeiros e garantir uma gestão transparente e eficiente.

## Stack Tecnológica

### Backend
- **Python**
  - FastAPI (Framework web de alta performance)
  - SQLAlchemy (ORM para interação com banco de dados)
  - Pydantic (Validação de dados e configurações)
  - Alembic (Migrações de banco de dados)

### Banco de Dados
- **PostgreSQL**

### Frontend
- **React**
  - Vite (Build tool e ambiente de desenvolvimento)
  - Tailwind CSS (Framework CSS utilitário)

## Funcionalidades Principais

- Gestão financeira completa
- Conciliação bancária
- Geração de relatórios oficiais
- Interface intuitiva e responsiva

## Configuração do Ambiente Virtual (Windows/PowerShell)

Para criar e ativar o ambiente virtual Python do projeto:

1. Certifique-se de que o Python 3.11+ está instalado:  
   ```powershell
   python --version
   ```

2. Crie o ambiente virtual dentro da pasta do projeto:  
   ```powershell
   py -3 -m venv .venv
   ```

3. Ative o ambiente virtual:  
   ```powershell
   .venv\Scripts\Activate.ps1
   ```

4. Valide que o ambiente está ativo (o prompt exibirá `(.venv)` no início) e que o `pip` está vinculado ao venv:  
   ```powershell
   python -m pip -V
   ```

> Observação: a pasta `.venv` **não deve ser versionada** (já está listada no `.gitignore`).
