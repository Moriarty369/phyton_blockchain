# 🚀 AAcoin Blockchain Project

![Blockchain](https://img.shields.io/badge/Blockchain-Python-blue)
![Flask](https://img.shields.io/badge/Flask-Framework-orange)
![Solidity](https://img.shields.io/badge/Solidity-Contract-green)
![Cryptocurrency](https://img.shields.io/badge/Cryptocurrency-AAcoin-brightgreen)

Este proyecto implementa una cadena de bloques personalizada, un contrato inteligente en Solidity, y una criptomoneda denominada **AAcoin**. 

## 🛠️ Tecnologías Utilizadas

- **Python**: Para la lógica de blockchain y la implementación de nodos de red.
- **Flask**: Para crear la API RESTful que interactúa con la blockchain.
- **Solidity**: Para el desarrollo del contrato inteligente que gestiona AAcoin.
- **JavaScript/HTML**: Para la interacción con la blockchain desde una interfaz web (EtherWallet v3).

## 📂 Estructura del Proyecto

- **`blockchain/`**: Contiene el código principal de la blockchain y los nodos.
- **`smart_contract/`**: Aquí se encuentra el contrato inteligente `aacoin.sol`.
- **`etherwallet-v3/`**: Carpeta para interactuar con la blockchain usando una interfaz de billetera Ethereum.
- **`nodes.json`**: Archivo con la lista de nodos de la red.

## 📜 Descripción del Proyecto

### Blockchain
El componente de blockchain permite la creación de una cadena de bloques simple, con funcionalidades para añadir transacciones, minar bloques, y validar la cadena. Implementa Proof of Work (PoW) como mecanismo de consenso y soporte para múltiples nodos.

### Cryptocurrency - AAcoin
La criptomoneda **AAcoin** está integrada con la blockchain y permite transacciones entre nodos. Utiliza Flask para crear una API que facilita el proceso de minado, transacciones, y verificación de la cadena.

### Smart Contract
El contrato inteligente `aacoin.sol` fue desarrollado en Solidity y gestiona la lógica de inversión y venta de AAcoins, permitiendo a los usuarios comprar y vender monedas de acuerdo a un sistema de equity.

## 🖥️ Instalación y Configuración

### Requisitos

- Python 3.x
- Flask
- Docker (opcional, para SQL Server en macOS)
- Node.js (para interactuar con la interfaz web)

### Instrucciones

1. **Clonar el repositorio:**
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    cd tu_repositorio
    ```

2. **Instalar las dependencias de Python:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Ejecutar los nodos:**
    - Puedes ejecutar cada nodo en diferentes puertos para simular una red distribuida:
    ```bash
    python node1.py
    python node2.py
    python node3.py
    ```

4. **Compilar y desplegar el contrato inteligente:**
    - Utiliza una herramienta como Remix o Truffle para desplegar `aacoin.sol` en una red Ethereum local o de prueba.

5. **Interacción con EtherWallet:**
    - Dirígete a la carpeta `etherwallet-v3/` y sigue las instrucciones en `README` para interactuar con tu blockchain desde la web.

## 🚀 Cómo Usar el Proyecto

### Minado de un Bloque
Haz una solicitud GET a `/mine_block` en el puerto correspondiente de un nodo para minar un nuevo bloque.

### Verificación de la Cadena
Haz una solicitud GET a `/is_valid` para verificar si la cadena es válida.

### Conectar Nodos
Para conectar nuevos nodos, haz una solicitud POST a `/connect_node` con el JSON de nodos.

### Transacciones
Para añadir una nueva transacción, haz una solicitud POST a `/post_transaction` con los detalles de la transacción.

## 📄 Licencia
Este proyecto está bajo la Licencia MIT. Ver [LICENSE](./LICENSE) para más detalles.

## 🧑‍💻 Autor
Creado por **Abelardo Acosta Cracco**.

