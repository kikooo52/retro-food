$(document).ready(function() {
    let order = getOrder();
    if (order){
        $(".header__cart-count").text(order.cartCount);
        checkExpiration(new Date(order.date));
    }

    $('.order_btn').click( function(e) {
        debugger             
        e.preventDefault(); 

        removeCookie('idss')
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
            var Idsss = Ids.indexOf(pk) === -1 ? Ids.push(pk) : console.log("This item already exists");
        }
        setCookie('ordersId', JSON.stringify(Ids));
        let order = { 'cartCount': cartCount, 'date': expirationHour.getTime(), 'ordersId': Ids, 'idds':  Idsss};
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
    function setCookie(name, value) {
        var expiration_date = new Date();
        expiration_date.setTime(expiration_date.getTime() + 1 * 3600 * 1000);
        document.cookie = name + '=' + value +'; expires=' + expiration_date.toUTCString() + '; path=/';
    }
    function removeCookie(name) {
        document.cookie = name + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT;path=/;';
    }    
});