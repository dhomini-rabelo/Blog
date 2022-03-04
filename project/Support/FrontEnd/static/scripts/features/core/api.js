export function fetchPost(url, data) {
    return fetch(url, {
        method: 'POST',
        ...data
    }).then(data => data.json())
}

export function fetchGet(url, options) {
    return fetch(url, {
        method: 'GET',
        ...options
    }).then(data => data.json())
}