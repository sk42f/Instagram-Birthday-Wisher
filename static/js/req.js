function senddeleterequest(){
    var user = document.getElementById("senddelete").getAttribute("data")
    console.log(user)
    $.ajax({
      url: "/delete",
      type: "get",
      data: {username: user},
      success: function(response) {
        window.location.replace('/');
      },
    });     
  }

