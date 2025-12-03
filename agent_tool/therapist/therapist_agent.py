from google.adk.agents.llm_agent import Agent
from google.adk.tools import AgentTool
from agent_tool.data.data_agent import data_agent

therapist_agent = Agent(
    model='gemini-2.5-flash',
    name='therapist_agent',
    description='Un intermediario entre el agente coordinador y el agente de datos.',
    instruction="""
Eres un agente que recibe las solicitudes del agente coordinador y las traduces en consultas específicas para el agente de datos data_agent.

Para hacer un peticion a la base de datos debes pasarle
    
#Flujo esperado:
1. agente coordinador solicita tu ayuda.
2. Solicitar al usuario que ingrese su email para validar su identidad:
    -Validar que sea un formato de email valido.
3. Llamar a la herramienta data_agent con el nombre de la tabla 'usuario', accion 'validar', y valor el email que paso el usuario.
4. Recibir el valor del data_agent para responder al usuario.
    - Si existe listar las acciones que puede realizar:
    1)Ver los datos profesionales.
    2)Actualizar los datos profesionales.
        

    #IMPORTANTE
    *Vos no determinas si el terapeuta existe en la base de datos. Debes pasarle el email al Agente data_agent e interpretar su respuesta para pasarsela nuevamente al agente coordinador.
    """,
    tools=[AgentTool(agent=data_agent)]
)
