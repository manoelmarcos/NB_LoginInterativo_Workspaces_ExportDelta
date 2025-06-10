# STEP 1 – Importações

from msal import PublicClientApplication
import requests
import json
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

# STEP 2 – Autenticação interativa via Device Code Flow

client_id = ""  # 🔁 Substitua aqui

authority = "https://login.microsoftonline.com/common"
scopes = ["https://analysis.windows.net/powerbi/api/.default"]

app = PublicClientApplication(client_id=client_id, authority=authority)
flow = app.initiate_device_flow(scopes=scopes)

if "user_code" not in flow:
    raise Exception("❌ Erro ao iniciar device flow. Verifique o client_id e permissões.")

print(f"👉 Acesse {flow['verification_uri']} e digite o código: {flow['user_code']}")

token_response = app.acquire_token_by_device_flow(flow)
access_token = token_response.get("access_token")

if not access_token:
    raise Exception("❌ Token não foi gerado. Verifique permissões no Entra ID.")
print("✅ Token obtido com sucesso.")

# STEP 3 – Requisição à API do Power BI

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

url = "https://api.powerbi.com/v1.0/myorg/groups"
response = requests.get(url, headers=headers)
response.raise_for_status()

workspaces_json = response.json()

# STEP 4 – Estruturar dados em um DataFrame Spark

workspace_data = [
    {
        "workspace_id": ws.get("id"),
        "workspace_name": ws.get("name"),
        "is_on_dedicated_capacity": str(ws.get("isOnDedicatedCapacity"))
    }
    for ws in workspaces_json["value"]
]

schema = StructType([
    StructField("workspace_id", StringType(), True),
    StructField("workspace_name", StringType(), True),
    StructField("is_on_dedicated_capacity", StringType(), True)
])

df = spark.createDataFrame(workspace_data, schema)

# STEP 5 – Salvar como Tabela Delta no Lakehouse com nome fixo

tabela_nome = "workspaces_fabric"

df.write.format("delta").mode("overwrite").saveAsTable(tabela_nome)

print(f"✅ Tabela Delta '{tabela_nome}' criada com sucesso no Lakehouse.")
