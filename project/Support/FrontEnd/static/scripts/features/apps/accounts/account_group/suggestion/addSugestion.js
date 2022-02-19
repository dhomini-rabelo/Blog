document.querySelector('.add-suggestion').addEventListener('click', addSuggestionForm)
document.addEventListener('keydown', enterForChangeFocus)


function enterForChangeFocus(e) {

    if (e.keyCode === 13) {
        let input = document.querySelector('#id_suggestion')
        if (input){
            input.blur()
        }
    }

}



function addSuggestionForm() {
    setTimeout(() => {
        let container = document.querySelector('.suggestions')
        let divForm = document.createElement('div')
    
        divForm.setAttribute('class', 'suggestion-block center-c current-form-class')
        divForm.innerHTML = `
        <div class="suggestion-block-top sb-x">
            <span class="suggestion-name"><input type="text" name="suggestion" id="id_suggestion" class="input-suggestion-name"></span>
            <div class="suggestion-status-color"><i class="fa-solid fa-circle-exclamation"></i></div>
        </div>
        <div class="suggestion-block-bottom sb-x">
            <span>Status</span>
            <span>Em andamento</span>
        </div>
        `
    
        container.appendChild(divForm)
    
        document.querySelector('#id_suggestion').focus()
        document.querySelector('#id_suggestion').addEventListener('blur', validateSuggestionForm)
    }, 100)
}


function validateSuggestionForm(e) {

    let inputValue = e.currentTarget.value
    let currentForm = document.querySelector('.current-form-class')

    if ((inputValue.trim().length > 0) && (inputValue.trim().length <= 20)) {
        currentForm.innerHTML = `
            <div class="suggestion-block-top sb-x">
                <span class="suggestion-name">${inputValue}</span>
                <div class="suggestion-status-color"><i class="fa-solid fa-circle-exclamation"></i></div>
            </div>
            <div class="suggestion-block-bottom sb-x">
                <span>Status</span>
                <span>Em andamento</span>
            </div>
        `
        currentForm.classList.remove('current-form-class')
    } else {
        currentForm.remove()
    }

}