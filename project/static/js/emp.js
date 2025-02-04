window.addEventListener("load", function () {
    let f_name = document.getElementById("id_f_name");
    let l_name = document.getElementById("id_l_name");
    let age = document.getElementById("id_age");
    let salary = document.getElementById("id_salary");
    let email = document.getElementById("id_email");
    let dept_id = document.getElementById("id_dept_id");
    let project_id = document.getElementById("id_project_id");
    let form = document.getElementById("form");

    function validate_inputs() {
        if (!f_name || !l_name || !age || !salary || !email || !dept_id || !project_id) {
            console.error("One or more form elements are missing!");
            return false;
        }

        if (f_name.value.trim() === "") {
            alert("First name cannot be empty");
            f_name.focus();
            return false;
        }
        if (!/^[A-z]+$/.test(f_name.value)) {
            alert("First name is not valid");
            f_name.focus();
            return false;
        }
        if (l_name.value.trim() === "") {
            alert("Last name cannot be empty");
            l_name.focus();
            return false;
        }
        if (!/^[A-z]+$/.test(l_name.value)) {
            alert("Last name is not valid");
            l_name.focus();
            return false;
        }
        if (age.value === "" || !/^[0-9]+$/.test(age.value)) {
            alert("Invalid age");
            age.focus();
            return false;
        }
        if (salary.value === "" || !/^[0-9]+$/.test(salary.value)) {
            alert("Invalid salary");
            salary.focus();
            return false;
        }
        if (email.value.trim() === "" || !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email.value)) {
            alert("Invalid email");
            email.focus();
            return false;
        }
        if (dept_id.value.trim() === "" || !/^[0-9]+$/.test(dept_id.value)) {
            alert("Invalid department ID");
            dept_id.focus();
            return false;
        }
        if (project_id.value.trim() === "" || !/^[0-9]+$/.test(project_id.value)) {
            alert("Invalid project ID");
            project_id.focus();
            return false;
        }
        return true;
    }
    if (form) {
        form.addEventListener("submit", function (event) {
            if (!validate_inputs()) {
                event.preventDefault();
                console.log("Validation failed");
            } else {
                let formData = new FormData(form);
                fetch('/submit_form', {
                    method: 'POST',
                    body: formData
                })
                .then(response => response.json())
                .then(data => {
                    console.log('Success:', data);
                    alert("Form submitted successfully!");
                })
                .catch((error) => {
                    console.error('Error:', error);
                });
            }
        });
    } else {
        console.error("Form not found!");
    }

   
});
