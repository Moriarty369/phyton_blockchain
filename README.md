# 🚀 AAcoin Blockchain Project

![Blockchain](https://img.shields.io/badge/Blockchain-Python-blue)
![Flask](https://img.shields.io/badge/Flask-Framework-orange)
![Solidity](https://img.shields.io/badge/Solidity-Contract-green)
![Cryptocurrency](https://img.shields.io/badge/Cryptocurrency-AAcoin-brightgreen)

This project implements a custom blockchain, a smart contract in Solidity, and a cryptocurrency called **AAcoin**.

## 🛠️ Technologies Used

- **Python**: For blockchain logic and network node implementation.
- **Flask**: To create the RESTful API that interacts with the blockchain.
- **Solidity**: For developing the smart contract that manages AAcoin.
- **JavaScript/HTML**: For interacting with the blockchain through a web interface (EtherWallet v3).

## 📂 Project Structure

- **`blockchain/`**: Contains the main code for the blockchain and nodes.
- **`smart_contract/`**: This folder contains the smart contract `aacoin.sol`.
- **`etherwallet-v3/`**: Folder for interacting with the blockchain using an Ethereum wallet interface.
- **`nodes.json`**: File containing the list of network nodes.

## 📜 Project Description

### Blockchain
The blockchain component allows the creation of a simple blockchain with functionalities to add transactions, mine blocks, and validate the chain. It implements Proof of Work (PoW) as a consensus mechanism and supports multiple nodes.

### Cryptocurrency - AAcoin
The cryptocurrency **AAcoin** is integrated with the blockchain and enables transactions between nodes. It uses Flask to create an API that facilitates the processes of mining, transactions, and chain verification.

### Smart Contract
The smart contract `aacoin.sol` was developed in Solidity and manages the logic for investing in and selling AAcoins, allowing users to buy and sell coins according to an equity system.

## 🖥️ Installation and Setup

### Requirements

- Python 3.x
- Flask
- Docker (optional, for SQL Server on macOS)
- Node.js (to interact with the web interface)

### Instructions

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your_username/your_repository.git
    cd your_repository
    ```

2. **Install the Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the nodes:**
    - You can run each node on different ports to simulate a distributed network:
    ```bash
    python node1.py
    python node2.py
    python node3.py
    ```

4. **Compile and deploy the smart contract:**
    - Use a tool like Remix or Truffle to deploy `aacoin.sol` on a local or test Ethereum network.

5. **Interact with EtherWallet:**
    - Go to the `etherwallet-v3/` folder and follow the instructions in the `README` to interact with your blockchain from the web.

## 🚀 How to Use the Project

### Mining a Block
Make a GET request to `/mine_block` on the corresponding port of a node to mine a new block.

### Chain Verification
Make a GET request to `/is_valid` to verify if the chain is valid.

### Connect Nodes
To connect new nodes, make a POST request to `/connect_node` with the JSON of nodes.

### Transactions
To add a new transaction, make a POST request to `/post_transaction` with the transaction details.

## 📄 License
This project is licensed under the MIT License. See [LICENSE](./LICENSE) for more details.

## 🧑‍💻 Author
Created by **Abelardo Acosta Cracco**.


# Español:

##🚀 AAcoin Blockchain Project

![Blockchain](https://img.shields.io/badge/Blockchain-Python-blue)
![Flask](https://img.shields.io/badge/Flask-Framework-orange)
![Solidity](https://img.shields.io/badge/Solidity-Contract-green)
![Cryptocurrency](https://img.shields.io/badge/Cryptocurrency-AAcoin-brightgreen)

This project implements a custom blockchain, a smart contract in Solidity, and a cryptocurrency called **AAcoin**.

## 🛠️ Technologies Used

- **Python**: For blockchain logic and network node implementation.
- **Flask**: To create the RESTful API that interacts with the blockchain.
- **Solidity**: For developing the smart contract that manages AAcoin.
- **JavaScript/HTML**: For interacting with the blockchain through a web interface (EtherWallet v3).

## 📂 Project Structure

- **`blockchain/`**: Contains the main code for the blockchain and nodes.
- **`smart_contract/`**: This folder contains the smart contract `aacoin.sol`.
- **`etherwallet-v3/`**: Folder for interacting with the blockchain using an Ethereum wallet interface.
- **`nodes.json`**: File containing the list of network nodes.

## 📜 Project Description

### Blockchain
The blockchain component allows the creation of a simple blockchain with functionalities to add transactions, mine blocks, and validate the chain. It implements Proof of Work (PoW) as a consensus mechanism and supports multiple nodes.

### Cryptocurrency - AAcoin
The cryptocurrency **AAcoin** is integrated with the blockchain and enables transactions between nodes. It uses Flask to create an API that facilitates the processes of mining, transactions, and chain verification.

### Smart Contract
The smart contract `aacoin.sol` was developed in Solidity and manages the logic for investing in and selling AAcoins, allowing users to buy and sell coins according to an equity system.

## 🖥️ Installation and Setup

### Requirements

- Python 3.x
- Flask
- Docker (optional, for SQL Server on macOS)
- Node.js (to interact with the web interface)

### Instructions

1. **Clone the repository:**
    ```bash
    git clone https://github.com/your_username/your_repository.git
    cd your_repository
    ```

2. **Install the Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the nodes:**
    - You can run each node on different ports to simulate a distributed network:
    ```bash
    python node1.py
    python node2.py
    python node3.py
    ```

4. **Compile and deploy the smart contract:**
    - Use a tool like Remix or Truffle to deploy `aacoin.sol` on a local or test Ethereum network.

5. **Interact with EtherWallet:**
    - Go to the `etherwallet-v3/` folder and follow the instructions in the `README` to interact with your blockchain from the web.

## 🚀 How to Use the Project

### Mining a Block
Make a GET request to `/mine_block` on the corresponding port of a node to mine a new block.

### Chain Verification
Make a GET request to `/is_valid` to verify if the chain is valid.

### Connect Nodes
To connect new nodes, make a POST request to `/connect_node` with the JSON of nodes.

### Transactions
To add a new transaction, make a POST request to `/post_transaction` with the transaction details.

## 🧑‍💻 Author
Created by **Abelardo Acosta Cracco with SuperDatScienceTeam Udemy:  https://www.udemy.com/course/blockchain-de-la-a-a-la-z-crea-tu-criptomoneda-en-python/**.



# Español:
## 🚀 AAcoin Blockchain Project

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


## 🧑‍💻 Autor
Creado por **Abelardo Acosta Cracco con SuperDatScience en el curso de Udemy https://www.udemy.com/course/blockchain-de-la-a-a-la-z-crea-tu-criptomoneda-en-python/**.

