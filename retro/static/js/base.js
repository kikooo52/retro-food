$(document).ready(function() {
    (function(global){
        $('.popupCloseButton').click(function(){
            $('.messageOrederSuccess').hide();
        });
        let order = getOrder();
        if (order){
            $(".header__cart-count").text(order.cartCount);
            checkExpiration(new Date(order.expirationDate));
        }
    
        $(document).on('submit', '#postForm',function(e){
            e.preventDefault();
            let food = $(this);
            submit(food);
            return false;
        });
    
        function submit(food) {
            let foodId = food.find("button").data('myval');
            let quantity = food.find("#id_quantity").val()
            $.ajax({
                type:'POST',
                url: "/bg/cart/add/" + foodId + "/",
                data:{
                    quantity: quantity,
                    update_quantity: false,
                    csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
                    action: 'post'
                },
                success:function(json){
                    document.getElementById("postForm").reset();
                    $('.messageOrederSuccess').show();
                    $('.foodName').html(json.result.quantity + " x " + json.result.food_name +" <span style='color: green'>&#10003; </span>");
                    let cartCount = $(".header__cart-count").text();
                    cartCount = +cartCount + +json.result.quantity;
                    $(".header__cart-count").text(cartCount);
                    setOrder(cartCount);
                },
                error : function(xhr,errmsg,err) {
                    console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
                }
            });
        }

        function setOrder(cartCount) {
            let expirationHours = new Date();
            expirationHours.setHours(expirationHours.getHours() + 2); //two hours from now
            let order = { 'cartCount': cartCount, 'expirationDate': expirationHours.getTime()};
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
    
        $('.removeFood').click(function(e){
            let foodCount = $(this).closest('tr').find('select').val();
            let order = getOrder();
            if (order){
                let newCount = +order.cartCount - +foodCount;
                if (newCount < 0) {
                    newCount = 0;
                }
                setOrder(newCount);
            }
        });

        $('.updateFood').click(function(e){
            let quantities = $("select[name=quantity]");
            let newCount = 0;
            for (let index = 0; index < quantities.length; index++) {
               let quantity = $(quantities[index]).val();
               newCount = newCount + +quantity;
            }
            let order = getOrder();
            if (order){
                setOrder(newCount);
            }
        });

        function checkExpiration(expirationDate) {
            // Check for expiration hours
            if (expirationDate < new Date()) {
                localStorage.removeItem("order");
            }
        }

        global.bundleObj = {
          setOrder: setOrder,
          getOrder: getOrder
        }
    
      })(window)
});