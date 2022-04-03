import { fetchPost } from './../../../../core/api.js'
import { getCookie, setCookie } from './../../../../core/utils.js'

document.querySelector('.add-suggestion').addEventListener('click', addSuggestionForm)
document.addEventListener('keydown', enterForChangeFocus)


function enterForChangeFocus(e) {

    if (e.keyCode === 13) {
        if (document.querySelector('#id_suggestion') === document.activeElement){
            sendForm()
        }
    }

}

function sendForm(){
    let input = document.querySelector('#id_suggestion')
    if (input !== null && input.value.trim() !== ''){
        input.blur()
        document.querySelector('#suggestion-form').submit()
    }else{
        document.querySelector('.suggestion-block.center-c.current-form-class.loading').remove()
    }
}



function addSuggestionForm() {
    setTimeout(() => {
        let container = document.querySelector('.suggestions')
        let divForm = document.createElement('div')
    
        divForm.setAttribute('class', 'suggestion-block center-c current-form-class loading')
        divForm.innerHTML = `
        <form method="POST" class="suggestion-block-top sb-x" id="suggestion-form">
            <span class="suggestion-name"><input type="text" name="suggestion" id="id_suggestion" class="input-suggestion-name"></span>
            <div class="suggestion-status-color"><img src="/media/assets/account_group/suggestions/time.png" alt="" class="suggestion-img"></div>
            <input type="hidden" name="csrfmiddlewaretoken" value="${getCookie('csrftoken')}">
        </form>
        <div class="suggestion-block-bottom sb-x">
            <span>Status</span>
            <span>Em andamento</span>
        </div>
        `
    
        container.appendChild(divForm)
    
        document.querySelector('#id_suggestion').focus()
        document.querySelector('#id_suggestion').removeEventListener('blur', sendForm)
        document.querySelector('#id_suggestion').addEventListener('blur', sendForm)
    }, 100)
}
