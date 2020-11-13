  function Validate() {
    if (document.getElementById('password').value ==
    document.getElementById('passwordConfirm').value) {
    document.getElementById('message').style.color = 'green';
    document.getElementById('message').innerHTML = 'Password is matching';
    document.getElementById('submitbutton').disabled = false;
  } else {
    document.getElementById('message').style.color = 'red';
    document.getElementById('message').innerHTML = 'Password is not matching';
    document.getElementById('submitbutton').disabled = 'disabled'
  }
  }

function validateForm() {
    var a = document.getElementById('firstName').value;
    var b = document.getElementById('lastName').value;
    var c = document.getElementById('email').value;
    var d = document.getElementById('date').value;
    var e = document.getElementById('password').value;
    var f = document.getElementById('passwordConfirm').value;
    console.log(a);
    if (!(a == null || a == "", b == null || b == "", c == null || c == "", d == null || d == "", e == null || e == "", f == null || f == "")) {
      document.getElementById('submitbutton').disabled = false;}
      else
      document.getElementById('submitbutton').disabled = 'disabled';
  }
