function msg()
{
  var message = document.getElementById("chat-msg").value;
  list = document.getElementById("msg-list")
  add = document.getElementById("send")

  add.addEventListener('click', function() {
  list.innerHTML += '<li class="text-right list-group-item">' + message + '</li>';

           var chatlist = document.getElementById('msg-list-div');
            chatlist.scrollTop = chatlist.scrollHeight;
   });
}
