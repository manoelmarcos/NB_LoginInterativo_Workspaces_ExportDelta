# 📊 Microsoft Fabric – Extração de Workspacescom Python + APIs

Este repositório contém um script 100% funcional no Microsoft Fabric que realiza:

✅ Autenticação interativa via Device Code Flow  
✅ Acesso à API REST do Power BI  
✅ Conversão dos dados em DataFrame Spark  
✅ Armazenamento como Tabela Delta no Lakehouse

---

## 🚀 Objetivo

Automatizar a coleta de informações sobre os Workspaces do Power BI e gravar os dados no Lakehouse do Microsoft Fabric, viabilizando análises de governança, auditoria ou controle organizacional.

---

## 🛠️ Tecnologias Utilizadas

- Python
- MSAL (Microsoft Authentication Library)
- API REST Power BI
- PySpark (no Microsoft Fabric)
- Delta Lake

---

## 📂 Estrutura do Script

| Etapa | Descrição |
|-------|-----------|
| STEP 1 | Importação das bibliotecas |
| STEP 2 | Autenticação via Device Code Flow |
| STEP 3 | Requisição à API do Power BI |
| STEP 4 | Conversão dos dados para DataFrame Spark |
| STEP 5 | Salvamento em tabela Delta no Lakehouse |

---

## 🧪 Como Usar

1. **Abra um notebook no Microsoft Fabric** (Engine: Apache Spark)
2. **Copie e cole o código do script** neste repositório
3. **Substitua o `client_id`** pela aplicação registrada no Entra ID com permissões de leitura para a API do Power BI
4. **Execute o notebook**  
5. Acesse o link exibido e insira o código gerado para autenticar
6. O script criará a tabela Delta `workspaces_fabric` no seu Lakehouse

---

## 📌 Permissões Necessárias

No Entra ID, a aplicação deve conter a permissão delegada:

- `Tenant.Read.All` ou `Workspace.Read.All`  
*(Escopo: `https://analysis.windows.net/powerbi/api/.default`)*

---

## 📦 Saída Esperada

Uma tabela Delta chamada `workspaces_fabric` com as seguintes colunas:

| workspace_id | workspace_name | is_on_dedicated_capacity |
|--------------|----------------|---------------------------|

---

## 💡 Exemplos de Uso

- Inventário de workspaces para governança
- Auditoria de uso e capacidade
- Base de dados para dashboards internos de administração

---

## 📧 Contato

Criado por [Manoel Marcos da Silva](https://www.linkedin.com/in/manoelmarcos/)  
Especialista em Power BI e Microsoft Fabric  
📍 Gravatá – PE, Brasil

---

