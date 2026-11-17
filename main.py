from pyscript import document


grade_7 = {"Yashkin Sunga", "John Pork", "Carlos Aguas"}
grade_8 = {"Lucas Gonzales", "Justine Sunga", "Annalyn Gonzales"}
grade_9 = {"Renelito Fish", "Renelyn Fih", "Shadow black"}
grade_10 = {"Brielle Torres", "Lacey Gonzales", "Madeline Carlost"}


def add_member(e):


    first_name = document.querySelector("#fname").value
    last_name = document.querySelector("#lname").value
    
    full_name = f"{first_name} {last_name}"
    new_member = {full_name}
    
    master_set = grade_7 | grade_8 | grade_9 | grade_10 | new_member
    
    formatted_members = "<br>".join(sorted(master_set))
    
    total_members = len(master_set)
    
    output_div = document.querySelector("#output")
    output_div.classList.remove("d-none")
    output_div.innerHTML = f"""
        All members:<br>
        {formatted_members}<br>
        Total members: {total_members}
    """