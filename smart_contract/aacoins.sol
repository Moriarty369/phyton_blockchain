// SPDX-License-Identifier: UNLICENSED

//Versión del Compilador 
pragma solidity ^0.4.26;

//arrancar contrato inteligente (crar clase)
contract aacoin_ico {

    //Número máximo de coins disponibles para la venta (Integer sin simbolos )
    uint public max_aacoins = 1000000;
    //Conversion rate entre USdollar y aacoins
    uint public usd_to_aacoins = 1;
    //Números de aacoins compradas por inversores
    uint public total_coins_bought = 0;

    //Mapping que al recibir la direccion del inversor, devuelve su equite tanto en AAcoins como en USD 
    mapping(address => uint) equity_aacoins;
    mapping(address => uint) equity_usd;

    //Verificamos (con "funcion") si un inversor puede comprar coins (disponibilidad)
    modifier can_buy_coins(uint usd_invested){
        //el require es una especie de if anidado que va ligado al modifier (function)
        //donde analizamos sin hay siponibilidad de coins (conviertiendo de USD a coins)
        require(usd_invested * usd_to_aacoins + total_coins_bought <= max_aacoins);
        _; //indicamos a la funcion que solo se aplique si es verdadera if:true 
    }
        //funcion para obtener balance de coins de un inversor (address es tipo de dato
        // e investor es nombre de la external-constant y se obtiene de la clave pública
    function equity_in_aacoins(address investor) external constant returns (uint){
            return equity_aacoins[investor];
    }

        //obtener balance de USD de un inversor
    function equity_in_usd(address investor) external constant returns (uint){
            return equity_usd[investor];
    }
        
    //COMPRAR COINS analizando si hay coins disponibles
    function buy_aacoins(address investor, uint usd_invested) external 
        can_buy_coins(usd_invested){
            uint aacoins_bought = usd_invested * usd_to_aacoins;
            equity_aacoins[investor] += aacoins_bought;
           // para no incrementar ambos valores en paralelo se utiliza el mapeo anterior para actualizar la siguiente 
            equity_usd[investor] = equity_aacoins[investor] / usd_to_aacoins;
            total_coins_bought += aacoins_bought;
    }
    //Vender coins
    function sell_aacoins(address investor, uint aacoins_to_sell) external {
            equity_aacoins[investor] -= aacoins_to_sell;
           // para no incrementar ambos valores en paralelo se utiliza el mapeo anterior para actualizar la siguiente 
            equity_usd[investor] = equity_aacoins[investor] / usd_to_aacoins;
            total_coins_bought -= aacoins_to_sell;
    }

}
