

[RESP] 

Introducción

Los modelos de lenguaje generativos, conocidos como LLMs (Lenguaje generado por modelos), han demostrado ser una revolución en el campo de la inteligencia artificial, con aplicaciones en una amplia variedad de tareas, desde la traducción automática hasta la generación de respuestas a preguntas y la creación de contenido. Sin embargo, estos modelos también han sido objeto de críticas recientes debido a sus sesgos, conocidos como hallucinaciones y omisiones. Estos sesgos, también conocidos como "sesgos de generación de falsedades", se refieren a la capacidad de los modelos para generar respuestas falsas o respuestas incorrectas a preguntas que no están presentes en el conjunto de datos de entrenamiento. Esto se debe a que los LLMs aprenden a predecir respuestas basándose en la distribución de los datos y no en la verdadera realidad, lo que lleva a que sean susceptibles a generar respuestas falsas o omisiones en situaciones nuevas. En este informe, se analizarán los sesgos en los LLMs, concreto los sesgos intrínsecos y extrínsecos, y cómo se propagan en el entrenamiento y la generación de texto.

Los sesgos intrínsecos se refieren a los sesgos presentes en los propios pesos de las conexiones del modelo, mientras que los sesgos extrínsecos se refieren a la influencia de los datos de entrenamiento. Los sesgos intrínsecos se han demostrado en modelos como BERT y GPT-3, lo que ha llevado a la comunidad a investigar métodos para reducirlos, como el enfoque de entrenamiento con datos equilibrados y la regularización de la entropía. Sin embargo, los sesgos extrínsecos han sido menos estudiados, y se han demostrado en los modelos más recientes como GPT-3 y RoBERT.

Los sesgos extrínsecos se refieren a las tendencias en la generación de texto que reflejan las preferencias de los datos de entrenamiento, como la tendencia de los LLMs a generar respuestas que reflejen estereotipos o prejuicios. Estos sesgos se han demostrado en la generación de texto de modelos como BART y T5.

Los sesgos intrínsecos se han analizado en detalle en trabajos anteriores, pero los sesgos extrínsecos son menos conocidos. Este informe se centrará en los sesgos extrínsecos, y cómo se propagan en la generación de texto.

Los sesgos extrínsecos se han demostrado en la generación de texto de los LLMs, pero la extensión de estos sesgos