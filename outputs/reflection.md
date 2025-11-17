# Reflexión Personal: Multi-Agent vs RAG — Mi experiencia en Lima


### 1. ¿Cómo manejó el multi-agent la ambigüedad y contradicciones?

En el Exercise 1, los agentes (researcher, writer, reviewer) funcionaron como un equipo. El researcher buscaba info con DuckDuckGo, el writer hacía un borrador, y el reviewer chequeaba errores. Para ambigüedad, como en temas como "bias in LLMs", el reviewer detectaba contradicciones (por ejemplo, una fuente decía que el bias se soluciona con más data, otra que no) y mandaba de vuelta al writer para refinar. Pero a veces el loop se ponía lento si el reviewer era muy estricto. Usando Ollama local, evité problemas de conexión, pero si el prompt no era claro, los agentes repetían cosas.


### 2. ¿Cómo manejó el RAG la factuality y cobertura de retrieval?

En el Task 2, el RAG fue más directo: chunks de Wikipedia en ChromaDB, retrieval con top 5, y generación con Mistral. Para factualidad, fue genial porque solo usaba data de Wikipedia, es decir, la data no es totalmente factual. La cobertura fue buena para preguntas específicas, ya que retrievaba chunks relevantes sobre privacidad y comunicación. Pero si la pregunta era muy amplia, a veces no cubría todo porque dependía de lo que tenía el vector store. Con Ollama, el summary salió coherente, pero tuve que ajustar el prompt para llegar a 400–500 palabras.


### 3. ¿Cuál es mejor para preguntas open-ended vs. factual?

Para preguntas factuales (por ejemplo, *"explica desafíos de FL en salud"*), RAG es mejor: rápido, preciso y basado en datos reales sin divagar.  
Para preguntas open-ended, multi-agent es superior: el reviewer maneja contradicciones y el writer sintetiza ideas creativas. El multi-agent es como un brainstorming, pero más lento; RAG es directo pero limitado a la base de datos.



