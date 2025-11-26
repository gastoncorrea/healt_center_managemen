from google.adk.agents.llm_agent import Agent
from google.adk.tools import AgentTool
from agent_tool.therapist.therapist_agent import therapist_agent

def get_type_of_user(user_input: str) -> dict:
    """Identifica el tipo de usuario basado en su input.
    
    Args:
        user_input (str): El input proporcionado por el usuario.

    Returns:
        dict: {'status': 'success', 'type_of_user': tipo_de_usuario}
    
    """
    tipo_de_usuario = "Desconocido"

    print(f"[COORDINATOR AGENT]Analizando el input del usuario para identificar el tipo de usuario: {user_input}")

    palabras_claves_potencial = [
        'información general', 'horarios', 'primera consulta',
          'practicas']
    
    palabras_claves_pacientes_existentes = [
        'citas', 'recetas', 'tratamiento', 'mi historial médico']

    palabras_claves_terapeuta = [
        'informacion personal', 'informacion de pacientes', 
        'turnos agendados', 'mi agenda', 'terapeuta', 'psicólogo', 'psicopedagogo','fonoaudiólogo']
    
    input_lower = user_input.lower()

    for palabra in palabras_claves_potencial:
        if palabra in input_lower:
            tipo_de_usuario = "Potencial paciente"
        
    for palabra in palabras_claves_pacientes_existentes:
        if palabra in input_lower:
            tipo_de_usuario = "Paciente existente"

    for palabra in palabras_claves_terapeuta:
        if palabra in input_lower:
            tipo_de_usuario = "Terapeuta"
        
        
    return {'status': 'success', 'tipo_de_usuario': tipo_de_usuario}

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='Un coordinador entre usuario y agentes especializados',
    instruction="""
Eres un agente coordinador que ayuda a los usuarios a interactuar con varios agentes especializados.

Tu tarea es identificar el tipo de usuario con el que estas interactuando.

<Tipo de usuario>
1- Potencial paciente: Busca información general sobre horarios, practicas y/o una primera consulta.
2- Paciente existente: Necesita asistencia con citas, recetas o información específica sobre su tratamiento.
3- Terapeuta: Requiere acceso a informacion personal, informacion de pacientes, turnos agendados.
</Tipo de usuario>

# Pasos a seguir:  
1. Saluda al usuario de manera cordial.
2. Haz preguntas para identificar el tipo de usuario (Potencial paciente, Paciente existente, Terapeuta).
    A) Llama a la herramienta get_type_of_user(user_input: str) para identificar el tipo de usuario.
3. Delega al agente especializado correspondiente según el tipo de usuario identificado:
    A) Si el usuario es identificado como un "Terapeuta"
        - Llama a la herramienta therapist_agent.
4. Interpreta la respuesta del agente especializado y preséntala al usuario de manera clara y concisa.
""",
    tools=[get_type_of_user, AgentTool(agent=therapist_agent)],
)
