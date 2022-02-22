document.querySelector('select#id_category').addEventListener('change', changeSubcategories)


function changeSubcategories(e) {

    let optionSelected = e.currentTarget.value
    let subcategories = document.querySelectorAll('.ag-check-box.cb-category')
    subcategories.forEach((subcategory) => {
        if (subcategory.getAttribute('for') === optionSelected) {
            subcategory.classList.remove('invisible')
        } else {
            subcategory.classList.add('invisible')
        }
    })

}