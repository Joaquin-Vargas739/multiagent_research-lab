#Definimos los Agentes:

search_tool = DuckSearchTool()

researcher = Agent(
    name="Researcher",
    role="AI Research Specialist",
    goal="Recolectar información actual y relevante desde la web.",
    backstory="Experto en análisis de fuentes públicas y rastreo de información técnica.",
    tools=[search_tool],
    llm="HuggingFaceH4/zephyr-7b-beta"
)

writer = Agent(
    name="Writer",
    role="Technical Writer",
    goal="Redactar un resumen estructurado de alrededor de 500 palabras.",
    backstory="Especialista en comunicación científica y síntesis de información compleja.",
    llm="HuggingFaceH4/zephyr-7b-beta"
)

reviewer = Agent(
    name="Reviewer",
    role="Research Quality Analyst",
    goal="Revisar precisión, coherencia y solidez del contenido final.",
    backstory="Editor académico con experiencia en verificación de hechos.",
    llm="microsoft/deberta-v3-small"
)
