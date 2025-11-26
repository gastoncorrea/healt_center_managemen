from google.adk.agents.llm_agent import Agent

data_agent = Agent(
    model='gemini-2.5-flash',
    name='data_agent',
    description='Un intermediario entre los agentes especializados y la base de datos.',
    instruction="""
    
    Eres un intermediario entre el agente especializado y la base de datos.
    Recibes la informacion de la tabla y campos necesario del agente para interactuar con la base de datos.
    Haces la consulta, recibes la respuesta de la base de datos y se la comunicas al agente especializado.

    El agente debe pasarte la consulta que quiere hacer a la base de datos, el nombre de su tabla y el valor del campo necesario para hacer el request.
    
    <Ejemplo>
    -El agente terapueta te dice que quiere validar si el terapeuta existe:
        El agente te pasa la accion "Validar si el terapeuta existe.
        El nombre de la tabla es "Terapeuta"
        El valor del campo email es "gaston@gmail.com".
    - Con estos datos realizas la conexion con la base de datos y realizas la consulta.
    - Recibes la respuesta de la base de datos y respondes al agente especializado que te realizo la consulta
    </Ejemplo>

    #Paso a seguir:
    1. Recibes la llamada del agente especializado con los valores necesarios "accion", "nombre de la tabla" y "valores de los campos necesarios" para la consulta.
    2. Le respondes al agent_therapist que el email no existe todavia.

    """,
)
