
    let f_name = this.document.getElementById("id_f_name");
    let l_name = this.document.getElementById("id_l_name");
    let age = this.document.getElementById("id_age");
    let salary = this.document.getElementById("id_salary");
    let email = this.document.getElementById("id_email");
    let dept_id = this.document.getElementById("id_dept_id");
    let project_id = this.document.getElementById("id_project_id");
    function validate_inputs(){
        if(f_name.value.trim() === ""){
            alert("firstname cant not be empty");
            f_name.focus();
            return false;
        }
        if(!/^[A-z]+$/.test(f_name)){
            alert("first name not valid");
            f_name.focus();
            return false ;
        }
        if(l_name_name.value.trim() === ""){
            alert("firstname cant not be empty");
            f_name.focus();
            return false;
        }
        if(!/^[A-z]+$/.test(l_name)){
            alert("first name not valid");
            f_name.focus();
            return false ;
        }
        if(age.value===""){
            alert("age can no be empty");
            age.focus();
            return false;
        }
        if(!/^[0-9]+$/.test(age)){
            alert("not valid value for age ");
            age.focus();
            return false
        }
        if(salary.value===""){
            alert("salary cant not be empty");
            salary.focus();
            return false;
        }
        if(!/^[0-9]+$/.test(salary)){
            alert("not valid value for age ");
            salary.focus();
            return false;
        }
        if(email.value.trim() === ""){
            alert("email cannot be empty");
            email.focus();
            return false;
        }
        if(!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)){
            alert("not a valid email address");
            email.focus();
            return false;
        }
        if(dept_id.value.trim() === ""){
            alert("department ID cannot be empty");
            dept_id.focus();
            return false;
        }
        if(!/^[0-9]+$/.test(dept_id.value)){
            alert("not a valid value for department ID");
            dept_id.focus();
            return false;
        }
        if(project_id.value.trim() === ""){
            alert("project ID cannot be empty");
            project_id.focus();
            return false;
        }
        if(!/^[0-9]+$/.test(project_id.value)){
            alert("not a valid value for project ID");
            project_id.focus();
            return false;
        }
        return true;
    }
    validate_inputs();
    let form = this.document.getElementById("form");
    form.addEventListener("submit",function(event){
        if(validate_inputs()){
            alert("Form submitted successfully!");
            form.reset();
        }
        else{
            event.preventDefault();
            form.reset();
            console.log('atia');
        }
    });
let btn = document.getElementById("butn");
btn.addEventListener("click",function(){
    console.log("atia");
})