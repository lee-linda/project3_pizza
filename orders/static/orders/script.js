
document.addEventListener('DOMContentLoaded', () => {

      $('.minus').click(function () {
        var $input = $(this).parent().find('input');
        var count = parseInt($input.val()) - 1;
        count = count < 0 ? 0 : count;
        $input.val(count);
        $input.change();
        return false;
      });
      $('.plus').click(function () {
        var $input = $(this).parent().find('input');
        var count = parseInt($input.val()) + 1;
        $input.val(count);
        $input.change();
        return false;
      });

});


  function displayToppings(pizza_type, num_toppings, size, priceEach) {

      if (num_toppings === 0)
      {
        document.getElementById('pizza_type0').value = pizza_type;
        document.getElementById('numToppings0').value = num_toppings;
        document.getElementById('size0').value = size;
        document.getElementById('priceEach0').value = priceEach;

        document.getElementById("noTopping").style.display = 'block';
        document.getElementById("withToppings").style.display = 'none';
      }
      else
      {
        document.getElementById('pizza_type').value = pizza_type;
        document.getElementById('numToppings').value = num_toppings;
        document.getElementById('size').value = size;
        document.getElementById('priceEach').value = priceEach;

        document.getElementById('num_toppings').innerHTML = num_toppings;
        document.getElementById("withToppings").style.display = 'block';
        document.getElementById("noTopping").style.display = 'none';
      }
  }

  function displayAddtoCart(item, size, priceEach)
  {
        document.getElementById('item').value = item;
        document.getElementById('size').value = size;
        document.getElementById('priceEach').value = priceEach;

        document.getElementById("noTopping").style.display = 'block';
  }

    function checkQuantity()
    {
        event.preventDefault();

        var item_quan = parseInt(document.getElementById('itemquantity0').value);
        var myForm = document.querySelector("#noTopping");

        if (item_quan > 0)
        {
          myForm.submit();
        }
        else
        {
          alert("Please key in appropriate value for quantity.");
        }
    };


   function checkItem()
    {
        event.preventDefault();

        var item_quan = parseInt(document.getElementById('itemquantity').value);
        var numToppings = parseInt(document.getElementById('numToppings').value);
        var myForm = document.querySelector("#withToppings");

        var toppingsList = document.getElementsByClassName("quantity");
        var toppingName = document.getElementsByClassName("toppingName");

        var i, toppingVal;
        var total = 0;
        var addition = '';

        for (i = 0; i < toppingsList.length; i++) {
          toppingVal = parseInt(toppingsList[i].value);
          total += toppingVal
          // Exit func if toppingVal is not a number
          if (Number.isNaN(toppingVal))
          {
            alert("Please key in appropriate value for quantity of toppings.");
            return;
          }

          // Keep track of toppings selected by user
          if (toppingVal > 0)
            {
              addition += toppingVal;
              addition += ' x '
              addition += toppingName[i].innerHTML
              addition += ', '
            }
          }  //end for

        if (!(item_quan > 0))
        {
          alert("Please key in appropriate value for quantity.");
        }
        else if (total > numToppings)
        {
          alert("Your total number of toppings exceeded maximum allowed toppings.");
        }
        else if (total < numToppings)
        {
          alert("Your total number of toppings has not reached maximum allowed toppings.");
        }
        else
        {
          document.getElementById('addition').value = addition;
          myForm.submit();
        }

    };


  function confirmDeleteAll()
  {
    var myForm = document.querySelector("#deleteAllItem");

    if (confirm("Confirm deletion of all items?")) {
      myForm.submit();
    }
  }


function displayAddSmall(item, size, priceEach)
{
  document.getElementById('sub_small').value = item;
  document.getElementById('sizeS').value = size;
  document.getElementById('priceEachS').value = priceEach;

  document.getElementById("Additions_S").style.display = 'block';
  document.getElementById("Additions_L").style.display = 'none';
}

function displayAddLarge(item, size, priceEach)
{
  document.getElementById('sub_large').value = item;
  document.getElementById('sizeL').value = size;
  document.getElementById('priceEachL').value = priceEach;

  document.getElementById("Additions_L").style.display = 'block';
  document.getElementById("Additions_S").style.display = 'none';
}

function checkSubExtra(size)
  {
      event.preventDefault();

      if (size === "Small")
      {
        var item_quan = parseInt(document.getElementById('itemquantityS').value);
        var myForm = document.querySelector("#Additions_S");

        var extrasName = document.getElementsByClassName("extraS");
        var extrasquant = document.getElementsByClassName("quantityS");
        var extraCharge = document.getElementsByClassName("extraChargeS");
      }

      if (size === "Large")
      {
        var item_quan = parseInt(document.getElementById('itemquantityL').value);
        var myForm = document.querySelector("#Additions_L");

        var extrasName = document.getElementsByClassName("extraL");
        var extrasquant = document.getElementsByClassName("quantityL");
        var extraCharge = document.getElementsByClassName("extraChargeL");
      }

      var i, extraVal;
      var extraPrice = 0;
      var addition = '';

      for (i = 0; i < extrasName.length; i++) {
          extraVal = parseInt(extrasquant[i].value);
          plusCharge = parseFloat(extraCharge[i].value)

          // Exit func if extraVal is not a number
          if (Number.isNaN(extraVal))
          {
            alert("Please key in appropriate value for quantity of extras.");
            return;
          }

          if (extraVal > 0)
            {
              addition += extraVal;
              addition += ' x '
              addition += extrasName[i].innerHTML
              addition += ', '
              extraPrice += extraVal*plusCharge
            }
        }  //end for

      if (!(item_quan > 0))
      {
        alert("Please key in appropriate value for quantity.");
      }
      else
      {
        if (size === "Small")
        {
          document.getElementById('additionS').value = addition;
          var price = parseFloat(document.getElementById('priceEachS').value)
          document.getElementById('priceEachS').value = price + extraPrice
          myForm.submit();
        }
        if (size === "Large")
        {
          document.getElementById('additionL').value = addition;
          var price = parseFloat(document.getElementById('priceEachL').value)
          document.getElementById('priceEachL').value = price + extraPrice
          myForm.submit();
        }
      }

  };
