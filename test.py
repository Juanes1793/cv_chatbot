import httpx
import asyncio
import time


URL = "http://localhost:8000/chat_stream"


input_data = {
  "conversation_id": "26955b4a-a382-45aa-b11c-d8deccbdd18e",
  "history": [
    {
      "role": "user",
      "content": "Haz un ensayo de 150 palabras sobre la inteligencia artificial. Termina el ensayo con la frase colorin colorado este cuento se ha acabado",
    }
  ]
}

async def test_streaming_endpoint():
    # Usa httpx para hacer una solicitud asíncrona de streaming
    async with httpx.AsyncClient(timeout=None) as client:
        try:
            # Envío de la solicitud POST
            async with client.stream("POST", URL, json=input_data) as response:
                if response.status_code == 200:
                    print("Recibiendo datos de streaming...")
                    # Itera sobre las partes de la respuesta conforme llegan
                    async for line in response.aiter_text():
                        if line:
                            print(f"Chunk recibido: {line}")
                            
                else:
                    print(f"Error en la solicitud: {response.status_code}")
        except Exception as e:
            print(f"Se produjo un error: {str(e)}")

# Ejecuta la función de prueba de forma asíncrona
if __name__ == "__main__":
    asyncio.run(test_streaming_endpoint())