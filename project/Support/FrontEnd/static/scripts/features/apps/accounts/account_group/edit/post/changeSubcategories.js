document.querySelector('select#id_category').addEventListener('change', changeSubcategories)
document.addEventListener('DOMContentLoaded', changeSubcategories)


function changeSubcategories(e) {

    let optionSelected = e.currentTarget.value || document.querySelector('#id_category').value
    let subcategories = document.querySelectorAll('.ag-check-box.cb-category')
    subcategories.forEach((subcategory) => {
        if (subcategory.getAttribute('for') === optionSelected) {
            subcategory.classList.remove('invisible')
        } else {
            subcategory.classList.add('invisible')
            subcategory.querySelector('input[type="checkbox"]').checked = false
        }
    })
}