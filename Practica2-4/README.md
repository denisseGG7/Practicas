# 2.4 PicoW + OLED + Boton + CHATGTP

>Autor: Guipzot Garibay Denisse Abigail 20211788 SC7C
 
### Código Micropython
_En este apartado se presenta el código .py para  *interacturar con el modelo de lenguaje GPT-3 (CHATGPT)**_
```python
#Guipzot Garibay Denisse Abigail 20211788
#Sistemas Programables SC7C
#2.4 PicoW + OLED + Boton + CHATGTP

#librerias
import json #manejo de datos
import network #conexion a wifi
import time #manejar tiempo de espera 
import urequests #manejo de recursos http
import ssd1306 #pantalla oled

# configuracion de conexion física
i2c = machine.I2C(0, sda=machine.Pin(0), scl=machine.Pin(1), freq=400000) #comuncación
pantalla = ssd1306.SSD1306_I2C(128, 64, i2c) #oled
cmd = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP) #botón

#función para manejar y preguntar a chat gpt
#definición de parametros 
def mod_chat(conexion, contra, endpoint, api_key, model, prompt, limite_tok):
    """
        Description: This is a function to hit chat gpt api and get
            a response.
        
        Parameters:
        
        conexion[str]: The name of your internet connection
        contra[str]: Password for your internet connection
        endpoint[str]: API enpoint
        api_key[str]: API key for access
        model[str]: AI model (see openAI documentation)
        prompt[str]: Input to the model
        limite_tok[int]: The maximum number of tokens to
            generate in the completion.
        
        Returns: Simply prints the response
    """
    #establecer parametros para conexión wifi  
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(conexion, contra)
    
    #ciclo para buscar conexión
    max_wait = 10 #constante de tiempo
    while max_wait > 0:
        #condición para el lapso de tiempo de conexión
      if wlan.status() < 0 or wlan.status() >= 3:
        break
      max_wait -= 1
      print('Buscando conexión. ¡Espere!') #mensaje
      time.sleep(1)
    #condición de despliegue de mensajes en caso de que conexión haya o no encontrado
    if wlan.status() != 3:
       print(wlan.status())
       raise RuntimeError('La conexión ha fallado. Intente más tarde.')
    else:
      print('Conexión exitosa')
      print(wlan.status())
      status = wlan.ifconfig()
    
    #bloque de control de http
    #encabezados
    headers = {'Content-Type': 'application/json',
               "Authorization": "Bearer " + api_key}
    #parametros que contra el cuerpo de la solicitud (modelo, prompt y limite de tokens)
    data = {"model": model,
            "prompt": prompt,
            "limite_tok": limite_tok}
    
    print("Prompt en proceso de envío") #mensaje en consola
    #definición de url a la que se le envia la solicitud junto con los formatos establecidos
    peticion = urequests.post("https://api.openai.com/v1/{}".format(endpoint),
                       json=data,
                       headers=headers)
    #comprobación del procesamiento de la solicitud, si esta ha sido exitosa o no
    if peticion.status_code >= 300 or peticion.status_code < 200:
        print("Lo siento. Hubo un error en generar la respuesta \n" +
              "Estado de la solicitud: " + str(peticion.text))
    else:
        #bloque para procesar la respuesta ya que ha sido aprobada
        #se alamacena la respuesta para su despliegue en pantalla y consola
        print("Petición exitosa")
        response_data = json.loads(peticion.text)
        completion = response_data["choices"][0]["text"]
        print(completion)
        pantalla.fill(0)
        
        #se le da formato de despligue con ayuda de ciclos for para dividir los caracteres
        max_chars_per_line = 15
        lines = [completion[i:i+max_chars_per_line] for i in range(0, len(completion), max_chars_per_line)]

        for i, line in enumerate(lines):
            pantalla.text(line, 0, i * 10)
        pantalla.show() #mostrar en pantalla
    peticion.close() #cerrar conexión HTTP

#función para solicitar un prompt a Chat GPT en caso de presionar el botón
def presionar(x):
    if not cmd.value():
        print("¡Enviando prompt! Se ha presionando el botón") #mensaje en consola
        pantalla.fill(0)#preparar pantalla
        pantalla.text("Prompt enviado", 0, 0) #despliegue de mensaje y posición
        pantalla.show() #mostrar en oled
        
         #datos de conexión, API key a la que se le solicita, qué se solicita y los tokens maximos
        mod_chat("Jesail",
                 "",
                 "completions",
                 "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",
                 "text-davinci-003",
                  "Give me the name of a famous actress",
                 20)

#Configuración de los disparos (presionar) el botón
cmd.irq(trigger=machine.Pin.IRQ_FALLING, handler=presionar)

while True:
    pass
```
### Resultados en consola
_Despliegue de resultados que se muestran en la consola del software de Thonny_
![]()

### Modelo físico 
_Construcción del circuito en manera física y despliegue de resultados_ 

![]()
