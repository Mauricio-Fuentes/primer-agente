from tipos import Gasto
from modelo import crear_modelo
from pydantic_ai import Agent
from config import Settings

modelo = crear_modelo(Settings())
mi_agente = Agent(
    model=modelo,
    instructions="Responde en español y en una sola frase")

historial = []
while True:
    texto = input("Tú: ").strip()
    if texto.lower() == "salir":
        print("Chat finalizado.")
        break
    if not texto:
        continue

    resultado = mi_agente.run_sync(texto, message_history=historial)
    historial = resultado.all_messages()
    print(f"Agente: {resultado.output}")
