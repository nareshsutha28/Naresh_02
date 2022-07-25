function fname_val(){
    var s= document.rform.fname.value;
    var r=/^[A-Za-z]+$/
    if(s=="")
    {
        document.getElementById("fname").innerHTML="enter a name";
    } 
    else if(!r.test(s))
    {
        document.getElementById("fname").innerHTML="Name contain only alphabet";
    }
    else 
    {
        document.getElementById("fname").innerHTML="";
    } 
    
}

function sname_val(){
    var s= document.rform.sname.value;
    var r=/^[A-Za-z]+$/
    if(s=="")
    {
        document.getElementById("sname").innerHTML="enter a surname";
    } 
    else if(!r.test(s))
    {
        document.getElementById("sname").innerHTML="Surname contain only alphabet.";
    } 
    else 
    {
        document.getElementById("sname").innerHTML="";
    }
    
}

function email_val(){
    var s= document.rform.email.value;
    var r=/^[A-Za-z0-9._-]+@[A-Za-z]+\.[a-z]{2,4}$/;
    
    // console(fname)


    if(s=="")
    {
        document.getElementById("email").innerHTML="Please enter a mail ID";

    } 
    else if(!r.test(s))
    {
        document.getElementById("email").innerHTML="Please enter a valid Email Id";
    } 
    else 
    {
        document.getElementById("email").innerHTML="";
    }
}

function mobile_val(){
    var s= document.rform.mobile.value;
    var r=/^\d{10}$/;

    if(s=="")
    {
        document.getElementById("mobile").innerHTML="Please enter a mobile no";

    } 
    else if(!r.test(s))
    {
        document.getElementById("mobile").innerHTML="Please enter a valid mobile no";
    }
    
    else 
        {
            document.getElementById("mobile").innerHTML="";
        }
};



function password_val(){
    var s= document.rform.password.value;
    var r=/^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[^A-Za-z0-9])(?!.*\s).{6,15}$/;

    if(s=="")
    {
        document.getElementById("password").innerHTML="Please enter a password";

    } 
    else if(!r.test(s))
    {
        document.getElementById("password").innerHTML="paaword contain at least one special charactor, uppercase charactor, lowercase charactor, one digit.";
    }
    else 
    {
        document.getElementById("password").innerHTML="";
    }
    
};

function cpassword_val(){
    var s= document.rform.cpassword.value;
    var r=document.rform.password.value;

    if(s=="")
    {
        document.getElementById("cpassword").innerHTML="Please confirm your password";

    }
    else if(r!=s)
    {
        document.getElementById("cpassword").innerHTML="password is not matched";
    }
    else 
    {
        document.getElementById("cpassword").innerHTML="";
    }
    
}