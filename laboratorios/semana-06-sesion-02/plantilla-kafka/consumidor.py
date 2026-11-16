import json
from kafka import KafkaConsumer


def deserializar_evento(datos):
    return json.loads(datos.decode("utf-8"))

# TODO: usa el mismo nombre de topico que en productor.py.
topico = "TODO_topico"

consumidor = KafkaConsumer(
    topico,
    bootstrap_servers="localhost:9092",
    value_deserializer=deserializar_evento,
    auto_offset_reset="earliest",
    consumer_timeout_ms=10000,
)

for mensaje in consumidor:
    evento = mensaje.value
    # TODO: procesa cada evento como lo necesitarias en tu proyecto
    # (contar, detectar un umbral, o simplemente imprimir).
    print(f"Consumido: {evento}")

consumidor.close()
