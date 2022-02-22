document.querySelectorAll('.checkbox-label').forEach((label) => {
    label.addEventListener('click', clickInCheckBox)
})

function clickInCheckBox(e) {
    let label = e.currentTarget
    let checkbox = label.parentElement.querySelector('input[type="checkbox"]')
    checkbox.checked = checkbox.checked === true ? false : true
}