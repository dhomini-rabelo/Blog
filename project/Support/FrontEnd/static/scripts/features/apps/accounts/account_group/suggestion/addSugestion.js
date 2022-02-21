import { fetchPost } from './../../../../core/api.js'
import { getCookie, setCookie } from './../../../../core/utils.js'

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
    
        divForm.setAttribute('class', 'suggestion-block center-c current-form-class loading')
        divForm.innerHTML = `
        <div class="suggestion-block-top sb-x">
            <span class="suggestion-name"><input type="text" name="suggestion" id="id_suggestion" class="input-suggestion-name"></span>
            <div class="suggestion-status-color"><img src="/media/assets/account_group/suggestions/time.png" alt="" class="suggestion-img"></div>
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


async function validateSuggestionForm(e) {

    let inputValue = e.currentTarget.value
    let container = document.querySelector('.suggestions')
    let currentForm = document.querySelector('.current-form-class')

    if ((inputValue.trim().length > 0) && (inputValue.trim().length <= 50)) {
        currentForm.innerHTML = `
            <div class="suggestion-block-top sb-x">
                <span class="suggestion-name">${inputValue}</span>
                <div class="suggestion-status-color"><img src="/media/assets/account_group/suggestions/time.png" alt="" class="suggestion-img"></div>
            </div>
            <div class="suggestion-block-bottom sb-x">
                <span>Status</span>
                <span>Em andamento</span>
            </div>
        `
        currentForm.classList.remove('current-form-class')
        if ((getCookie('email')==='')||(getCookie('access_token')==='')||(getCookie('refresh_token')==='')) {
            window.location.pathname = `/api/token/get-cookie?latest_url=${document.URL}`
        }
        let path = document.location.pathname
        let index = path.indexOf('sugestao/')
        let url
        switch(path.slice(index+8)){
            case '/categorias':
                url = `${window.location.origin}/api/category-suggestion/view-or-create`
                break
            case '/sub-categorias':
                url = `${window.location.origin}/api/subcategory-suggestion/view-or-create`
                break
        }
        let body = {
            name: inputValue,
            email: getCookie('email').slice(1, -1),
        }
        let response = await fetchPost(url, {
            body: JSON.stringify(body),
            headers: {
                'Content-Type': "application/json",
                Authorization: `Bearer ${getCookie('access_token')}`,
            }
        })
        if (response.status == 401){
            let newAccessToken = await fetchPost(`${window.location.origin}/api/token/refresh-token`, {
                body: JSON.stringify({refresh: getCookie('refresh_token')}),
                headers: {
                    'Content-Type': "application/json",
                }
            }).then(data => data.access)
            setCookie('access_token', newAccessToken, 3)
            let newResponse = await fetchPost(url, {
                body: JSON.stringify(body),
                headers: {
                    'Content-Type': "application/json",
                    Authorization: `Bearer ${newAccessToken}`,
                }
            })
            if (newResponse.status == 401){
                window.location.pathname = `/api/token/get-cookie?latest_url=${document.URL}`
            }
        }
    } else if (inputValue.trim().length > 50){
        currentForm.remove()
        let error = document.createElement('div')
        error.setAttribute('class', 'error')
        error.innerHTML = '<span class="error-message"><img src="/static/admin/img/icon-no.svg" alt="error-img">Sugestão deve ter no máximo 50 caracteres</span>'
        container.appendChild(error)
        setTimeout(() => {
            error.remove()
        }, 5000)
    } else {
        currentForm.remove()
    }

}