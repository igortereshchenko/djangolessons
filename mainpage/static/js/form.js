$("#checkname").click(function () {

    alert("BT")
    $.ajax({
    type:"GET",
    url:"check_name/",
    data:{
        'name':$("#user_name").val()
    },
    dataType:"text",
    cache:false,
    success:function (data) {
        alert(data)
        return true
    }
    });

});

