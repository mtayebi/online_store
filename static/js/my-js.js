// function AddOrder(product_id, url) {
//       $.get(url, function(data, status){
//     alert("Data: " + data + "\nStatus: " + status);
//   });
// //     console.log('sssssssss')
// //     $.ajax({
// //     method: 'GET',
// //     headers: {
// //         "X-CSRFToken": '{{ csrf_token }}'
// //     },
// //     url: 'google.com',
// //     success: renderList,
// //         error: function(error){
// //         console.log('sssssssss')
// //         console.log(error)
// //         console.log('sssssssss')
// //     }
// //       });
// // }
// // function renderList(data) {
// //     alert(data);
// }
orders = {}
function AddOrder(product_id, amount){
    orders[product_id] = $("#"+amount).html()
    document.cookie = "orders="+JSON.stringify(orders)
    $("#power").html(Object.keys(orders).length)
    $("#power").attr("hidden",false);
}

function Decrement(amount_id){

    if ($("#"+amount_id).html() >= 2) {
        $("#" + amount_id).html($("#" + amount_id).html()-1)
    }
}

function Increment(amount_id){
        $("#" + amount_id).html(parseInt($("#" + amount_id).html())+1)
}