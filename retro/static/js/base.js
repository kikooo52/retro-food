$(document).ready(function() {
    let order = getOrder();
    if (order){
        $(".header__cart-count").text(order.cartCount);
        checkExpiration(new Date(order.date));
    }

    $('.order_btn').click( function(e) {
        debugger
        e.preventDefault(); 
        let cartCount = $(".header__cart-count").text();
        cartCount++;
        $(".header__cart-count").text(cartCount);
        let pk = $(this).data('myval');
        setOrder(cartCount, pk);        
        return false; 
    });

    function setOrder(cartCount, pk) {
        let expirationHour = new Date();
        expirationHour.setHours(expirationHour.getHours() + 1); //one hour from now
        let Ids = [];
        Ids.push(pk);
        let lastOrder = getOrder();
        if (lastOrder) {        
            Ids = Ids.concat(lastOrder.ordersId);
        }

        let order = { 'cartCount': cartCount, 'date': expirationHour.getTime(), 'ordersId': Ids };
        localStorage.setItem('order', JSON.stringify(order));
    }

    function getOrder() {
        let order = localStorage.getItem('order');
        if (order) {
            return JSON.parse(localStorage.getItem('order'));
        } else {
            return false
        }
    }

    function checkExpiration(date) {
        // Check for expiration hour
        if (date < new Date()) {
            localStorage.removeItem("order");
        }
    }    
});