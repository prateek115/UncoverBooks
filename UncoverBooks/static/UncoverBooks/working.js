if(localStorage.getItem('cart') == null)
{
   var cart = {};
}
else
{
   cart = JSON.parse(localStorage.getItem('cart'));
   updateCart(cart);
}
$('.divpr').on('click', 'button.cart', function()
{
   var idstr = this.id.toString();
   if(cart[idstr] != undefined)
   {
      qty = cart[idstr][0] + 1;
   }
   else
   {
      qty = 1;
        name = document.getElementById('name'+idstr).innerHTML
        price = document.getElementById('price'+idstr).innerHTML
        cart[idstr] = [qty, name, parseInt(price)];

   }
   console.log(cart);
   updateCart(cart);
});

function updateCart(cart)
{
  var sum = 0;
  for(var item in cart)
  {
    sum += cart[item][0];
//    document.getElementById('div'+item).innerHTML="<button id='minus" + item + "' class='btn btn-primary minus'>-</button> <span id='val" + item + "''>" + cart[item][0] + "</span> <button id='plus" + item + "' class='btn btn-primary plus'> + </button>";
  }
  localStorage.setItem('cart', JSON.stringify(cart));
  document.getElementById('cart-item').innerHTML = sum;
}

$('.divpr').on("click", "button.minus", function() {
    a = this.id.slice(7, );
    cart['pr' + a][0] = cart['pr' + a][0] - 1;
    cart['pr' + a][0] = Math.max(0, cart['pr' + a][0]);
    document.getElementById('valpr' + a).innerHTML = cart['pr' + a][0];
    if (cart['pr' + a][0] == 0)
    {
      document.getElementById('divpr' + a).innerHTML = '<button id="pr'+a+'" class="btn btn-warning cart" style="width:100%">Add to Cart</button>';
      delete cart['pr' + a];
    }
    else
    {
      document.getElementById('valpr' + a).innerHTML = cart['pr' + a][0];
    }
    updateCart(cart);
});

$('.divpr').on("click", "button.plus", function() {
    a = this.id.slice(6, );
    cart['pr' + a][0] = cart['pr' + a][0] + 1;
    document.getElementById('valpr' + a).innerHTML = cart['pr' + a][0];
    updateCart(cart);
});

function clearCart()
{
   cart = JSON.parse(localStorage.getItem('cart'));
   localStorage.clear();
   cart = {};
   updateCart(cart);
}
